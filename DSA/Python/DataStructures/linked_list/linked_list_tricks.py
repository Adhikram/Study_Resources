"""
Core linked-list patterns for coding interviews — runnable & self-testing.

Every pattern below is a real, callable function (not a stub) with its time and
space complexity, the edge cases it handles, and inline `assert` tests. Run
`python3 linked_list_tricks.py`; a clean exit means all patterns passed.

The patterns reuse a tiny `Node` plus two helpers — `build(list)` and
`to_list(head)` — so each test reads as Python lists while exercising real
node-pointer code.

Patterns:
    1.  Reverse                 — iterative (O(1) space) & recursive
    2.  Fast / slow pointers    — find the middle node in one pass
    3.  Floyd's cycle detection — has-cycle + find the cycle's START node
    4.  Merge two sorted lists  — dummy-node splice
    5.  Remove Nth from end     — two-pointer gap, one pass
    6.  Intersection of lists   — length-difference / two-pointer switch
    7.  Palindrome check        — reverse second half, O(1) space
    8.  Reorder list            — split + reverse + interleave
    9.  Dummy-node removal       — delete all nodes matching a value
"""

from typing import Optional, List


# ===========================================================================
# Node + test helpers (list <-> linked list)
# ===========================================================================
class Node:
    """Singly-linked-list node."""

    __slots__ = ("val", "next")

    def __init__(self, val: int, next: "Optional[Node]" = None) -> None:
        self.val = val
        self.next = next


def build(values: List[int]) -> Optional[Node]:
    """Build a linked list from a Python list; return the head (None if empty)."""
    head: Optional[Node] = None
    for v in reversed(values):        # build back-to-front so order is preserved
        head = Node(v, head)
    return head


def to_list(head: Optional[Node]) -> List[int]:
    """Materialize a linked list into a Python list. O(n)."""
    out: List[int] = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


# ===========================================================================
# 1. REVERSE — iterative (O(1) space) and recursive (O(n) stack)
# ===========================================================================
def reverse_iterative(head: Optional[Node]) -> Optional[Node]:
    """Reverse the list and return the new head. Time O(n), Space O(1).
    Flip each node's pointer to its predecessor; stash `next` before overwriting.
    Edge cases: empty / single -> returned unchanged."""
    prev: Optional[Node] = None
    cur = head
    while cur is not None:
        nxt = cur.next        # remember the rest BEFORE we clobber the pointer
        cur.next = prev       # reverse this link
        prev = cur            # advance prev
        cur = nxt             # advance cur
    return prev               # old tail is the new head


def reverse_recursive(head: Optional[Node]) -> Optional[Node]:
    """Reverse via recursion. Time O(n), Space O(n) call stack (NOT O(1)).
    Base case: empty / single returns itself. Otherwise reverse the tail, then
    make the next node point back at us and sever our forward link."""
    if head is None or head.next is None:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head     # the node after us now points back to us
    head.next = None          # we become the new tail
    return new_head


# ===========================================================================
# 2. FAST / SLOW POINTERS — find the middle node in a single pass
# ===========================================================================
def find_middle(head: Optional[Node]) -> Optional[Node]:
    """Return the middle node. Time O(n), Space O(1).
    `slow` moves 1 step, `fast` moves 2; when fast falls off, slow is at the
    middle. For EVEN length this returns the SECOND of the two middles
    (LeetCode convention). Edge cases: empty -> None; single -> that node."""
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next      # type: ignore[union-attr]
        fast = fast.next.next
    return slow


# ===========================================================================
# 3. FLOYD'S CYCLE DETECTION — has-cycle, then find the cycle's start
# ===========================================================================
def has_cycle(head: Optional[Node]) -> bool:
    """Detect a cycle with the tortoise & hare. Time O(n), Space O(1).
    If fast ever equals slow, there's a loop; if fast hits None, there isn't."""
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next      # type: ignore[union-attr]
        fast = fast.next.next
        if slow is fast:      # identity, not value — they met
            return True
    return False


def cycle_start(head: Optional[Node]) -> Optional[Node]:
    """Return the node where the cycle begins, or None if acyclic. O(n), O(1).
    Step 1: find a meeting point (Floyd). Step 2: reset one pointer to head and
    advance both one step at a time — they meet AT the cycle's entrance. (Why
    this works is derived in COMPLEXITY.md.)"""
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next      # type: ignore[union-attr]
        fast = fast.next.next
        if slow is fast:                  # cycle confirmed
            ptr = head
            while ptr is not slow:
                ptr = ptr.next            # type: ignore[union-attr]
                slow = slow.next          # type: ignore[union-attr]
            return ptr
    return None


