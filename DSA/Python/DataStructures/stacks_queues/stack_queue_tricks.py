"""
Core stack & queue patterns for coding interviews — runnable & self-testing.

Every pattern below is a real, callable function or class (not a stub) with its
time and space complexity, the edge cases it handles, and inline `assert` tests.
Run `python3 stack_queue_tricks.py`; a clean exit means all patterns passed.

Patterns:
    1.  Monotonic stack       — next greater element & daily temperatures
    2.  Valid parentheses     — match (), [], {} with a stack
    3.  Min stack             — O(1) push/pop/top AND getMin
    4.  MyQueue (2 stacks)     — FIFO via two LIFO stacks, amortized O(1)
    5.  MyStack (queues)       — LIFO via FIFO queue(s)
    6.  Sliding window maximum — monotonic deque, O(n)
    7.  Basic calculator       — +-*/ with precedence, single pass
    8.  Decode string          — "3[a]2[bc]" -> "aaabcbc" with two stacks
"""

from collections import deque
from typing import Deque, List, Optional


# ===========================================================================
# 1. MONOTONIC STACK — next/previous greater/smaller in O(n)
# ===========================================================================
def next_greater_element(arr: List[int]) -> List[int]:
    """For each element, the next element to its RIGHT that is strictly greater,
    or -1 if none. Time O(n) amortized, Space O(n).
    Trick: keep a stack of indices whose 'next greater' is still unknown. Each
    index is pushed once and popped once -> O(n) total (see COMPLEXITY.md).
    Edge cases: empty -> []; strictly decreasing -> all -1."""
    n = len(arr)
    result = [-1] * n
    stack: List[int] = []            # indices with no greater element seen yet
    for i in range(n):
        # current arr[i] is the answer for every smaller index on the stack top
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result                    # indices left on the stack keep -1


def daily_temperatures(temps: List[int]) -> List[int]:
    """For each day, how many days until a WARMER temperature (0 if none).
    Time O(n) amortized, Space O(n). Same monotonic-stack idea, but we store
    the DISTANCE (index gap) instead of the value.
    Edge cases: empty -> []; non-increasing -> all 0."""
    n = len(temps)
    result = [0] * n
    stack: List[int] = []            # indices of days still waiting for warmth
    for i in range(n):
        while stack and temps[i] > temps[stack[-1]]:
            j = stack.pop()
            result[j] = i - j        # days waited
        stack.append(i)
    return result


# ===========================================================================
# 2. VALID PARENTHESES — match (), [], {} using a stack
# ===========================================================================
def is_valid_parentheses(s: str) -> bool:
    """True iff every bracket is closed by the correct type in the right order.
    Time O(n), Space O(n). Push openers; on a closer, the stack top MUST be its
    match. Edge cases: '' -> True; leftover openers / lone closer -> False."""
    pairs = {')': '(', ']': '[', '}': '{'}
    stack: List[str] = []
    for ch in s:
        if ch in pairs.values():          # an opener
            stack.append(ch)
        elif ch in pairs:                 # a closer
            if not stack or stack.pop() != pairs[ch]:
                return False
        # any other character is ignored
    return not stack                      # all openers must be closed


# ===========================================================================
# 3. MIN STACK — push/pop/top/getMin all O(1)
# ===========================================================================
class MinStack:
    """A stack that also reports its current minimum in O(1).
    Trick: a parallel 'min_stack' whose top is always the min of everything
    currently in the main stack. Push the new min (or repeat the old one) on
    every push; pop it in lockstep. Time O(1) per op, Space O(n).
    Edge cases: top()/get_min() on empty -> None instead of crashing."""

    def __init__(self) -> None:
        self._stack: List[int] = []
        self._mins: List[int] = []        # _mins[-1] == min(self._stack)

    def push(self, x: int) -> None:
        self._stack.append(x)
        # store the running minimum so far (<= keeps duplicates safe on pop)
        self._mins.append(x if not self._mins else min(x, self._mins[-1]))

    def pop(self) -> Optional[int]:
        if not self._stack:
            return None
        self._mins.pop()
        return self._stack.pop()

    def top(self) -> Optional[int]:
        return self._stack[-1] if self._stack else None

    def get_min(self) -> Optional[int]:
        return self._mins[-1] if self._mins else None


