# Heaps / Priority Queues — Complete Interview Prep Guide

A single place to revise everything about heaps and priority queues in Python
for coding interviews: how a binary heap works, what every operation costs, the
edge cases that break solutions, and the core patterns with runnable, tested
code.

> All `.py` files here are **runnable and self-testing**. Run any of them
> directly (`python3 fundamentals.py`) — they execute `assert`-based tests and
> print a short demo. If a file runs without raising, every example passed.

---

## Files in this folder

| File | What it covers |
|------|----------------|
| `fundamentals.py` | Every `heapq` operation + its Big-O, max-heap via negation, tuple/counter priority, common gotchas |
| `heap_tricks.py`  | The 7 core heap patterns (k-th largest, top-k, merge-k, running median, k-closest, reorganize, last stone), each runnable with inline `assert` tests |
| `edge_cases.py`   | A concrete, runnable edge-case checklist (empty pop / k>n / k=0 / dups / unorderable ties / single / negatives) |
| `max_heap.py`     | A from-scratch `MaxHeap` class (sift-up/down, heapify, remove) — the mechanics `heapq` hides |
| `COMPLEXITY.md`   | The *why* behind every Big-O here — especially why `heapify` is O(n), not O(n log n) |
| `README.md`       | This guide — fundamentals, complexity tables, checklists, pattern index |

---

## 1. What is a binary heap?

A **binary heap** is a **complete binary tree** (every level full except
possibly the last, which fills left-to-right) that satisfies the **heap
property**:

- **Min-heap:** every parent `<=` its children → the **minimum** is at the root.
- **Max-heap:** every parent `>=` its children → the **maximum** is at the root.

Because the tree is *complete*, it is stored in a **plain array** with no
pointers — the tree shape is implied by the indices:

```
          index 0
         /        \
     index 1      index 2
     /     \       /
  idx 3   idx 4  idx 5

parent(i)      = (i - 1) // 2
left_child(i)  = 2*i + 1
right_child(i) = 2*i + 2
```

The heap property is **weaker than sorting**: it only relates each parent to its
children, not siblings. So the root is the min/max, but `heap[1]` is **not**
necessarily the 2nd smallest. This is exactly why heaps are cheaper than sorting
when you only need the extremes.

For a from-scratch implementation of all this (sift-up, sift-down, bottom-up
heapify, arbitrary remove), see **`max_heap.py`** in this folder.

---

## 2. Python's `heapq` — a MIN-heap on a plain list

Python's standard library gives you heap operations via `heapq`, which works
**directly on a regular `list`** and is **min-heap only** — there is no
`reverse=True` and no max-heap flag.

```python
import heapq
h = []
heapq.heappush(h, 3)        # h is now a valid min-heap
heapq.heappop(h)            # always removes/returns the SMALLEST
h[0]                        # peek the minimum, O(1)
```

### Max-heap via negation

Since `heapq` is min-only, get a max-heap by **negating on the way in and out**:

```python
heapq.heappush(h, -x)       # store the negative
largest = -heapq.heappop(h) # negate back -> the real maximum
```

(For tuples, negate the priority field: `(-priority, item)`.) See
`max_heap_via_negation` in `fundamentals.py`. Negation round-trips exactly even
for negative inputs (`edge_cases.py`).

### Priority queue via tuples + a counter

Push `(priority, item)` — tuples compare lexicographically, so the smallest
priority pops first. But on a **tie**, Python compares the *next* field (the
payload); if the payload is unorderable (a dict, or objects without `__lt__`),
that raises `TypeError`. The fix is the **stability counter idiom**:

```python
import itertools
counter = itertools.count()                 # unique, increasing
heapq.heappush(pq, (priority, next(counter), item))
```

The counter is unique, so it breaks every tie before the payload is reached, and
it preserves FIFO order among equal priorities (a *stable* PQ). This is the
single most important heap idiom — see `stable_priority_queue` in
`fundamentals.py` and the crash it prevents in `gotchas()`.

---

## 3. Operation complexity (memorize this table)

| Operation | `heapq` call | Time | Notes |
|-----------|--------------|------|-------|
| Peek min | `heap[0]` | **O(1)** | the root |
| Push | `heapq.heappush(h, x)` | **O(log n)** | sift the new leaf up |
| Pop min | `heapq.heappop(h)` | **O(log n)** | move last leaf to root, sift down |
| Push then pop | `heapq.heappushpop(h, x)` | O(log n) | one sift, not two |
| Pop then push | `heapq.heapreplace(h, x)` | O(log n) | heap must be non-empty |
| Build heap | `heapq.heapify(h)` | **O(n)** | bottom-up — NOT O(n log n)! |
| Top-k largest | `heapq.nlargest(k, it)` | O(n log k) | beats sort when k ≪ n |
| Top-k smallest | `heapq.nsmallest(k, it)` | O(n log k) | |
| Merge sorted | `heapq.merge(*its)` | O(N log k) | lazy iterator over N items, k inputs |
| Build by n pushes | n × `heappush` | O(n log n) | use `heapify` instead if you have the list |

**Space:** a heap of n items is O(n). The size-k heap patterns
(`heap_tricks.py`) use only **O(k)** extra space regardless of n — that's their
whole point.

