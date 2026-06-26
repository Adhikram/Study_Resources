# Complexity — the *why* behind the Big-O

The number (`O(log n)`, `O(n)`, ...) is the answer. This file is the **reasoning
trick** that produces it — the mental model that lets you derive the complexity
in an interview instead of memorizing it. Each entry names the trick, then
proves it.

The single idea behind almost every heap bound is **tree height**. A binary heap
is a *complete* binary tree on n nodes, so its height is `⌊log₂ n⌋ = O(log n)`.
Anything that walks one root-to-leaf path is therefore O(log n); anything O(1) is
just touching the root. The one surprising result — `heapify` being O(n) — comes
from a **sum-of-heights** argument that we derive in full below.

---

## 1. Peek-min is O(1) — it's literally the root

The heap property says every parent `<=` its children. Apply it transitively
from the root down and the **global minimum must sit at index 0**. Reading
`heap[0]` is a single array access → **O(1)**. No search, no traversal. (For a
max-heap-via-negation, the max is likewise at index 0 of the negated array.)

---

## 2. `heappush` is O(log n) — sift UP one path, height = log n

A push appends the new value as the last leaf (amortized O(1) array append),
then **sifts it up**: compare with its parent, swap if it violates the heap
property, repeat. Each swap moves the element up **one level**.

**Trick — the number of levels is the tree height.** A complete tree on n nodes
has height `⌊log₂ n⌋`, so the element can rise at most `log n` times. Each
comparison/swap is O(1) → **O(log n) worst case.** The element stops early the
moment its parent is already smaller, so many pushes are faster, but the bound is
the path length.

---

## 3. `heappop` is O(log n) — sift DOWN one path, height = log n

You can't just remove the root and leave a hole. Instead: move the **last leaf
into the root**, shrink the array, then **sift down** — repeatedly swap the new
root with its *smaller* child until the heap property holds again. Each swap
descends **one level**.

**Same trick:** the descent is bounded by the tree height → at most `log n`
swaps, each O(1) → **O(log n).** `heapreplace` and `heappushpop` are also O(log n)
because they do exactly **one** sift-down (they fuse the push and pop so the
element is never appended-then-bubbled twice).

---

## 4. `heapify` is O(n) — NOT O(n log n) — the sum-of-heights argument

This is the result interviewers love, because the naive guess is wrong.

**The naive (wrong) guess.** "Building a heap means inserting n elements, each
push is O(log n), so it's O(n log n)." That bound is correct *for building by n
pushes* (see §5) — but `heapq.heapify` does **not** do that.

**What heapify actually does — bottom-up sift-down.** Start at the **last
non-leaf node** (index `n//2 - 1`) and sift *down* at every node, moving toward
the root:

```
for i in range(n // 2 - 1, -1, -1):
    sift_down(i)
```

The cost of `sift_down` at a node is bounded by that node's **height** (distance
to the deepest leaf below it), not by `log n`. And here's the key fact:

> **Most nodes are near the bottom, where height is tiny.**

In a complete tree of height `h ≈ log n`:

- there are `~n/2` leaves at **height 0** (sift_down does nothing),
- `~n/4` nodes at **height 1**,
- `~n/8` nodes at **height 2**,
- ... and only **1** node (the root) at **height h**.

The total work is the sum of (number of nodes at a height) × (that height):

```
total  ≈  Σ over heights k=0..h   (n / 2^(k+1)) · k
       =  (n/2) · Σ_{k=0}^{∞}  k / 2^k
```

The series `Σ k / 2^k` **converges to a constant (= 2)** — it does not grow with
n. So:

```
total  ≈  (n/2) · 2  =  n   →  O(n)
```

**Trick in one sentence:** the expensive sift-downs (near the root) are *rare*,
and the *many* cheap ones (near the leaves) cost almost nothing, so the weighted
sum collapses to a constant times n. The geometric decay in node count beats the
linear growth in height.

---

## 5. Building by n pushes is O(n log n) — contrast with heapify

If instead you start empty and call `heappush` n times, each push is O(log
(current size)). Summing over the n inserts:

```
Σ_{i=1}^{n} log i  =  log(n!)  ≈  n log n   (Stirling)
```

→ **O(n log n) total.** The difference from §4 is *direction*: pushes sift
**up** from leaves (where the tree is widest, so most elements travel a long
way), while heapify sifts **down** from internal nodes (where the half that are
leaves travel zero distance). **Takeaway: if you already have the whole list,
`heapify` it (O(n)); only build incrementally when elements arrive over time.**

---

## 6. `nlargest`/`nsmallest`(k) is O(n log k) — a size-k heap, not a size-n sort

To get the k largest of n, keep a **size-k min-heap of the largest seen so far**:
push each element, and whenever the heap exceeds k, pop the smallest. The heap
never grows past k, so every push/pop costs `O(log k)`, done n times →
**O(n log k).**

**Trick — bound the heap size, not the input.** When `k ≪ n`, `n log k` beats
sorting everything (`n log n`), and uses only **O(k)** space. When `k ≈ n`,
there's no win — just sort. (`heapq` switches to a plain sort internally when k
is close to n.)

---

## 7. Two-heaps running median — O(log n) per insert, O(1) query

Maintain two heaps: a **max-heap** `low` for the smaller half and a **min-heap**
`high` for the larger half, kept balanced (`|len(low) - len(high)| <= 1`) with
`low` holding the extra element on odd counts.

- **Insert:** one push, then one rebalancing push/pop between the heaps — a
  constant number of O(log n) heap operations → **O(log n) per insert.**
- **Query:** the median is either the root of `low` (odd) or the average of the
  two roots (even) — both are `heap[0]` reads → **O(1).**

**Trick — split the data at the median so the answer is always at a root.** A
single sorted structure would cost O(n) to insert into; two heaps turn "find the
middle" into "read two roots," paying only the O(log n) to keep the halves
balanced. See `MedianFinder` in `heap_tricks.py`.

---

## Cheat-sheet: which trick gives which bound

| Bound | Trick that produces it |
|-------|------------------------|
| O(1) peek | the min/max is the root, index 0 — a single read |
| O(log n) push | sift **up** one path; path length = tree height = log n |
| O(log n) pop / replace | sift **down** one path; height = log n; replace fuses into one sift |
| **O(n) heapify** | bottom-up sift-down; Σ (nodes at height k)·k converges to a constant × n |
| O(n log n) build-by-pushes | n pushes, Σ log i = log(n!) ≈ n log n (contrast with heapify) |
| O(n log k) top-k | bound the **heap** to size k, not the input → log k per op, k space |
| O(log n) median insert | two balanced heaps; answer lives at the roots (O(1) read) |