# ===========================================================================
# 4. MyQueue — a FIFO queue built from two LIFO stacks
# ===========================================================================
class MyQueue:
    """Queue (FIFO) using two stacks. Amortized O(1) per operation.
    Trick: `_in` receives pushes; `_out` serves pops. When `_out` is empty we
    pour `_in` into it, reversing the order so the oldest element ends up on
    top. Each element is moved across at most once -> amortized O(1).
    Edge cases: peek/pop on empty -> None."""

    def __init__(self) -> None:
        self._in: List[int] = []     # newest on top
        self._out: List[int] = []    # oldest on top

    def push(self, x: int) -> None:  # enqueue, O(1)
        self._in.append(x)

    def _shift(self) -> None:
        if not self._out:            # only refill when empty (keeps it amortized)
            while self._in:
                self._out.append(self._in.pop())

    def pop(self) -> Optional[int]:  # dequeue front, amortized O(1)
        self._shift()
        return self._out.pop() if self._out else None

    def peek(self) -> Optional[int]:
        self._shift()
        return self._out[-1] if self._out else None

    def empty(self) -> bool:
        return not self._in and not self._out


# ===========================================================================
# 5. MyStack — a LIFO stack built from FIFO queue(s)
# ===========================================================================
class MyStack:
    """Stack (LIFO) using a single FIFO queue. push O(n), pop/top O(1).
    Trick: after enqueuing the new element, rotate the queue so that the new
    element is moved to the FRONT (rotate the older elements behind it). Then
    popleft always returns the most-recently pushed value.
    Edge cases: pop/top on empty -> None."""

    def __init__(self) -> None:
        self._q: Deque[int] = deque()

    def push(self, x: int) -> None:  # O(n): rotate to put newest at the front
        self._q.append(x)
        for _ in range(len(self._q) - 1):
            self._q.append(self._q.popleft())

    def pop(self) -> Optional[int]:  # O(1)
        return self._q.popleft() if self._q else None

    def top(self) -> Optional[int]:
        return self._q[0] if self._q else None

    def empty(self) -> bool:
        return not self._q


# ===========================================================================
# 6. SLIDING WINDOW MAXIMUM — monotonic deque, O(n)
# ===========================================================================
def max_sliding_window(arr: List[int], k: int) -> List[int]:
    """Maximum of every contiguous window of size k. Time O(n), Space O(k).
    Trick: a deque of INDICES kept in decreasing value order. The front is
    always the window's max; we drop indices that fall out of the window
    (front) and indices smaller than the incoming value (back). Each index
    enters and leaves the deque once -> O(n) (see COMPLEXITY.md).
    Edge cases: k==1 -> arr itself; k==len(arr) -> [max(arr)];
    empty / k<=0 / k>len -> []."""
    n = len(arr)
    if n == 0 or k <= 0 or k > n:
        return []
    result: List[int] = []
    window: Deque[int] = deque()     # indices, arr-values strictly decreasing
    for i in range(n):
        if window and window[0] <= i - k:    # front fell out of the window
            window.popleft()
        while window and arr[i] >= arr[window[-1]]:   # back is now useless
            window.pop()
        window.append(i)
        if i >= k - 1:               # first full window starts at index k-1
            result.append(arr[window[0]])
    return result


# ===========================================================================
# 7. BASIC CALCULATOR — + - * / with precedence, no parentheses
# ===========================================================================
def calculate(s: str) -> int:
    """Evaluate an expression of non-negative ints with + - * / and spaces.
    * and / bind tighter than + and -. Integer division truncates toward zero.
    Time O(n), Space O(n).
    Trick: defer each number with the PENDING sign. For + / - push (+/-)num.
    For * / pop the top and combine immediately (precedence). Sum the stack.
    Edge cases: single number; leading/trailing spaces; '3+2*2' -> 7."""
    stack: List[int] = []
    num = 0
    op = '+'                         # the operator that PRECEDES `num`
    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)
        # act when we hit an operator OR the final character (flush last num)
        if (ch in '+-*/') or i == len(s) - 1:
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            elif op == '/':
                # int() truncates toward zero (differs from // on negatives)
                stack.append(int(stack.pop() / num))
            op = ch
            num = 0
    return sum(stack)


