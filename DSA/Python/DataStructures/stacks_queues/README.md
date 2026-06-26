# Stacks & Queues — Complete Interview Prep Guide

A single place to revise everything about stacks (LIFO) and queues (FIFO) in
Python for coding interviews: how they work, what every operation costs, the
edge cases that break solutions, and the core patterns with runnable, tested
code.

> All `.py` files here are **runnable and self-testing**. Run any of them
> directly (`python3 fundamentals.py`) — they execute `assert`-based tests and
> print a short demo. If a file runs without raising, every example passed.

---

## Files in this folder

| File | What it covers |
|------|----------------|
| `fundamentals.py` | Stack via `list`, queue/deque via `collections.deque`, every operation + its Big-O, common gotchas/pitfalls |
| `stack_queue_tricks.py` | The 8 core stack/queue patterns, each runnable with inline `assert` tests |
| `edge_cases.py`   | A concrete, runnable edge-case checklist (empty pop/peek, single element, unbalanced parens, k boundaries, spaces) |
| `COMPLEXITY.md`   | The *why* behind every Big-O here — the reasoning/trick that derives it |
| `README.md`       | This guide — fundamentals, complexity tables, checklists, pattern index |

---

## 1. What are stacks and queues (in Python)?

A **stack** is LIFO — *Last In, First Out*. The last item pushed is the first
popped (think a stack of plates). A **queue** is FIFO — *First In, First Out*.
The first item enqueued is the first dequeued (think a line at a counter).

| Structure | Add | Remove | Python tool |
|-----------|-----|--------|-------------|
| Stack (LIFO) | push = `append()` | pop = `pop()` (from end) | **`list`** |
| Queue (FIFO) | enqueue = `append()` | dequeue = `popleft()` (from front) | **`collections.deque`** |
| Deque (both ends) | `append` / `appendleft` | `pop` / `popleft` | **`collections.deque`** |

### Use a `list` as a stack
`list.append()` and `list.pop()` both operate on the **end** in O(1) amortized —
a list is a perfect stack out of the box.

### Use `collections.deque` as a queue (NOT `list.pop(0)`)
A queue removes from the **front**. On a `list`, `pop(0)` (or `insert(0, x)`)
forces every remaining element to **shift one slot** to stay contiguous —
**O(n)** per operation, a hidden **O(n²)** in a loop. A `deque` is a
doubly-linked list of fixed-size blocks, so `popleft()` / `appendleft()` are
genuine **O(1)**. *Always reach for `deque` when you need front access.*

```python
from collections import deque
q = deque()
q.append(1); q.append(2)   # enqueue   -> O(1)
q.popleft()                # dequeue 1 -> O(1)   (list.pop(0) would be O(n))
```

A `deque` is also a **double-ended queue**: O(1) at both ends, with an optional
`maxlen` that auto-evicts from the far end (handy for fixed sliding windows).
Its one weakness vs a list: **indexing the middle is O(n)**, so use a list when
you need fast arbitrary `a[i]`.

---

## 2. Operation complexity (memorize this table)

| Operation | Stack (`list`) | Queue / Deque (`deque`) | Notes |
|-----------|----------------|--------------------------|-------|
| push / enqueue back | `append(x)` — O(1) amortized | `append(x)` — O(1) | occasional list resize |
| push front | n/a | `appendleft(x)` — O(1) | deque only |
| pop top / pop back | `pop()` — O(1) | `pop()` — O(1) | |
| dequeue front | `pop(0)` — **O(n)** ✗ | `popleft()` — O(1) ✓ | this is the whole reason to use deque |
| peek top / front | `a[-1]` / `a[0]` — O(1) | `dq[-1]` / `dq[0]` — O(1) | raises `IndexError` if empty |
| index middle | `a[i]` — O(1) | `dq[i]` — **O(n)** | deque is linked blocks |
| size | `len(a)` — O(1) | `len(dq)` — O(1) | stored, not counted |
| empty check | `not a` — O(1) | `not dq` — O(1) | |
| rotate | n/a | `dq.rotate(k)` — O(k) | |
| build from iterable | `list(it)` — O(n) | `deque(it)` — O(n) | |

**Space:** a stack/queue of n items is O(n). The amortized patterns below (two
stacks, monotonic stack/deque) all stay O(n) total despite inner loops.

