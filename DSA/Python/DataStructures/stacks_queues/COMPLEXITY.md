# Complexity — the *why* behind the Big-O

The number (`O(n)`, `O(1)`, ...) is the answer. This file is the **reasoning
trick** that produces it — the mental model that lets you derive the complexity
in an interview instead of memorizing it. Each entry names the trick, then
proves it.

Two reasoning tools cover almost everything here:

1. **Structure choice** — the right data structure makes an operation O(1) that
   would be O(n) on the wrong one. This is the `deque` vs `list.pop(0)` story.
2. **Amortized / charging argument** — "this loop looks like it could be O(n²),
   but each element is pushed and popped *at most once total*, so it's O(n)."
   This single argument covers monotonic stacks, the two-stack queue, and the
   sliding-window-maximum deque.

If you can spot which of these applies, you can derive the bound yourself.

---

## 1. `deque` is O(1) at both ends — the doubly-linked-block structure

A `collections.deque` is **not** a contiguous array. It is a doubly-linked list
of small fixed-size blocks. The deque keeps direct pointers to the **head block**
and the **tail block**, so:

- `append` / `pop` (right end) touch only the tail block → **O(1)**.
- `appendleft` / `popleft` (left end) touch only the head block → **O(1)**.

Nothing downstream has to move, because there is no single contiguous array
whose indices must stay packed. That is exactly why a deque can give you O(1) at
*both* ends, which a list fundamentally cannot.

**The trade-off:** indexing the *middle* (`dq[i]`) must walk from an end across
blocks → **O(n)**. A list pays the opposite price: O(1) indexing, O(n) front ops.

---

## 2. `list.pop(0)` is O(n) — contiguous shifting, no trick

A `list` stores elements contiguously by index. Removing element 0 means **every
later element must shift one slot left** to keep indices contiguous. n shifts →
**O(n)** for a single dequeue. Do it in a loop to drain the queue and you get
`n + (n-1) + ... + 1 ≈ n²/2` → **O(n²)** — a classic hidden blowup.

**Interview tell:** `while q: x = q.pop(0)` is O(n²). Swap the `list` for a
`deque` and `pop(0)` for `popleft()` and the same loop becomes O(n). There is no
clever workaround *for a list front* — O(1) at the front is what a deque is for.

---

## 3. Monotonic stack — amortized O(n) by the "pushed once, popped once" charge

```python
st = []                       # indices, kept monotonic
for i in range(n):            # outer loop: n iterations
    while st and arr[i] > arr[st[-1]]:   # inner loop: how many times total?
        st.pop()
    st.append(i)
```

The inner `while` makes people guess O(n²). It isn't. **Charging argument:** each
index is `append`ed to the stack **exactly once**, and once it is popped it is
gone for good — it can be popped **at most once**. So across the *entire* run,
the total number of pop operations is ≤ n, no matter how the outer loop and inner
loop interleave.

Total work = n appends + (≤ n) pops + n outer steps = **O(n)** time, O(n) space.
The key insight: don't multiply the inner loop by the outer loop — *sum* the work
charged to each element. Each element pays O(1) to enter and O(1) to leave.

This is identical reasoning for **next greater element**, **daily temperatures**,
**stock span**, and **largest rectangle in a histogram**.

---

## 4. Queue from two stacks — amortized O(1) by "each element crosses once"

```python
_in, _out = [], []
def push(x): _in.append(x)            # always O(1)
def pop():
    if not _out:                      # only refill when _out is empty
        while _in: _out.append(_in.pop())
    return _out.pop()
```

A single `pop` can be O(n) when it has to pour the whole `_in` stack into `_out`.
So how is it amortized O(1)?

**Charging argument:** every element is moved from `_in` to `_out` **exactly
once** in its lifetime. Once it is in `_out`, it is never moved again — it just
gets popped. So the transfer cost of any element is O(1), charged once. Across n
pushes and n pops, total transfer work is O(n), spread over O(n) operations =
**O(1) amortized per operation.**

The crucial detail is `if not _out:` — refilling **only when `_out` is empty**.
If you refilled on every pop, elements would cross repeatedly and you'd lose the
amortized bound. Worst-case single op is still O(n); the *average* is O(1).

---

## 5. Sliding window maximum — O(n) because each index enters and leaves once