# ===========================================================================
# 8. DECODE STRING — "3[a]2[bc]" -> "aaabcbc" with two stacks
# ===========================================================================
def decode_string(s: str) -> str:
    """Expand run-length-encoded strings of the form k[encoded]. Nesting allowed:
    '3[a2[c]]' -> 'accaccacc'. Time/Space O(output length).
    Trick: two stacks. On '[' push the repeat count and the string-so-far, then
    reset. On ']' pop them and fold: prev + count * current.
    Edge cases: no brackets -> returned unchanged; nested brackets handled."""
    count_stack: List[int] = []
    str_stack: List[str] = []
    current = ""
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '[':
            count_stack.append(num)
            str_stack.append(current)
            num = 0
            current = ""
        elif ch == ']':
            repeat = count_stack.pop()
            current = str_stack.pop() + current * repeat
        else:
            current += ch
    return current


# ===========================================================================
# TESTS — run via main(); cover normal + edge cases
# ===========================================================================
def _test() -> None:
    # 1. monotonic stack
    assert next_greater_element([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
    assert next_greater_element([]) == []
    assert next_greater_element([5, 4, 3]) == [-1, -1, -1]   # decreasing
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == \
        [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures([]) == []
    assert daily_temperatures([30, 20, 10]) == [0, 0, 0]

    # 2. valid parentheses
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("([{}])") is True
    assert is_valid_parentheses("(]") is False
    assert is_valid_parentheses("(") is False        # leftover opener
    assert is_valid_parentheses(")") is False        # lone closer
    assert is_valid_parentheses("") is True          # empty is valid

    # 3. min stack
    ms = MinStack()
    assert ms.get_min() is None and ms.top() is None  # empty
    for v in (5, 3, 7, 3):
        ms.push(v)
    assert ms.get_min() == 3 and ms.top() == 3
    assert ms.pop() == 3                              # removes one of the 3s
    assert ms.get_min() == 3                          # other 3 still present
    assert ms.pop() == 7
    assert ms.get_min() == 3
    assert ms.pop() == 3
    assert ms.get_min() == 5                          # back to 5

    # 4. MyQueue (FIFO via two stacks)
    q = MyQueue()
    assert q.empty() is True and q.pop() is None
    for v in (1, 2, 3):
        q.push(v)
    assert q.peek() == 1
    assert q.pop() == 1
    q.push(4)                                         # interleave push & pop
    assert q.pop() == 2 and q.pop() == 3 and q.pop() == 4
    assert q.empty() is True

    # 5. MyStack (LIFO via a queue)
    st = MyStack()
    assert st.empty() is True and st.pop() is None
    for v in (1, 2, 3):
        st.push(v)
    assert st.top() == 3
    assert st.pop() == 3 and st.pop() == 2
    st.push(9)
    assert st.pop() == 9 and st.pop() == 1
    assert st.empty() is True

    # 6. sliding window maximum
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert max_sliding_window([1, 2, 3], 1) == [1, 2, 3]   # k == 1
    assert max_sliding_window([4, 2, 9], 3) == [9]         # k == n
    assert max_sliding_window([], 3) == []                 # empty
    assert max_sliding_window([1, 2], 5) == []             # k > n

    # 7. basic calculator with precedence
    assert calculate("3+2*2") == 7
    assert calculate(" 3/2 ") == 1                         # spaces + truncation
    assert calculate(" 3+5 / 2 ") == 5
    assert calculate("42") == 42                           # single number
    assert calculate("14-3/2") == 13
    assert calculate("2*3+4*5") == 26

    # 8. decode string (incl. nesting & no-bracket passthrough)
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"        # nested
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert decode_string("abc") == "abc"                   # no brackets


def main() -> None:
    _test()
    print("stack_queue_tricks.py: all 8 patterns verified ✔")


if __name__ == "__main__":
    main()