# ===========================================================================
# 4. MERGE TWO SORTED LISTS — dummy-node splice
# ===========================================================================
def merge_sorted(a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
    """Merge two SORTED lists into one sorted list. Time O(n+m), Space O(1).
    A dummy head lets us append without a special 'first node' case; `tail`
    always has a valid `.next` to set. Edge cases: either list empty -> the
    other is returned (attached after the dummy)."""
    dummy = Node(0)
    tail = dummy
    while a is not None and b is not None:
        if a.val <= b.val:                # <= keeps the merge STABLE
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a if a is not None else b  # attach whatever remains (already sorted)
    return dummy.next


# ===========================================================================
# 5. REMOVE Nth FROM END — two-pointer gap, single pass
# ===========================================================================
def remove_nth_from_end(head: Optional[Node], n: int) -> Optional[Node]:
    """Remove the n-th node from the END (1-indexed). Time O(n), Space O(1).
    Open a gap of n between `fast` and `slow` by advancing fast n steps, then
    move both until fast hits the tail — slow now sits just BEFORE the target.
    A dummy before head handles removing the head itself. Edge case: removing
    the only node -> empty list."""
    dummy = Node(0, head)
    fast: Optional[Node] = dummy
    slow: Optional[Node] = dummy
    for _ in range(n):                    # open the n-node gap
        assert fast is not None
        fast = fast.next
    while fast is not None and fast.next is not None:
        fast = fast.next
        slow = slow.next                  # type: ignore[union-attr]
    assert slow is not None and slow.next is not None
    slow.next = slow.next.next            # unlink the target
    return dummy.next


# ===========================================================================
# 6. INTERSECTION OF TWO LISTS — find the shared-tail node (by identity)
# ===========================================================================
def get_intersection(a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
    """Return the first SHARED node (by identity) of two lists, or None.
    Time O(n+m), Space O(1). Two walkers swap to the other list's head on
    reaching the end; after at most len(a)+len(b) steps they align at the
    intersection (or both reach None together if there is none)."""
    if a is None or b is None:
        return None
    p, q = a, b
    while p is not q:                     # identity comparison, not value
        p = p.next if p is not None else b
        q = q.next if q is not None else a
    return p                              # the meeting node, or None


# ===========================================================================
# 7. PALINDROME CHECK — reverse the second half, compare, O(1) space
# ===========================================================================
def is_palindrome(head: Optional[Node]) -> bool:
    """Is the list a palindrome by value? Time O(n), Space O(1).
    Find the middle (fast/slow), reverse the second half, then walk both halves
    inward. Edge cases: empty / single -> True. (This mutates the list while
    checking; restore it in production if the caller still needs it.)"""
    if head is None or head.next is None:
        return True
    # 1. middle via fast/slow
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next      # type: ignore[union-attr]
        fast = fast.next.next
    # 2. reverse the second half (from slow onward)
    prev: Optional[Node] = None
    cur = slow
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    # 3. compare first half with reversed second half
    left, right = head, prev
    while right is not None:              # second half is the shorter/equal one
        if left.val != right.val:         # type: ignore[union-attr]
            return False
        left = left.next                  # type: ignore[union-attr]
        right = right.next
    return True


# ===========================================================================
# 8. REORDER LIST — L0->L1->...->Ln  becomes  L0->Ln->L1->Ln-1->...
# ===========================================================================
def reorder_list(head: Optional[Node]) -> Optional[Node]:
    """Reorder in place to L0->Ln->L1->Ln-1->... Time O(n), Space O(1).
    Three moves: (1) find middle, (2) reverse the second half, (3) interleave
    the two halves. Edge cases: empty / single / two nodes -> unchanged."""
    if head is None or head.next is None:
        return head
    # 1. middle (slow ends at start of 2nd half for splitting)
    slow, fast = head, head.next
    while fast is not None and fast.next is not None:
        slow = slow.next      # type: ignore[union-attr]
        fast = fast.next.next
    second = slow.next                    # type: ignore[union-attr]
    slow.next = None                      # type: ignore[union-attr]  # split halves
    # 2. reverse the second half
    prev: Optional[Node] = None
    cur = second
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    second = prev
    # 3. interleave first and reversed-second
    first = head
    while second is not None:
        f_next, s_next = first.next, second.next
        first.next = second
        second.next = f_next
        first = f_next                    # type: ignore[assignment]
        second = s_next
    return head


# ===========================================================================
# 9. DUMMY-NODE REMOVAL — delete every node equal to a value
# ===========================================================================
def remove_all(head: Optional[Node], val: int) -> Optional[Node]:
    """Remove ALL nodes whose value == val; return the new head. O(n), O(1).
    A dummy before the head means even leading matches are deleted without a
    special case. Don't advance `prev` when you unlink — the next node may also
    match. Edge case: every node matches -> empty list."""
    dummy = Node(0, head)
    prev = dummy
    while prev.next is not None:
        if prev.next.val == val:
            prev.next = prev.next.next    # unlink; stay on prev to recheck
        else:
            prev = prev.next
    return dummy.next


# ===========================================================================
# Helper for building a list WITH a cycle (for Floyd's tests)
# ===========================================================================
def build_with_cycle(values: List[int], pos: int) -> Optional[Node]:
    """Build a list whose tail links back to index `pos` (-1 = no cycle)."""
    head = build(values)
    if head is None or pos < 0:
        return head
    nodes: List[Node] = []
    cur = head
    while cur is not None:
        nodes.append(cur)
        cur = cur.next
    nodes[-1].next = nodes[pos]           # close the loop
    return head


# ===========================================================================
# TESTS — normal + edge cases, run from main()
# ===========================================================================
def _test() -> None:
    # 1. reverse (iterative + recursive); empty & single
    assert to_list(reverse_iterative(build([1, 2, 3, 4]))) == [4, 3, 2, 1]
    assert to_list(reverse_iterative(build([]))) == []
    assert to_list(reverse_iterative(build([9]))) == [9]
    assert to_list(reverse_recursive(build([1, 2, 3, 4]))) == [4, 3, 2, 1]
    assert to_list(reverse_recursive(build([]))) == []
    assert to_list(reverse_recursive(build([9]))) == [9]

    # 2. find middle (odd -> exact middle; even -> 2nd middle)
    assert find_middle(build([1, 2, 3, 4, 5])).val == 3        # type: ignore[union-attr]
    assert find_middle(build([1, 2, 3, 4])).val == 3           # type: ignore[union-attr]
    assert find_middle(build([7])).val == 7                    # type: ignore[union-attr]
    assert find_middle(build([])) is None

    # 3. Floyd's cycle detection + cycle start
    assert has_cycle(build([1, 2, 3])) is False
    assert has_cycle(build([])) is False
    looped = build_with_cycle([3, 2, 0, -4], pos=1)            # tail -> index 1
    assert has_cycle(looped) is True
    assert cycle_start(looped).val == 2                        # type: ignore[union-attr]
    assert cycle_start(build([1, 2, 3])) is None               # acyclic
    self_loop = build_with_cycle([1], pos=0)                   # 1 -> itself
    assert has_cycle(self_loop) is True
    assert cycle_start(self_loop).val == 1                     # type: ignore[union-attr]

    # 4. merge two sorted lists (incl. an empty operand)
    assert to_list(merge_sorted(build([1, 3, 5]), build([2, 4, 6]))) == [1, 2, 3, 4, 5, 6]
    assert to_list(merge_sorted(build([]), build([1, 2]))) == [1, 2]
    assert to_list(merge_sorted(build([]), build([]))) == []
    assert to_list(merge_sorted(build([1, 1]), build([1]))) == [1, 1, 1]

    # 5. remove Nth from end (middle, tail, head=only node)
    assert to_list(remove_nth_from_end(build([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert to_list(remove_nth_from_end(build([1, 2, 3]), 1)) == [1, 2]   # tail
    assert to_list(remove_nth_from_end(build([1, 2, 3]), 3)) == [2, 3]   # head
    assert to_list(remove_nth_from_end(build([7]), 1)) == []             # only node

    # 6. intersection (shared tail vs none)
    common = build([8, 4, 5])
    a = Node(4, Node(1, common))          # 4 -> 1 -> 8 -> 4 -> 5
    b = Node(5, Node(6, Node(1, common))) # 5 -> 6 -> 1 -> 8 -> 4 -> 5
    assert get_intersection(a, b) is common
    assert get_intersection(build([1, 2]), build([3, 4])) is None
    assert get_intersection(None, build([1])) is None

    # 7. palindrome (odd, even, none, single, empty)
    assert is_palindrome(build([1, 2, 3, 2, 1])) is True       # odd palindrome
    assert is_palindrome(build([1, 2, 2, 1])) is True          # even palindrome
    assert is_palindrome(build([1, 2, 3])) is False
    assert is_palindrome(build([1])) is True
    assert is_palindrome(build([])) is True

    # 8. reorder list (even & odd; tiny inputs unchanged)
    assert to_list(reorder_list(build([1, 2, 3, 4]))) == [1, 4, 2, 3]
    assert to_list(reorder_list(build([1, 2, 3, 4, 5]))) == [1, 5, 2, 4, 3]
    assert to_list(reorder_list(build([1, 2]))) == [1, 2]
    assert to_list(reorder_list(build([1]))) == [1]
    assert to_list(reorder_list(build([]))) == []

    # 9. dummy-node removal (leading match, all match, none match)
    assert to_list(remove_all(build([1, 2, 6, 3, 6]), 6)) == [1, 2, 3]
    assert to_list(remove_all(build([6, 6, 6]), 6)) == []      # all removed
    assert to_list(remove_all(build([6, 1, 6]), 6)) == [1]     # leading + trailing
    assert to_list(remove_all(build([1, 2, 3]), 9)) == [1, 2, 3]  # none match


def main() -> None:
    _test()
    print("linked_list_tricks.py: all 9 patterns verified ✔")


if __name__ == "__main__":
    main()
