# Arrays — Complete Interview Prep Guide

A single place to revise everything about arrays/lists in Python for coding
interviews: how they work, what every operation costs, the edge cases that
break solutions, and the core patterns with runnable, tested code.

> All `.py` files here are **runnable and self-testing**. Run any of them
> directly (`python3 fundamentals.py`) — they execute `assert`-based tests and
> print a short demo. If a file runs without raising, every example passed.

---

## Files in this folder

| File | What it covers |
|------|----------------|
| `fundamentals.py` | Python `list` internals, every operation + its Big-O, common gotchas/pitfalls |
| `array_tricks.py` | The 11 core array patterns, each runnable with inline `assert` tests |
| `edge_cases.py`   | A concrete, runnable edge-case checklist (empty/single/dup/negatives/...) |
| `COMPLEXITY.md`   | The *why* behind every Big-O here — the reasoning/trick that derives it |
| `README.md`       | This guide — fundamentals, complexity tables, checklists, pattern index |

---

## 1. What is an array (in Python)?

A Python `list` is a **dynamic array**: a contiguous block of pointers to
objects, that grows automatically. It is *not* a fixed-size C array.

- **Indexing is O(1)** — direct pointer arithmetic.
- **Append is amortized O(1)** — the backing store over-allocates, so most
  appends are free; occasionally it reallocates and copies (O(n) for that one
  append, but averaged out it's O(1)).
- Elements can be **any type** and **mixed types** (`[1, "a", None]`).
- Lists are **mutable** and **passed by reference** — a function can mutate the
  caller's list. This is the #1 source of interview bugs (see gotchas).

For fixed-type numeric arrays use `array.array` or `numpy`; interviews almost
always mean `list`.

---

## 2. Operation complexity (memorize this table)

| Operation | Example | Time | Notes |
|-----------|---------|------|-------|
| Index read/write | `a[i]` | O(1) | |
| Append | `a.append(x)` | O(1) amortized | occasional O(n) resize |
| Pop from end | `a.pop()` | O(1) | |
| Pop / insert at front or middle | `a.pop(0)`, `a.insert(i, x)` | **O(n)** | shifts elements — avoid in loops |
| Membership test | `x in a` | **O(n)** | use a `set`/`dict` for O(1) |
| Search index | `a.index(x)` | O(n) | |
| Length | `len(a)` | O(1) | stored, not counted |
| Slice | `a[i:j]` | O(k) | copies k elements |
| Concatenate | `a + b` | O(n+m) | new list |
| Extend | `a.extend(b)` | O(m) | in place |
| Sort | `a.sort()` | O(n log n) | Timsort, stable, in place |
| Reverse | `a.reverse()` / `a[::-1]` | O(n) | latter copies |
| Min/max/sum | `min(a)` | O(n) | |
| Count | `a.count(x)` | O(n) | |
| Copy | `a.copy()` / `a[:]` | O(n) | **shallow** |

**Space:** a plain list of n items is O(n). A slice/copy/comprehension that
builds a new list is extra O(n) space — call it out when asked for O(1) space.

> Want the *reasoning* behind these numbers (why append is amortized O(1), why a
> sliding window isn't O(n²), etc.)? See **`COMPLEXITY.md`** — it derives each
> bound from the trick that produces it.

---

## 3. Edge-case checklist (run through this for EVERY array problem)

Before coding, ask / handle:

- [ ] **Empty array** `[]` — does your code index `arr[0]` blindly? It will crash.
- [ ] **Single element** `[x]` — two-pointer / windowing loops may not enter.
- [ ] **Two elements** `[a, b]` — smallest case where pointers actually move.
- [ ] **All duplicates / all same value** `[5, 5, 5]` — dedup logic, counts.
- [ ] **Negative numbers** — breaks "init max to 0" (use `-inf` or `arr[0]`).
- [ ] **Zeros** — break product / division approaches.
- [ ] **Already sorted & reverse sorted** — best/worst case for many algos.
- [ ] **Even vs odd length** — median, pairing, middle index.
- [ ] **Target/element not present** — return sentinel (`-1`, `[]`, `None`)?
- [ ] **Multiple valid answers** — any one? all? first? clarify.
- [ ] **k boundaries** — `k = 0`, `k = n`, `k > n`, `k < 0` for windows/rotation.
- [ ] **Very large input** — does O(n²) pass? Is O(1) space required?
- [ ] **Mutation allowed?** — may you modify the input, or must you copy?
- [ ] **Integer overflow** — not an issue in Python (arbitrary precision ints),
      but mention it if the interviewer expects C/Java reasoning.

### Clarifying questions to ask the interviewer
- Size constraints? Value range? Sorted? Duplicates allowed?
- Can I modify the input? Is extra space allowed (target space complexity)?
- What to return when there's no valid answer / ties?

---

## 4. Pattern index (see `array_tricks.py`)

| Pattern | When to reach for it | Typical complexity |
|---------|----------------------|--------------------|
| **Two pointers** | sorted array, pair/triplet sums, in-place dedup, palindrome | O(n) time, O(1) space |
| **Sliding window** | contiguous subarray/substring with a constraint (fixed or variable size) | O(n) |
| **Kadane's** | maximum-sum contiguous subarray | O(n) |
| **Prefix sum** | many range-sum queries, subarray-sum-equals-k (with hashmap) | O(n) build, O(1) query |
| **Dutch national flag** | sort/partition into 3 groups in one pass (Sort Colors) | O(n), O(1) |
| **Cyclic sort** | values in range `1..n`, find missing/duplicate | O(n), O(1) |
| **In-place reversal rotation** | rotate by k without extra array | O(n), O(1) |
| **Binary search** | sorted array, "search space" answers, first/last occurrence, rotated | O(log n) |
| **Matrix staircase search** | row- and column-sorted matrix | O(m+n) |
| **Product except self** | products/sums without division | O(n), O(1) extra |
| **Boyer–Moore majority vote** | element appearing > n/2 times | O(n), O(1) |

---

## 5. Decision guide — "which pattern?"

```
Is the array sorted?
├── Yes → binary search / two pointers
└── No
    ├── Need contiguous subarray w/ constraint? → sliding window / Kadane
    ├── Need range sums repeatedly?             → prefix sum
    ├── Values are 1..n?                         → cyclic sort
    ├── Need to sort into ≤3 buckets in place?  → Dutch national flag
    ├── O(1) lookups needed?                     → hash set / dict
    └── Otherwise                                → sort first, or brute force then optimize
```

---

## 6. Python idioms worth knowing (interview-friendly)

```python
a[::-1]                      # reversed copy
a.sort(key=lambda x: (x[1], x[0]))   # multi-key sort (stable)
sorted(a, reverse=True)      # new sorted list, descending
prefix = list(itertools.accumulate(a))   # running sums
from collections import Counter; Counter(a)   # frequency map
[x for x in a if x != val]   # filter
enumerate(a)                 # index + value
zip(a, b)                    # pair up two lists
min(a, key=abs)              # min by custom key
float('inf'), float('-inf')  # safe sentinels for min/max init
```

See `fundamentals.py` for the full, runnable list of operations and gotchas.
