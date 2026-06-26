# Complexity — the *why* behind the Big-O

The number (`O(n)`, `O(h)`, `O(log n)`, ...) is the answer. This file is the
**reasoning trick** that produces it — the mental model that lets you derive the
complexity in an interview instead of memorizing it. Each entry names the trick,
then proves it.

For trees, almost everything reduces to two quantities:

1. **`n` — total nodes.** Anything that must *look at every node* is `O(n)`. You
   can't do better than `O(n)` if the answer depends on all values.
2. **`h` — height.** Anything bounded by a single root-to-leaf path (a search,
   the recursion call stack) is `O(h)`. The entire balanced-vs-skewed story is
   just `h = O(log n)` vs `h = O(n)`.

If you can decide "does this touch all nodes, or follow one path?" you can derive
the bound yourself.

---

## 1. Traversal is O(n) — each node is visited exactly once

Pre/in/post-order and BFS all **visit every node once and do O(1) work per
visit** (append a value, push/pop children). n visits × O(1) = **O(n) time.**

There's no double counting: a node is reached from its unique parent and handed
off to its two children — the recursion/queue forms a walk that enters each node
once and leaves it once. That "once per node" is why *every* full traversal,
regardless of order, is `O(n)` and you cannot beat it when the task needs all
values (e.g. summing, height, validation).

---

## 2. Recursion space is O(h) — the call stack equals the current path depth

A DFS recursion only has **one active root-to-leaf path on the stack at a time**.
When you recurse into `node.left`, that frame stays until the whole left subtree
finishes — but you are never deeper than the length of the path from the root to
the node you're currently at.

So the maximum number of stacked frames = the **deepest path = the height h** →
**O(h) space.**

- **Balanced tree:** `h = O(log n)` → `O(log n)` stack. Cheap.
- **Skewed tree (linked list):** `h = n-1` → **O(n) stack.** This is exactly why a
  2000-node skewed tree throws `RecursionError` in Python (default limit ~1000) —
  see `edge_cases.py`. The fix is an **explicit stack on the heap** (iterative
  traversal): same `O(h)` asymptotics, but heap space is far larger than the call
  stack, so it survives.

> Iterative traversals don't *improve* the `O(h)` bound — they move it from the
> fragile call stack to the roomy heap.

---

## 3. BST search / insert / delete is O(h) — each comparison drops a whole subtree

In a BST, one comparison at a node tells you the target is **smaller (go left)**
or **larger (go right)** — so you discard the **entire other subtree** and never
look back. The work is a single descent from root toward a leaf → **O(h).**

How balance changes it:

```
balanced:  h ≈ log₂(n)   → search/insert/delete = O(log n)
skewed:    h = n - 1     → search/insert/delete = O(n)   (degrades to a list scan)
```

This is the same "halve the search space" idea as binary search — **but only if
the tree is balanced.** A plain BST gives no balance guarantee; inserting sorted
data builds a fully skewed `O(n)` tree. Self-balancing variants (AVL, red-black)
do rotations to keep `h = O(log n)`, which is what *guarantees* the `O(log n)`.

- **Delete's two-child case** still fits in `O(h)`: replace the value with the
  **inorder successor** (leftmost node of the right subtree — one more descent),
  then delete that successor (a leaf or one-child node). One extra path traversal,
  still `O(h)`.
- **Search is O(1) space** done iteratively (a moving pointer, no stack);
  recursive insert/delete are `O(h)` space for the call stack.

---

## 4. `validate_bst` is O(n), and why parent-only comparison is WRONG

Validation must touch every node (`O(n)`), carrying an **open range `(low,
high)`** that tightens on the way down: going left replaces the high bound with
the current value, going right replaces the low bound.

The trick is realizing the invariant is about the **whole subtree, not the
parent**. A naive "left child < node < right child" check passes trees like:

```
      5
       \
        7
       /
      4        # 4 < 5, but it sits in 5's RIGHT subtree -> invalid
```

The parent check (`4 < 7`) is satisfied, so the bug accepts it. The range check
inherits `low = 5` from the right-turn at the root, and `4 < 5` fails it
correctly. One pass, `O(1)` work per node → **O(n) time, O(h) recursion space.**

---

## 5. Morris inorder is O(1) space — the threading trick

Recursive/iterative inorder need `O(h)` space for the stack. **Morris traversal
removes the stack entirely** by reusing the tree's own **null right pointers** as
temporary "threads" back to the ancestor you'd otherwise have remembered.

For each node with a left child, find its **inorder predecessor** (the rightmost
node of the left subtree). That predecessor's `right` pointer is null (it's the
rightmost) — free scratch space. **Point it back at the current node** (the
thread), then walk left. When you later arrive back via that thread, you know the
left subtree is done: visit the node, **undo the thread** (restore null), and go
right.

- Each edge is traversed at most a constant number of times (down, via thread,
  and to remove the thread), so despite the inner "find predecessor" loop the
  total work is still **O(n)** (an aggregate/charging argument — the predecessor
  walks across the whole tree sum to `O(n)`, not `O(n)` each).
- No stack, no recursion, only O(1) pointers held at once → **O(1) extra space.**
- Caveat: it **temporarily mutates** the tree. Threads are always removed before
  the traversal returns, so the tree is restored — but it's not safe under
  concurrent reads, and you must mention the mutation when asked for "read-only."

---

## 6. Level-order space is O(w) — the queue holds at most one level

BFS keeps a queue of nodes "discovered but not yet processed." If you snapshot the
queue size at the top of each level (`for _ in range(len(q))`), the queue never
holds more than **one level's worth plus the next**, so its peak size is the
**maximum width `w`** of the tree → **O(w) space.**

How `w` relates to `n`:

- A **balanced/complete** tree's last level holds up to `n/2` nodes → `w =
  O(n)`. So BFS is `O(n)` space in the worst case — *wider* trees cost more.
- A **skewed** tree has width 1 at every level → `w = 1`, BFS is `O(1)` space,
  whereas its DFS recursion is `O(n)`.

That's the trade-off: **DFS space scales with height, BFS space scales with
width.** Pick the traversal whose "bad" dimension your tree doesn't have.

---

## Cheat-sheet: which trick gives which bound

| Bound | Trick that produces it |
|-------|------------------------|
| O(n) time (any full traversal) | each node visited exactly once, O(1) work per visit |
| O(h) recursion / search space | only one root-to-leaf path is active at a time |
| O(log n) | balanced ⇒ `h = log n`; each comparison drops a whole subtree |
| O(n) (degraded) | skewed ⇒ `h = n`; the BST is effectively a linked list |
| O(1) space inorder | Morris threading reuses null right pointers instead of a stack |
| O(w) space | BFS queue holds at most the widest level (one-level-at-a-time) |
| correct BST validation | inherit a (low, high) range, not a parent-only comparison |
| O(h) BST delete (2 children) | swap in the inorder successor, then delete it (one more descent) |
