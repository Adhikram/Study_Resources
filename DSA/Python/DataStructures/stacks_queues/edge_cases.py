"""
Stack & queue edge cases — the inputs that break naive solutions, with proof.

Each function demonstrates ONE edge-case category: a naive approach that fails
and the robust version that doesn't. Run `python3 edge_cases.py`; a clean exit
means every "robust" version handled its edge case as documented.

Use this as a pre-submission checklist: walk your solution through each case.
"""

from collections import deque
from typing import Deque, List, Optional


# ---------------------------------------------------------------------------
# 1. EMPTY POP / PEEK — the most common crash. pop() / popleft() / [-1] / [0]
#    on an empty container raises IndexError. DEFINE the empty behavior.
# ---------------------------------------------------------------------------
def empty_pop_peek() -> None:
    def naive_pop(stack):         # crashes on []
        return stack.pop()

    def robust_pop(stack) -> Optional[int]:
        return stack.pop() if stack else None     # explicit contract

    def robust_peek(stack) -> Optional[int]:
        return stack[-1] if stack else None

    assert robust_pop([]) is None
    assert robust_pop([1, 2]) == 2
    assert robust_peek([]) is None
    assert robust_peek([1, 2]) == 2
    try:
        naive_pop([])
        assert False
    except IndexError:
        pass                      # exactly the bug we avoid

    # same hazard for a queue front
    try:
        deque().popleft()
        assert False
    except IndexError:
        pass


# ---------------------------------------------------------------------------
# 2. SINGLE ELEMENT — push/pop should round-trip; min-stack of one element.
# ---------------------------------------------------------------------------
def single_element() -> None:
    s: List[int] = []
    s.append(42)
    assert s[-1] == 42            # peek
    assert s.pop() == 42          # pop
    assert not s                  # now empty

    q: Deque[int] = deque()
    q.append(7)
    assert q[0] == 7 and q.popleft() == 7 and not q


# ---------------------------------------------------------------------------
# 3. UNBALANCED / EMPTY PARENTHESES — leftover openers, lone closers, ''.
# ---------------------------------------------------------------------------
def unbalanced_parentheses() -> None:
    def is_valid(s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack: List[str] = []
        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            elif ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
        return not stack

    assert is_valid("") is True           # empty -> valid
    assert is_valid("(") is False         # leftover opener
    assert is_valid(")") is False         # lone closer (empty stack on close)
    assert is_valid("([)]") is False      # interleaved -> wrong order
    assert is_valid("()[]{}") is True


# ---------------------------------------------------------------------------
# 4. SLIDING WINDOW k BOUNDARIES — k == 1, k == n, k > n, empty, k <= 0.
# ---------------------------------------------------------------------------
def sliding_window_k_boundaries() -> None:
    def max_window(arr: List[int], k: int) -> List[int]:
        n = len(arr)
        if n == 0 or k <= 0 or k > n:     # guard ALL degenerate k up front
            return []
        out: List[int] = []
        dq: Deque[int] = deque()
        for i in range(n):
            if dq and dq[0] <= i - k:
                dq.popleft()
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                out.append(arr[dq[0]])
        return out

    assert max_window([4, 2, 9, 1], 1) == [4, 2, 9, 1]   # k == 1 -> each element
    assert max_window([4, 2, 9, 1], 4) == [9]            # k == n -> one window
    assert max_window([4, 2, 9, 1], 5) == []             # k > n -> no window
    assert max_window([], 3) == []                       # empty
    assert max_window([1, 2, 3], 0) == []                # k <= 0


# ---------------------------------------------------------------------------
# 5. EXPRESSION WITH SPACES / SINGLE NUMBER — flushing the last operand.
# ---------------------------------------------------------------------------
def expression_spaces_single() -> None:
    def calc(s: str) -> int:
        stack: List[int] = []
        num, op = 0, '+'
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (ch in '+-*/') or i == len(s) - 1:   # flush on last char too
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))
                op, num = ch, 0
        return sum(stack)

    assert calc("42") == 42              # single number, no operator
    assert calc("   7   ") == 7          # surrounded by spaces
    assert calc(" 3 + 2 * 2 ") == 7      # spaces between tokens
    assert calc("100/3") == 33           # truncation toward zero


# ---------------------------------------------------------------------------
# 6. list.pop(0) AS A QUEUE — correct value, WRONG complexity. Prefer deque.
# ---------------------------------------------------------------------------
def list_as_queue_trap() -> None:
    # Both dequeue the same FIFO order; the list version is O(n) per pop
    # (it shifts every remaining element), the deque version is O(1).
    lst = [1, 2, 3]
    dq = deque([1, 2, 3])
    out_lst, out_dq = [], []
    while lst:
        out_lst.append(lst.pop(0))   # O(n) each -> O(n^2) overall
    while dq:
        out_dq.append(dq.popleft())  # O(1) each -> O(n) overall
    assert out_lst == out_dq == [1, 2, 3]


def main() -> None:
    empty_pop_peek()
    single_element()
    unbalanced_parentheses()
    sliding_window_k_boundaries()
    expression_spaces_single()
    list_as_queue_trap()
    print("edge_cases.py: all 6 edge-case categories verified ✔")


if __name__ == "__main__":
    main()
