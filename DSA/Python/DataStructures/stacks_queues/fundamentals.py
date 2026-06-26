"""
Stack & Queue fundamentals for interviews — Python `list` and `collections.deque`.

Covers every operation you are likely to use, its time complexity, and the
gotchas that cause real interview bugs. Each section is runnable and verified
with `assert`s. Run `python3 fundamentals.py` — if it exits cleanly, every
example behaved as documented.

A STACK is LIFO (Last In, First Out): the last thing pushed is the first popped.
A QUEUE is FIFO (First In, First Out): the first thing enqueued is the first out.

In Python:
  - A plain `list` is a perfect stack — `append`/`pop` are both O(1) at the end.
  - A `collections.deque` is the right queue — `append`/`popleft` are both O(1).
    Do NOT use `list.pop(0)` for a queue: it shifts every element -> O(n).
  - A `deque` is also a double-ended queue: O(1) push/pop at *both* ends.
"""

from collections import deque
from typing import Deque, List, Optional


# ---------------------------------------------------------------------------
# 1. STACK via list — LIFO. push/pop/peek/empty are all O(1).
# ---------------------------------------------------------------------------
def stack_ops() -> None:
    stack: List[int] = []

    # push -> append to the end, O(1) amortized
    stack.append(1)
    stack.append(2)
    stack.append(3)               # stack is now [1, 2, 3], top == 3
    assert stack == [1, 2, 3]

    # peek -> read the top WITHOUT removing it, O(1)
    assert stack[-1] == 3

    # pop -> remove & return the top (LIFO), O(1)
    assert stack.pop() == 3       # -> [1, 2]
    assert stack.pop() == 2       # -> [1]
    assert stack == [1]

    # empty check -> truthiness, O(1)
    assert bool(stack) is True    # non-empty -> truthy
    stack.pop()
    assert not stack              # empty -> falsy

    # size, O(1)
    stack.append(9)
    assert len(stack) == 1


# ---------------------------------------------------------------------------
# 2. QUEUE via deque — FIFO. enqueue/dequeue/peek are all O(1).
# ---------------------------------------------------------------------------
def queue_ops() -> None:
    queue: Deque[int] = deque()

    # enqueue -> append to the right (back), O(1)
    queue.append(1)
    queue.append(2)
    queue.append(3)               # front == 1, back == 3
    assert list(queue) == [1, 2, 3]

    # peek front -> queue[0], O(1)
    assert queue[0] == 1
    # peek back -> queue[-1], O(1)
    assert queue[-1] == 3

    # dequeue -> popleft removes & returns the FRONT (FIFO), O(1)
    assert queue.popleft() == 1   # -> [2, 3]
    assert queue.popleft() == 2   # -> [3]
    assert list(queue) == [3]

    # empty check & size, O(1)
    assert len(queue) == 1
    queue.popleft()
    assert not queue 


# ---------------------------------------------------------------------------
# 3. DEQUE both-ends — double-ended queue. O(1) at the front AND the back.
# ---------------------------------------------------------------------------
def deque_ops() -> None:
    dq: Deque[int] = deque()

    # push back / push front — both O(1)
    dq.append(2)                  # [2]
    dq.append(3)                  # [2, 3]
    dq.appendleft(1)              # [1, 2, 3]
    dq.appendleft(0)              # [0, 1, 2, 3]
    assert list(dq) == [0, 1, 2, 3]

    # pop back / pop front — both O(1)
    assert dq.pop() == 3          # [0, 1, 2]
    assert dq.popleft() == 0      # [1, 2]
    assert list(dq) == [1, 2]

    # peek both ends — O(1)
    assert dq[0] == 1 and dq[-1] == 2

    # bounded deque: maxlen auto-evicts from the opposite end (handy for windows)
    last3: Deque[int] = deque(maxlen=3)
    for x in [1, 2, 3, 4, 5]:
        last3.append(x)           # pushing past maxlen drops from the left
    assert list(last3) == [3, 4, 5]

    # rotate — O(k); rotate right by 1 moves the back element to the front
    r = deque([1, 2, 3, 4])
    r.rotate(1)
    assert list(r) == [4, 1, 2, 3]


