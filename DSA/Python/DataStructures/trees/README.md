# Binary Trees & BSTs — Complete Interview Prep Guide

A single place to revise everything about binary trees and binary search trees in
Python for coding interviews: how they're structured, what every operation costs,
the edge cases that break solutions, and the core patterns with runnable, tested
code.

> All `.py` files here are **runnable and self-testing**. Run any of them
> directly (`python3 fundamentals.py`) — they execute `assert`-based tests and
> print a short confirmation. If a file runs without raising, every example passed.

---

## Files in this folder

| File | What it covers |
|------|----------------|
| `fundamentals.py` | `TreeNode`, build-from-level-order, all traversals (recursive + iterative), BFS, height/count, BST insert/search/delete/validate, gotchas |
| `tree_tricks.py`  | The 9 core tree patterns, each runnable with inline `assert` tests |
| `edge_cases.py`   | A concrete, runnable edge-case checklist (empty/single/skewed/dup/balance/BST-boundary) |
| `COMPLEXITY.md`   | The *why* behind every Big-O here — the reasoning/trick that derives it |
| `README.md`       | This guide — fundamentals, complexity tables, checklists, pattern index |

---

## 1. What is a binary tree (and a BST)?

A **binary tree** is a set of **nodes**; each node holds a value and up to two
child pointers, `left` and `right`. A missing child is `None`. One node is the
**root** (no parent); nodes with no children are **leaves**.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

A **binary search tree (BST)** adds an **ordering invariant**: for *every* node,
all values in its **left** subtree are smaller and all values in its **right**
subtree are larger. That invariant is what makes search/insert/delete `O(h)` and
makes an **inorder** traversal emit values in **sorted order**.

> Key subtlety: the invariant is about the **whole subtree**, not just the
> immediate parent. A node deep in a left subtree can be larger than its parent
> yet still violate an ancestor's bound. Validation must carry a **range**, not do
> a parent comparison (see `validate_bst` and `edge_cases.py`).

### Terminology (memorize)

| Term | Meaning |
|------|---------|
| **height** of a node | edges on the longest path *down* to a leaf (a leaf has height 0) |
| **depth** of a node | edges from the root *down* to that node (root has depth 0) |
| **h** | height of the tree — `O(log n)` if balanced, `O(n)` if skewed |
| **leaf** | node with no children |
| **balanced** | every node's left/right subtree heights differ by ≤ 1 (height ≈ `log n`) |
| **complete** | every level full except possibly the last, which fills left-to-right |
| **full** | every node has either 0 or 2 children (never exactly 1) |
| **perfect** | full *and* all leaves at the same depth (`2^(h+1) - 1` nodes) |
| **skewed / degenerate** | every node has one child — effectively a linked list (`h = n-1`) |

> Note: "height in edges" vs "height in nodes" both appear in problems. This
> folder uses **edges** in `fundamentals.height()` (empty `-1`, leaf `0`) and
> **nodes** in `tree_tricks.max_depth()` (empty `0`, leaf `1`). Diameter is
> measured in **edges**. Always confirm which the problem means.

---

## 2. Operation complexity (memorize this table)

`n` = number of nodes, `h` = height, `w` = maximum width (widest level).

| Operation | Time | Space (extra) | Notes |
|-----------|------|---------------|-------|
| Traversal (pre/in/post-order) | O(n) | O(h) | each node visited once; recursion/stack = height |
| Level-order (BFS) | O(n) | O(w) | queue holds at most one full level |
| Morris inorder | O(n) | **O(1)** | threading trick — reuses null right pointers |
| Height / count nodes | O(n) | O(h) | must touch every node |
| BST search | O(h) | O(1) iter / O(h) rec | `O(log n)` balanced, `O(n)` skewed |
| BST insert | O(h) | O(h) | same shape dependence |
| BST delete | O(h) | O(h) | two-child case uses inorder successor |
| Validate BST | O(n) | O(h) | range check, not parent-only |
| Build from level-order | O(n) | O(n) | one BFS pass |
| Serialize / deserialize | O(n) | O(n) | preorder + null markers |

**The whole story is `h`.** Balanced → `h = O(log n)`, so BST ops are `O(log n)`.
Skewed → `h = O(n)`, so they degrade to `O(n)` (a linked list). Self-balancing
trees (AVL / red-black) guarantee `O(log n)` by keeping `h` small; plain BSTs do
not.

> Want the *reasoning* behind these numbers (why traversal is O(n), why recursion
> space is O(h), why Morris is O(1))? See **`COMPLEXITY.md`** — it derives each
> bound from the trick that produces it.

---

## 3. Edge-case checklist (run through this for EVERY tree problem)

Before coding, ask / handle:

- [ ] **Empty tree** `root is None` — does your recursion/BFS guard `None` BEFORE
      touching `node.val` / `node.left`? It will crash otherwise.
- [ ] **Single node** — it's a leaf *and* the root; leaf-based logic (path sum,
      leaf count) must handle "no children" correctly.
