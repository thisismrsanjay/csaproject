import random

# Cache states
MODIFIED = "M"
EXCLUSIVE = "E"
SHARED = "S"
INVALID = "I"

class CacheLine:
    def __init__(self, tag, state=INVALID):
        self.tag = tag
        self.state = state

class Cache:
    def __init__(self, size=4):
        self.lines = [CacheLine(None, INVALID) for _ in range(size)]

    def find_line(self, tag):
        for line in self.lines:
            if line.tag == tag:
                return line
        return None

    def evict_lru(self, tag):
        evicted_line = random.choice(self.lines)
        evicted_line.tag = tag
        evicted_line.state = INVALID
        return evicted_line

class MemoryHierarchy:
    def __init__(self, num_processors=2, cache_size=4):
        self.processors = [Cache(cache_size) for _ in range(num_processors)]

    def access_memory(self, processor_id, tag):
        cache = self.processors[processor_id]
        line = cache.find_line(tag)

        if line is None:
            line = cache.evict_lru(tag)
            other_caches = [p for i, p in enumerate(self.processors) if i != processor_id]
            for other_cache in other_caches:
                other_line = other_cache.find_line(tag)
                if other_line is not None:
                    if other_line.state == MODIFIED:
                        line.state = SHARED
                        other_line.state = SHARED
                    elif other_line.state == EXCLUSIVE:
                        line.state = SHARED
                        other_line.state = SHARED
                    elif other_line.state == SHARED:
                        line.state = SHARED
                    break
            else:
                line.state = EXCLUSIVE

        return line

def main():
    hierarchy = MemoryHierarchy(num_processors=4, cache_size=4)
    num_accesses = 10
    tags = ["A", "B", "C", "D", "E", "F", "G", "H"]

    for i in range(num_accesses):
        processor_id = random.randint(0, len(hierarchy.processors) - 1)
        tag = random.choice(tags)
        print(f"Processor {processor_id} accesses memory address {tag}")
        line = hierarchy.access_memory(processor_id, tag)
        print(f"Cache line: tag={line.tag}, state={line.state}\n")

if __name__ == "__main__":
    main()