> Want the *reasoning* behind these numbers (why push/pop are O(log n), and
> crucially why `heapify` is O(n) not O(n log n))? See **`COMPLEXITY.md`** — it
> derives each bound, including the sum-of-heights argument for heapify.

---

## 4. Edge-case checklist (run through this for EVERY heap problem)

Before coding, ask / handle:

- [ ] **Empty heap pop** — `heappop([])` raises `IndexError`, not a sentinel. Guard `if heap:`.
- [ ] **k > n** — don't pop k times blindly; `nlargest` clamps k, a manual loop crashes.
- [ ] **k == 0** — "top zero" should return `[]`/`None`, not all or a crash.
- [ ] **k < 0** — reject or treat as 0; never feed it to a range.
- [ ] **Duplicates** — heaps emit every duplicate; they are NOT set/dedup operations.
- [ ] **Tie-breaking on equal priority** — add a `count()` tiebreaker so an unorderable payload never gets compared (else `TypeError`).
- [ ] **Single element** — peek/pop/`heapreplace` boundary; `heapreplace` needs non-empty.
- [ ] **Negatives in a max-heap-via-negation** — double negation must round-trip exactly.
- [ ] **heap[0] vs sorted** — only the root is ordered; never read `heap[1:]` expecting sorted order.
- [ ] **Mutation** — `heapify`/`heappush` reorder the caller's list IN PLACE; copy first if it must be preserved.
- [ ] **Stale/lazy deletion** — `heapq` has no decrease-key/remove; the common trick is to push a new entry and skip outdated ones on pop.

### Clarifying questions to ask the interviewer
- Do you want the k largest/smallest, or just the k-th? Any order, or sorted?
- Stream or full array up front? (Stream → can't sort, heap shines.)
- How big is k relative to n? (k ≪ n → size-k heap; k ≈ n → just sort.)
- Are priorities unique, or can they tie? What's the tiebreak rule?
- Is the data already (partially) sorted? (Merge-k applies.)

---

## 5. Pattern index (see `heap_tricks.py`)

| Pattern | When to reach for it | Typical complexity |
|---------|----------------------|--------------------|
| **K-th largest** | k-th biggest/smallest without full sort | O(n log k) time, O(k) space |
| **Top-k frequent** | k most common items (count → size-k heap by freq) | O(n log k) |
| **Merge k sorted** | combine k sorted lists/streams into one | O(N log k) |
| **Two heaps (running median)** | median / balance point of a stream | O(log n) per insert, O(1) query |
| **K closest points** | k nearest by distance/score (size-k max-heap) | O(n log k) |
| **Greedy max-heap (reorganize / scheduling)** | repeatedly take the current max under a constraint | O(n log a) |
| **Repeated extremes (last stone)** | repeatedly combine the two largest/smallest | O(n log n) |

---

## 6. Decision guide — "heap vs sort vs bucket?"

```
Do you need ALL elements in order?
├── Yes → just sort (O(n log n)); a heap gives no advantage here.
└── No — only the extremes / top-k / a streaming order?
    ├── Streaming data (can't see it all at once)?
    │      → heap: running median (two heaps), k-th largest (size-k heap)
    ├── Want top-k and k ≪ n?
    │      → size-k heap / nlargest / nsmallest  (O(n log k) beats O(n log n))
    ├── Want top-k and k ≈ n?
    │      → just sort; the heap's edge has vanished.
    ├── Merging k already-sorted sequences?
    │      → heap of one front element per list (heapq.merge)
    ├── Frequencies/scores are small bounded integers (e.g. 0..n)?
    │      → BUCKET sort / counting can be O(n), beating the heap's log factor
    └── Repeatedly need "the current largest/smallest" as data changes?
           → heap (that's its core job)
```

Rule of thumb: **a heap is the answer when you need the best few — now and as
data arrives — but not a full ordering.** If k is tiny and bounded, or values
are small bounded integers, a bucket/counting approach can beat the log factor.

---

## 7. Python idioms worth knowing (interview-friendly)

```python
import heapq, itertools
heapq.heapify(a)                     # list -> min-heap IN PLACE, O(n)
heapq.heappush(h, x)                 # insert, O(log n)
heapq.heappop(h)                     # remove & return min, O(log n)
h[0]                                 # peek min, O(1)
heapq.heappushpop(h, x)              # push then pop-min, one sift
heapq.heapreplace(h, x)             # pop-min then push, one sift (h non-empty)
heapq.nlargest(k, it, key=fn)        # top-k by key, O(n log k)
heapq.nsmallest(k, it, key=fn)       # bottom-k by key
list(heapq.merge(a, b, c))           # merge sorted iterables, lazy

# max-heap via negation
heapq.heappush(h, -x); top = -heapq.heappop(h)

# stable priority queue (counter breaks ties; protects unorderable payloads)
counter = itertools.count()
heapq.heappush(pq, (priority, next(counter), item))

# two-heaps median: low = max-heap (negated), high = min-heap
```

See `fundamentals.py` for the full, runnable list of operations and gotchas, and
`max_heap.py` for the underlying mechanics done by hand.
