# Linked Lists — Complete Interview Prep Guide

A single place to revise everything about linked lists in Python for coding
interviews: how they work, what every operation costs, the edge cases that
break solutions, and the core patterns with runnable, tested code.

> All `.py` files here are **runnable and self-testing**. Run any of them
> directly (`python3 fundamentals.py`) — they execute `assert`-based tests and
> print a short demo. If a file runs without raising, every example passed.

---

## Files in this folder

| File | What it covers |
|------|----------------|
| `fundamentals.py` | A real `Node` + `LinkedList` (insert/delete/search/reverse), every op + its Big-O, gotchas |
| `linked_list_tricks.py` | The 9 core linked-list patterns, each runnable with inline `assert` tests |
| `edge_cases.py`   | A concrete, runnable edge-case checklist (empty/single/two/cycle/even-odd/head-tail/dummy) |
| `COMPLEXITY.md`   | The *why* behind every Big-O here — the reasoning/trick that derives it |
| `README.md`       | This guide — fundamentals, complexity tables, checklists, pattern index |

---

## 1. What is a linked list?

A **linked list** is a chain of **nodes**. Each node holds a value and a pointer
(`next`) to the following node; the last node points to `None`. You hold only the
**head**; everything else is reached by walking pointers.

The defining contrast with an array is **no contiguity and no index**:

- An array stores elements in one contiguous block, so `a[k]` is O(1) pointer
  arithmetic.
- A linked list scatters nodes anywhere in memory, joined only by pointers, so
  reaching the k-th node means **walking k hops from the head → O(n)**.

That single property flips the trade-offs: linked lists are **slow to index but
cheap to splice**. Inserting or deleting at a node you already hold is O(1) — you
just rewire two pointers, no shifting — whereas the same operation in an array is
O(n) because everything after the gap must shift.

### Flavours

- **Singly linked** — node has `next` only. Forward traversal. Lowest memory.
  (`fundamentals.py` implements this.)
- **Doubly linked** — node has `next` *and* `prev`. O(1) delete given the node,
  O(1) at both ends, backward traversal. Costs one extra pointer per node.
- **Circular** — the tail's `next` points back into the list instead of `None`.
  The basis of cycle problems.

### vs Python `list` and `collections.deque`

In real Python you almost never hand-roll a linked list — you use:

- **`list`** — a dynamic array. O(1) index, O(1) amortized append, but O(n)
  insert/pop at the front.
- **`collections.deque`** — a **doubly linked list** (of blocks) under the hood.
  It gives you the linked-list superpower in practice: **O(1) `append`,
  `appendleft`, `pop`, and `popleft`**. Indexing into the middle is O(n).

Interviews that say "implement/manipulate a linked list" want the node-based
version (`fundamentals.py`). Interviews that just need a queue/stack with O(1)
ends want `deque`. Know both.

---

## 2. Operation complexity (memorize this table)

For a singly linked list holding the **head** pointer:

| Operation | Time | Notes |
|-----------|------|-------|
| Access / get k-th node | **O(n)** | no random access — walk from head |
| Search by value | O(n) | walk until match |
| Insert at head | **O(1)** | the whole point — rewire one pointer |
| Insert at tail | O(n) | must walk to the end (**O(1)** if a `tail` pointer is cached) |
| Insert/delete at a **known** node (you hold its predecessor) | **O(1)** | rewire pointers, no shifting |
| Delete by value | O(n) | O(n) to find + O(1) to unlink |
| Reverse | O(n) time, **O(1) space** | iterative pointer flip |
| Length | O(n), or O(1) | O(1) only if size is cached on every insert/delete |

**`collections.deque` (practical linked list):**

| Operation | Time |
|-----------|------|
| `append` / `appendleft` | O(1) |
| `pop` / `popleft` | O(1) |
| Index in the middle `d[i]` | O(n) |
| Membership `x in d` | O(n) |

**Space:** a list of n nodes is O(n) (and uses more than an array of n values —
each node carries its pointer(s) plus object overhead). Reversal and fast/slow
traversal are **O(1) extra**; recursive reversal is **O(n)** for the call stack.

> Want the *reasoning* behind these numbers (why index is O(n), why Floyd's
> tortoise & hare meet, why reversal is O(1) space)? See **`COMPLEXITY.md`** — it
> derives each bound from the trick that produces it.

---

## 3. Edge-case checklist (run through this for EVERY linked-list problem)

Before coding, ask / handle:

- [ ] **Empty list** (`head is None`) — does your code read `head.val` /
      `head.next` blindly? It will raise `AttributeError`.
- [ ] **Single node** — `head.next is None`; fast/slow and reverse loops may not
      enter. Often the trivial / already-correct answer.
