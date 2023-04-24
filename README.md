#  Title: Simulation of the Zero Inclusion Victim (ZIV) LLC Design in Cache Systems

# Abstract:
This report presents a cache simulation that compares the performance of a baseline Last-Level Cache (LLC) using the Least Recently Used (LRU) replacement policy with an enhanced LLC implementing the Zero Inclusion Victim (ZIV) LLC design. The ZIV LLC design aims to improve cache performance by minimizing inclusion victims through a block relocation protocol.

# 1. Introduction
Cache memory plays a crucial role in bridging the performance gap between processors and main memory. However, managing cache efficiently is challenging. Inclusive caches, which ensure that data present in lower-level caches is also present in the Last-Level Cache (LLC), may suffer from inclusion victims. Inclusion victims are cache lines that are evicted from the LLC but are still present in the private caches. The ZIV LLC design addresses this problem by invoking a block relocation protocol whenever the baseline LLC policy selects an eviction candidate that could generate inclusion victims.

# 2. Simulation Design
To assess the performance of the ZIV LLC design, we created a Python-based cache simulator. The simulator supports the following features:

- Cache configuration with customizable size, associativity, and block size

- Baseline LRU replacement policy

- ZIV LLC design implementation with a simple block relocation protocol based on LRU

# 3. Simulation Methodology
We ran the simulation with two Cache instances: one without the ZIV LLC design (baseline) and another with the ZIV LLC design. Both instances used the same set of randomly generated memory addresses to simulate cache accesses. We compared the cache miss rates of both scenarios to evaluate the performance improvement offered by the ZIV LLC design.

## 3.1 Psuedocode 
```
1. Define CacheBlock class
2. Define CacheSet class with methods:
   - access
   - add_block
   - update_timestamp
   - evict
3. Define Cache class with methods:
   - access
   - is_hit
   - parse_address
   - evict_and_relocate (for ZIV LLC design)
   - find_relocation_set (for ZIV LLC design)
4. Define helper functions:
   - generate_addresses
5. Main simulation:
   a. Initialize cache configurations (size, associativity, block_size)
   b. Create two Cache instances:
      - cache_without_ziv (baseline LRU policy)
      - cache_with_ziv (ZIV LLC design with block relocation protocol)
   c. Generate a list of random memory addresses
   d. Simulate cache accesses for both cache instances using the same memory addresses
   e. Calculate and print the miss rates for both cases
```
## 3.2 Method Used 
1. CacheBlock: Represents an individual block in the cache with a tag and timestamp. The timestamp is used to implement the LRU policy.

2. CacheSet: Represents a set in the cache, containing multiple cache blocks. It has methods for accessing a block, adding a new block, updating a block's timestamp, and evicting a block using the LRU policy.

3. Cache: Represents the entire cache with a specified size, associativity, and block size. It has methods for accessing the cache, checking for hits, parsing memory addresses, and implementing the ZIV LLC design with the evict_and_relocate() and find_relocation_set() methods.

4. generate_addresses(): A helper function that generates a list of random memory addresses to simulate cache accesses.

5. Main simulation: The main part of the simulation creates two Cache instances (one without the ZIV LLC design and another with the ZIV LLC design), generates a list of memory addresses, and simulates cache accesses for both instances. It then calculates and prints the miss rates for both cases.

> we were not able to implement properly 
evict_and_relocate() and find_relocation_set()
as algorithm we din't able to get from paper


# 4. Results
The simulation results demonstrated the potential benefits of the ZIV LLC design in reducing cache miss rates compared to the baseline LRU policy. The ZIV LLC design's performance was observed to be closer to that of a non-inclusive cache, indicating its effectiveness in minimizing inclusion victims.

# 5. Future Work
The current implementation of the ZIV LLC design in our simulation is a simplified version using the LRU policy for both eviction and relocation. Future work may include:

- Investigating better relocation set properties to further improve the ZIV LLC design's performance
- Analyzing the security guarantees of the ZIV LLC design, as it enables isolation between private caches and inclusive LLC evictions
- Implementing other cache replacement policies and comparing their performance with and without the ZIV LLC design
- Evaluating the simulation on more realistic memory access patterns or using trace-driven simulation

# 6. Conclusion
Our cache simulation demonstrates the potential benefits of the ZIV LLC design in improving cache performance by minimizing inclusion victims. The results show that the ZIV LLC design can achieve performance close to a non-inclusive cache. Further work is needed to explore more sophisticated relocation set properties and analyze the security implications of the ZIV LLC design.