# ---------------------------------------------------------------------------
# 4. Safe wrappers — explicit empty handling instead of letting it crash.
#    Interviews expect you to DEFINE behavior on empty, not raise blindly.
# ---------------------------------------------------------------------------
def safe_peek(container) -> Optional[int]:
    """Peek the 'top'/'front' without removing it; None if empty. O(1)."""
    if not container:
        return None
    return container[-1] if isinstance(container, list) else container[0]


def safe_pop_stack(stack: List[int]) -> Optional[int]:
    """Pop top of a stack; None if empty (instead of IndexError). O(1)."""
    return stack.pop() if stack else None


def safe_dequeue(queue: Deque[int]) -> Optional[int]:
    """Dequeue front; None if empty (instead of IndexError). O(1)."""
    return queue.popleft() if queue else None


def safe_wrappers() -> None:
    assert safe_pop_stack([]) is None
    assert safe_pop_stack([1, 2]) == 2
    assert safe_dequeue(deque()) is None
    assert safe_dequeue(deque([1, 2])) == 1
    assert safe_peek([]) is None
    assert safe_peek([1, 2, 3]) == 3            # stack top
    assert safe_peek(deque([1, 2, 3])) == 1     # queue front


# ---------------------------------------------------------------------------
# 5. GOTCHAS — the bugs that cost interviews
# ---------------------------------------------------------------------------
def gotchas() -> None:
    # (a) pop / popleft on an EMPTY container raises IndexError — never assume
    #     there is something to remove. Guard with `if container:` first.
    empty_stack: List[int] = []
    try:
        empty_stack.pop()
        assert False, "expected IndexError"
    except IndexError:
        pass
    empty_q: Deque[int] = deque()
    try:
        empty_q.popleft()
        assert False, "expected IndexError"
    except IndexError:
        pass

    # (b) PEEKING an empty container with [-1] / [0] also raises IndexError.
    try:
        _ = empty_stack[-1]
        assert False, "expected IndexError"
    except IndexError:
        pass

    # (c) THE BIG ONE: list.pop(0) as a queue dequeue is O(n), not O(1).
    #     It shifts every remaining element left one slot. Correct but a hidden
    #     O(n^2) if done in a loop. Functionally equal, asymptotically a trap:
    as_list = [1, 2, 3]
    as_dq = deque([1, 2, 3])
    assert as_list.pop(0) == as_dq.popleft() == 1   # same VALUE...
    # ...but list.pop(0) shifted [2,3] left (O(n)); deque.popleft() did not (O(1)).
    assert as_list == [2, 3] and list(as_dq) == [2, 3]

    # (d) deque vs list: random indexing in the MIDDLE of a deque is O(n)
    #     (it is a doubly-linked list of blocks). Lists are O(1) by index.
    #     Use a list when you need fast arbitrary indexing; a deque for ends.
    dq = deque(range(1000))
    assert dq[500] == 500     # works, but this is O(n), not O(1) like a list

    # (e) Iterating a stack does NOT pop it — `for x in stack` leaves it intact.
    #     To drain in LIFO order you must actually pop in a loop.
    s = [1, 2, 3]
    seen = [x for x in s]
    assert seen == [1, 2, 3] and s == [1, 2, 3]   # untouched
    drained = []
    while s:
        drained.append(s.pop())
    assert drained == [3, 2, 1]                    # LIFO order, now empty

    # (f) deque(iterable) copies the iterable; mutating one doesn't affect the
    #     other — but the elements are shared (shallow), same as list().
    base = [1, 2, 3]
    dq2 = deque(base)
    dq2.append(4)
    assert base == [1, 2, 3]   # original list unchanged


def main() -> None:
    stack_ops()
    queue_ops()
    deque_ops()
    safe_wrappers()
    gotchas()
    print("fundamentals.py: all examples verified ✔")


if __name__ == "__main__":
    main()