- [ ] **Two nodes** — smallest case where pointers actually move; off-by-one
      central for reverse, swap, middle.
- [ ] **Cycle present** — a "walk to `None`" loop runs **forever**. Use Floyd's
      two pointers; never length-count a possibly-cyclic list.
- [ ] **Even vs odd length** — fast/slow returns the 1st *or* 2nd middle; know
      which your problem needs.
- [ ] **Deleting the head** — the head has no predecessor → use a **dummy node**.
- [ ] **Deleting the tail** — the new tail's `next` must become `None`.
- [ ] **Result head differs from input head** (merge, delete-head, remove-Nth
      where N is the head) — **dummy node** removes the special case.
- [ ] **Don't lose the rest of the list** — stash `node.next` *before*
      overwriting it.
- [ ] **Don't advance past the unlink point** — when deleting matches, stay on
      `prev` because the next node may also match.
- [ ] **Identity vs value** — cycle/intersection compare nodes with `is`, not
      `==`.
- [ ] **Mutation allowed?** — many tricks rewire the list in place; may you?

### Clarifying questions to ask the interviewer
- Singly or doubly linked? Is there a `tail` pointer? Is the size known/cached?
- Can the list contain a cycle? Can I mutate it in place, or must I preserve it?
- 0-indexed or 1-indexed for "k-th" / "Nth from end"? What to return when absent?
- For even length, which node counts as the "middle"?

---

## 4. Pattern index (see `linked_list_tricks.py`)

| Pattern | When to reach for it | Typical complexity |
|---------|----------------------|--------------------|
| **Iterative reverse** | reverse all/part, or as a sub-step (palindrome, reorder) | O(n) time, O(1) space |
| **Recursive reverse** | when recursion reads cleaner; mind the stack | O(n) time, O(n) stack |
| **Fast / slow pointers** | find the middle, split a list, nth-from-half | O(n), O(1) |
| **Floyd's cycle detection** | detect a loop and/or find where it starts | O(n), O(1) |
| **Merge two sorted lists** | merge step of merge-sort, combine sorted streams | O(n+m), O(1) |
| **Two-pointer gap** | remove/return the Nth node from the end in one pass | O(n), O(1) |
| **Length-diff / switch walkers** | intersection (shared tail) of two lists | O(n+m), O(1) |
| **Reverse-second-half** | palindrome check / reorder in O(1) space | O(n), O(1) |
| **Split + reverse + interleave** | reorder list L0→Ln→L1→Ln-1→… | O(n), O(1) |
| **Dummy (sentinel) node** | any op where the head might change or be deleted | O(n), O(1) |

---

## 5. Decision guide — "which pattern?"

```
Is there (or could there be) a cycle?
├── Yes / unknown → Floyd's tortoise & hare (detect, then find start)
└── No
    ├── Need the middle / to split the list?        → fast & slow pointers
    ├── Need the Nth node from the END?             → two-pointer gap of N
    ├── Reversing all or part of it?                → iterative reverse (O(1) space)
    ├── Combining two SORTED lists?                 → merge with a dummy node
    ├── Comparing two lists for a shared tail?      → switch-walkers intersection
    ├── Palindrome / reorder in O(1) space?         → reverse the second half
    └── Head might change or be deleted?            → add a dummy/sentinel node
```

---

## 6. Python idioms worth knowing (interview-friendly)

The **practical** linked list in Python is `collections.deque` — reach for it
whenever you need O(1) ends:

```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)        # O(1) push right        -> deque([1, 2, 3, 4])
dq.appendleft(0)    # O(1) push left         -> deque([0, 1, 2, 3, 4])
dq.pop()            # O(1) pop right  -> 4
dq.popleft()        # O(1) pop left   -> 0
dq[0], dq[-1]       # O(1) peek ends; middle index is O(n)
dq = deque(maxlen=3)             # bounded; oldest drops off automatically
dq.rotate(1)                    # O(k) rotate (sliding-window / round-robin)
dq.extend([5, 6]); dq.extendleft([7])   # bulk push (extendleft reverses order!)
```

For the node-based version (interview "implement a linked list"):

```python
class Node:
    __slots__ = ("val", "next")          # small memory win
    def __init__(self, val, next=None):
        self.val, self.next = val, next

dummy = Node(0, head)                    # sentinel: kills the "delete head" special case
prev, cur, nxt = None, head, None        # the iterative-reverse trio
slow = fast = head                       # the fast/slow pointer pair
while fast and fast.next:                # the universal fast/slow loop guard
    slow, fast = slow.next, fast.next.next
```

See `fundamentals.py` for the full, runnable list of operations and gotchas, and
`COMPLEXITY.md` for the reasoning behind each bound.