> Want the *reasoning* behind these numbers (why `deque` is O(1) at both ends,
> why a monotonic stack isn't O(n²), why two-stack queue is amortized O(1))?
> See **`COMPLEXITY.md`** — it derives each bound from the trick that produces it.

---

## 3. Edge-case checklist (run through this for EVERY stack/queue problem)

Before coding, ask / handle:

- [ ] **Empty pop / peek** — `pop()`, `popleft()`, `a[-1]`, `a[0]` all raise
      `IndexError` on an empty container. Guard with `if container:` and decide
      the contract (return `None`? raise? sentinel?).
- [ ] **Single element** — push/pop should round-trip; min-stack/queue of one.
- [ ] **Empty input string/array** — `""` parens are valid; empty window is `[]`.
- [ ] **Unbalanced parentheses** — leftover openers (stack non-empty at end),
      lone closer (close on empty stack), wrong order (`([)]`).
- [ ] **Window k boundaries** — `k == 1`, `k == n`, `k > n`, `k <= 0`.
- [ ] **Expression spaces & single number** — skip spaces, flush the LAST
      operand (no trailing operator to trigger it).
- [ ] **Operator precedence** — `*` / `/` bind tighter than `+` / `-`.
- [ ] **Integer division sign** — `int(a / b)` truncates toward zero;
      `a // b` floors (differs on negatives).
- [ ] **Nested structure** — `decode_string("3[a2[c]]")`, nested brackets.
- [ ] **`list.pop(0)` smell** — using a list as a queue is a hidden O(n²).
- [ ] **Monotonic direction** — increasing vs decreasing stack/deque; strict
      vs non-strict comparison decides duplicate handling.

### Clarifying questions to ask the interviewer
- Can the input be empty? What should an empty pop/dequeue return?
- Are the bracket/operator characters the only ones, or is there noise to skip?
- For the calculator: parentheses? unary minus? non-negative only? float or int?
- For sliding window: guaranteed `1 <= k <= n`, or must I handle bad k?

---

## 4. Pattern index (see `stack_queue_tricks.py`)

| Pattern | When to reach for it | Typical complexity |
|---------|----------------------|--------------------|
| **Monotonic stack** | next/previous greater/smaller, daily temperatures, stock span | O(n) amortized |
| **Valid parentheses** | balanced-bracket / matching-delimiter validation | O(n) |
| **Min stack** | stack that also reports min/max in O(1) | O(1) per op |
| **Queue from two stacks** | implement FIFO when only LIFO is available | amortized O(1) |
| **Stack from queue(s)** | implement LIFO when only FIFO is available | push O(n), pop O(1) |
| **Sliding window maximum** | max/min of every length-k window | O(n) (monotonic deque) |
| **Stack calculator** | evaluate infix expressions with precedence | O(n) |
| **Decode / parse with two stacks** | nested encodings `k[...]`, expression trees | O(output) |

---

## 5. Decision guide — "stack, queue, deque, or monotonic?"

```
Do you need the MOST-RECENT item first (LIFO)?
├── Yes → STACK (list: append/pop)
│         e.g. matching/validation, undo, DFS, expression parsing
└── No
    ├── Need the OLDEST item first (FIFO)? → QUEUE (deque: append/popleft)
    │     e.g. BFS, level-order, scheduling, streaming
    ├── Need O(1) at BOTH ends?            → DEQUE (append/appendleft + pop/popleft)
    │     e.g. palindrome checks, fixed-size windows (maxlen)
    └── Scanning for next/prev greater/smaller, or window max/min?
          → MONOTONIC stack (one-sided) / MONOTONIC deque (windowed)
            each element is pushed & popped once → O(n)
```

Quick tells:
- "next greater / previous smaller / span / largest rectangle" → **monotonic stack**.
- "max/min of every window of size k" → **monotonic deque**.
- "balanced / matching / nested" → **stack**.
- "process in arrival order / shortest path on unweighted graph" → **queue (BFS)**.

---

## 6. Python idioms worth knowing (interview-friendly)

```python
from collections import deque

stack = []                          # list is the idiomatic stack
stack.append(x); stack.pop()        # push / pop, O(1)
top = stack[-1] if stack else None  # safe peek

q = deque()                         # deque is the idiomatic queue
q.append(x); q.popleft()            # enqueue / dequeue, O(1)
front = q[0] if q else None         # safe peek front

dq = deque(maxlen=3)                # bounded: auto-drops oldest past maxlen
dq.appendleft(x); dq.rotate(1)      # both-ends ops; rotate right by 1

while stack:                        # drain in LIFO order
    process(stack.pop())

# monotonic-stack skeleton (next greater element)
st = []                             # stores indices
for i, x in enumerate(arr):
    while st and arr[st[-1]] < x:
        ans[st.pop()] = x
    st.append(i)
```

See `fundamentals.py` for the full, runnable list of operations and gotchas, and
`stack_queue_tricks.py` for every pattern above implemented and tested.