```python
dq = deque()                  # indices, arr-values strictly decreasing
for i in range(n):
    if dq and dq[0] <= i - k: dq.popleft()     # drop the index that fell out
    while dq and arr[i] >= arr[dq[-1]]: dq.pop()  # drop now-useless indices
    dq.append(i)
    if i >= k - 1: out.append(arr[dq[0]])
```

The inner `while` again suggests O(n²). Same charge as the monotonic stack:
**every index is `append`ed exactly once and removed at most once** (either by
the front `popleft` when it leaves the window, or by a back `pop` when a larger
value arrives). Total deque operations ≤ 2n → **O(n) time**.

Space is **O(k)**: the deque can hold at most one full window of indices at a
time. The deque front is always the window maximum because we maintain a strictly
decreasing order — anything smaller than the incoming value can never be the max
again while that larger value is in the window, so we discard it immediately.

---

## 6. Min stack — O(1) getMin with an auxiliary stack

To report the minimum of a stack in O(1), keep a **parallel `mins` stack** whose
top always equals the minimum of everything currently in the main stack:

```python
def push(x): mins.append(x if not mins else min(x, mins[-1]))
def pop():   mins.pop(); return stack.pop()
def get_min(): return mins[-1]
```

Every push pushes one value onto `mins` (either the new value or a repeat of the
old min), and every pop removes one — so `mins` stays in lockstep with the main
stack. No scanning, ever: `get_min` is just `mins[-1]`. **O(1) per operation**,
**O(n) extra space.** The trick is precomputing the answer *at push time* so the
query is a constant-time read, trading O(n) space for O(1) queries.

---

## 7. Stack from a queue — push O(n) to make pop O(1)

```python
def push(x):                  # rotate so the newest element is at the FRONT
    q.append(x)
    for _ in range(len(q) - 1):
        q.append(q.popleft())
def pop(): return q.popleft()  # O(1): front is always the most recent push
```

A FIFO queue hands out the *oldest* element first, but a stack needs the
*newest*. The trick: at push time, **rotate the queue** so the just-added element
is moved to the front and all older elements queue up behind it. That rotation
touches every element once → **push is O(n)**. In exchange, the front is always
the most-recently pushed value, so **pop and top are O(1)**. You choose which
operation to make expensive; here we front-load the cost onto `push`.

---

## 8. Valid parentheses & decode string — O(n), one pass, stack-bounded

Both scan the input once. **Valid parentheses** pushes each opener and pops on
each closer (O(1) each) → **O(n) time, O(n) space** (the stack can hold up to n
openers, e.g. `"((((("`). **Decode string** pushes the pending count and
string-so-far on `[` and folds them back on `]`; total work is proportional to
the **length of the output**, since each output character is produced once →
**O(output) time and space**. No element is reprocessed — the single-pass +
push-once structure is what keeps both linear.

---

## 9. Basic calculator — O(n) by deferring with a pending operator

```python
num, op = 0, '+'              # `op` is the operator preceding `num`
for ch in s:
    ... build num ...
    on operator-or-end:
        + / -  → push (+/-)num            # defer; sum later
        * / /  → push(stack.pop() OP num)  # apply immediately (precedence)
return sum(stack)
```

Precedence is handled in **one pass** without a second operator stack: `+`/`-`
just *defer* their operand onto the stack, while `*`/`/` *immediately* combine
with the top (because they bind tighter and can't be deferred). Each character is
visited once and does O(1) work; the final `sum(stack)` is O(n) → **O(n) time,
O(n) space.** The trick is the "pending operator" variable that lets a single
left-to-right scan respect precedence.

---

## Cheat-sheet: which trick gives which bound

| Bound | Trick that produces it |
|-------|------------------------|
| O(1) at both ends (deque) | doubly-linked blocks with head & tail pointers — no shifting |
| O(n) for `list.pop(0)` | contiguous storage forces every later element to shift left |
| O(n) from a stack/deque loop-with-inner-loop | each element is pushed once & popped ≤ once *total* (charging) |
| Amortized O(1) (two-stack queue) | each element crosses `_in`→`_out` exactly once; refill only when empty |
| O(k) space (window deque) | the deque holds at most one window of indices |
| O(1) query after O(n) build (min stack) | precompute the running min at push time |
| push O(n) / pop O(1) (stack from queue) | rotate on push to seat the newest element at the front |
| O(n) one-pass parse (parens / calc / decode) | visit each char once, O(1) work, stack bounded by input/output |
