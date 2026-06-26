# Data Structures — Complete Interview Prep Guide (Python)

A revision-ready reference for every core data structure. Each topic folder is a
self-contained guide built to the **same structure**, so once you know one you
know how to navigate them all.

## The 5-file structure (every folder)

| File | Purpose |
|------|---------|
| `README.md` | Master guide: what it is, Big-O operation table, edge-case checklist, clarifying questions, pattern index, decision guide, idioms |
| `fundamentals.py` | Every core operation + complexity + a **gotchas** section — runnable & `assert`-tested |
| `*_tricks.py` | The core interview **patterns**, each a real callable with inline tests |
| `edge_cases.py` | Runnable edge-case categories: naive-breaks vs robust, proven with asserts |
| `COMPLEXITY.md` | The **why/trick** behind each Big-O (amortized analysis, charging arguments, ...) |

> **Every `.py` file is runnable and self-testing.** Run it directly
> (`python3 arrays/array_tricks.py`); a clean exit + a `✔` line means all
> examples/patterns passed. Stdlib only — no external dependencies.

## Topics

| Topic | Folder | Core patterns covered |
|-------|--------|-----------------------|
| Arrays | [`arrays/`](arrays/) | two pointers, sliding window, Kadane, prefix sum, Dutch flag, cyclic sort, rotation, binary search, matrix search, product-except-self, Boyer–Moore |
| Linked Lists | [`linked_list/`](linked_list/) | reverse, fast/slow pointers, Floyd's cycle, merge sorted, Nth-from-end, intersection, palindrome, reorder, dummy node |
| Hash Maps / Sets | [`hashmap/`](hashmap/) | complement (two-sum), frequency count, group anagrams, dedup, subarray-sum-k, sliding window counts, first unique, LRU cache |
| Stacks & Queues | [`stacks_queues/`](stacks_queues/) | monotonic stack, valid parentheses, min stack, queue-from-stacks, sliding-window-max, calculator, decode string |
| Heaps / Priority Queues | [`heaps/`](heaps/) | kth largest, top-k frequent, merge k sorted, median (two heaps), k closest points, reorganize, last stone weight (+ from-scratch `max_heap.py`) |
| Trees & BSTs | [`trees/`](trees/) | traversals (DFS/BFS, Morris), depth, diameter, invert, balance, LCA, path sum, serialize, build from traversals |
| Tries (Prefix Trees) | [`trie/`](trie/) | insert/search/prefix/delete, wildcard dictionary, Word Search II, autocomplete, replace words, max XOR (binary trie) |
| Graphs | [`graphs/`](graphs/) | BFS/DFS, shortest path, connected components, cycle detection, topological sort, Dijkstra, bipartite, islands, union-find (+ `adjacency_list.py`) |

## How to use this for interview prep

1. Skim the topic `README.md` for the Big-O table and the **pattern index**.
2. Read `COMPLEXITY.md` to understand *why* the bounds hold — so you can derive
   them under pressure instead of memorizing.
3. Run the `*_tricks.py` file and read each pattern; they're the templates you'll
   adapt to real problems.
4. Before submitting any solution, walk it through `edge_cases.py` for that topic.

Worked problem sets that apply these patterns live in
[`../Questions/`](../Questions/).