- [ ] **Completely skewed tree** (degenerate linked list) — `h == n`, so deep
      recursion can hit Python's recursion limit (~1000). Consider iterative.
- [ ] **Two nodes** — smallest case with a parent/child relationship.
- [ ] **Duplicate values** — compare nodes by **identity** (`is`), not value;
      decide a **BST duplicate convention** (reject / count / send one side).
- [ ] **Unbalanced vs balanced** — affects whether your `O(h)` is `O(log n)` or
      `O(n)`; calling `height()` at every node is a hidden `O(n²)`.
- [ ] **BST range boundary** — validate against an inherited `(low, high)` range,
      NOT just the parent. Watch `<` vs `<=` for the duplicate convention.
- [ ] **Negative values** — break "init to 0" path-sum logic; never prune early
      assuming sums grow.
- [ ] **Not found / no valid path** — return a clear sentinel (`None`, `-1`, `False`).
- [ ] **Mutation allowed?** — may you rewire pointers (invert, flatten) or must
      you build a new tree?

### Clarifying questions to ask the interviewer
- Is it a BST or a general binary tree? Are values distinct or can they repeat?
- Height measured in nodes or edges? Is the tree guaranteed balanced?
- Can I mutate the tree / rewire pointers, or must the input be preserved?
- What do I return for an empty tree / when no path or node exists?
- For LCA: are both nodes guaranteed present? Do I have parent pointers?

---

## 4. Pattern index (see `tree_tricks.py`)

| Pattern | When to reach for it | Typical complexity |
|---------|----------------------|--------------------|
| **Max depth / height** | any "how tall" question; base for many others | O(n), O(h) |
| **Diameter** | longest path between two nodes (may skip root) | O(n), O(h) |
| **Invert / mirror** | reflect a tree; symmetry checks | O(n), O(h) |
| **Is-balanced** | height-balance check in ONE pass (avoid O(n²)) | O(n), O(h) |
| **LCA (binary tree)** | lowest common ancestor, no ordering | O(n), O(h) |
| **LCA (BST)** | LCA when ordering lets you walk down directly | O(h), O(1) |
| **Path sum I** | exact root-to-leaf sum exists? | O(n), O(h) |
| **Path sum III** | count any downward path summing to k (prefix-sum map) | O(n), O(h) |
| **Serialize / deserialize** | persist / reconstruct exact shape | O(n), O(n) |
| **Build from preorder+inorder** | reconstruct from two traversals | O(n), O(n) |
| **Morris inorder** | inorder in O(1) extra space (threading) | O(n), O(1) |

---

## 5. Decision guide — "which approach?"

```
Is it a BST (ordered)?
├── Yes → the ordering is a free comparator
│        ├── search / insert / delete / LCA  → walk down, O(h), often O(1) space
│        ├── kth smallest / sorted output     → INORDER traversal (yields sorted)
│        └── validate                          → carry a (low, high) range
└── No (general binary tree)
    │
    Do you process LEVEL BY LEVEL (widths, right-side view, zigzag, min depth)?
    ├── Yes → BFS with a deque (level-order)         → O(n) time, O(w) space
    └── No  → DFS recursion
             ├── need a value bubbled UP (height, balance, diameter, LCA, path sum)
             │      → post-order style: combine children's results
             ├── need state threaded DOWN a path (path sum III, root-to-leaf)
             │      → pass accumulator + backtrack (decrement) on the way up
             └── need O(1) extra space for inorder → Morris threading
```

**DFS vs BFS quick rule:** BFS when the answer is organized by level or you want
the *shallowest* result (e.g. minimum depth, nearest node). DFS for everything
that combines subtree results or follows root-to-leaf paths. **BST property
helps** whenever you can decide "go left or go right" from a comparison — that
turns an `O(n)` search into `O(h)`.

---

## 6. Python idioms worth knowing (interview-friendly)

```python
# --- The recursion template: base case for None, recurse, combine ---
def solve(node):
    if not node:
        return BASE            # 0, -1, None, True ... pick the identity value
    left = solve(node.left)
    right = solve(node.right)
    return combine(node, left, right)

# --- Level-order (BFS) with a deque: snapshot the level size each pass ---
from collections import deque
def level_order(root):
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):        # exactly the nodes on this level
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        out.append(level)
    return out

# --- Iterative inorder (left-dive stack) when recursion depth is a risk ---
def inorder(root):
    out, stack, cur = [], [], root
    while stack or cur:
        while cur:
            stack.append(cur); cur = cur.left
        cur = stack.pop(); out.append(cur.val); cur = cur.right
    return out

# --- "Return a value up + track a global" (diameter, max path sum) ---
best = 0
def dfs(node):
    nonlocal best
    ...                        # update best with the path THROUGH node
    return height_or_gain      # return what the PARENT can use

float('inf'), float('-inf')    # safe (low, high) bounds for BST validation
```

See `fundamentals.py` for the full, runnable set of operations and gotchas, and
`tree_tricks.py` for each pattern implemented and tested.
