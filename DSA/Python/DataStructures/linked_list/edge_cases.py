"""
Linked-list edge cases — the inputs that break naive solutions, with proof.

Each function demonstrates ONE edge-case category: a naive approach that fails
and the robust version that doesn't. Run `python3 edge_cases.py`; a clean exit
means every "robust" version handled its edge case as documented.

Use this as a pre-submission checklist: walk your solution through each case.
A linked-list solution is correct only when it survives ALL of:
empty, single, two-node, cycle-present, even/odd length, head vs tail deletion,
and the cases that demand a dummy node.
"""

from typing import Optional, List


# ---------------------------------------------------------------------------
# Minimal node + helpers so each case reads in terms of Python lists.
# ---------------------------------------------------------------------------
class Node:
    __slots__ = ("val", "next")

    def __init__(self, val: int, next: "Optional[Node]" = None) -> None:
        self.val = val
        self.next = next


def build(values: List[int]) -> Optional[Node]:
    head: Optional[Node] = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def to_list(head: Optional[Node]) -> List[int]:
    out: List[int] = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


# ---------------------------------------------------------------------------
# 1. EMPTY LIST (head is None) — the most common crash. Anything that reads
#    head.val or head.next without a guard explodes on None.
# ---------------------------------------------------------------------------
def empty_list() -> None:
    def naive_first(head):            # crashes on None
        return head.val

    def robust_first(head):           # explicit contract for empty input
        if head is None:
            return None
        return head.val

    assert robust_first(build([])) is None
    assert robust_first(build([5])) == 5
    try:
        naive_first(build([]))
        assert False
    except AttributeError:
        pass                          # exactly the None-deref bug we avoid


# ---------------------------------------------------------------------------
# 2. SINGLE NODE — loops that look at `head.next` may never enter, and
#    fast/slow must terminate immediately rather than overstep.
# ---------------------------------------------------------------------------
def single_node() -> None:
    def find_middle(head):            # fast/slow; must handle len 1
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    mid = find_middle(build([42]))
    assert mid is not None and mid.val == 42       # the only node IS the middle
    assert find_middle(build([])) is None          # and empty stays None


# ---------------------------------------------------------------------------
# 3. TWO NODES — the smallest case where pointers actually move; classic
#    off-by-one territory for reverse, swap, and middle.
# ---------------------------------------------------------------------------
def two_nodes() -> None:
    def reverse(head):                # iterative reverse
        prev = None
        cur = head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    assert to_list(reverse(build([1, 2]))) == [2, 1]
    assert to_list(reverse(build([1]))) == [1]     # single unchanged
    assert to_list(reverse(build([]))) == []       # empty unchanged


# ---------------------------------------------------------------------------
# 4. CYCLE PRESENT — a length-counting / "walk to None" loop runs forever.
#    Floyd's tortoise & hare terminates; naive traversal must not be used.
# ---------------------------------------------------------------------------
def cycle_present() -> None:
    def has_cycle(head):              # robust: bounded by Floyd
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    # build 1 -> 2 -> 3 -> back to node 2
    a, b, c = Node(1), Node(2), Node(3)
    a.next, b.next, c.next = b, c, b
    assert has_cycle(a) is True
    assert has_cycle(build([1, 2, 3])) is False    # acyclic terminates normally
    # A naive `while head: head = head.next` on `a` would never stop — that's
    # the bug; we don't call it, we rely on Floyd's bounded two-pointer walk.


# ---------------------------------------------------------------------------
# 5. EVEN vs ODD LENGTH (middle) — fast/slow returns different "middles"; you
#    must know which one your problem wants. Off-by-one here silently misreorders.
# ---------------------------------------------------------------------------
def even_odd_middle() -> None:
    def middle_second(head):          # even -> SECOND middle (LeetCode default)
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def middle_first(head):           # even -> FIRST middle (start fast ahead)
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    assert middle_second(build([1, 2, 3])).val == 2     # odd: same either way
    assert middle_second(build([1, 2, 3, 4])).val == 3  # even: 2nd middle
    assert middle_first(build([1, 2, 3, 4])).val == 2   # even: 1st middle


# ---------------------------------------------------------------------------
# 6. DELETING HEAD vs TAIL — head has no predecessor; tail's `next` is None.
#    Naive "find prev, prev.next = prev.next.next" has no prev for the head.
# ---------------------------------------------------------------------------
def delete_head_vs_tail() -> None:
    def naive_delete(head, val):      # FAILS to delete the head (no prev)
        cur = head
        while cur is not None and cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
                return head
            cur = cur.next
        return head                   # head match is silently ignored

    def robust_delete(head, val):     # dummy node -> head has a predecessor
        dummy = Node(0, head)
        prev = dummy
        while prev.next is not None:
            if prev.next.val == val:
                prev.next = prev.next.next
                break
            prev = prev.next
        return dummy.next

    # naive misses the HEAD...
    assert to_list(naive_delete(build([1, 2, 3]), 1)) == [1, 2, 3]   # bug!
    # ...robust deletes head and tail correctly
    assert to_list(robust_delete(build([1, 2, 3]), 1)) == [2, 3]     # head
    assert to_list(robust_delete(build([1, 2, 3]), 3)) == [1, 2]     # tail


# ---------------------------------------------------------------------------
# 7. DUMMY-NODE NEED — operations whose result head differs from the input
#    head (merge, delete-head, remove-Nth-that-is-head). Without a sentinel you
#    write a branch for "is it the first node?" everywhere and miss one.
# ---------------------------------------------------------------------------
def dummy_node_need() -> None:
    def merge(a, b):                  # dummy makes the "first appended" case normal
        dummy = Node(0)
        tail = dummy
        while a is not None and b is not None:
            if a.val <= b.val:
                tail.next, a = a, a.next
            else:
                tail.next, b = b, b.next
            tail = tail.next
        tail.next = a if a is not None else b
        return dummy.next             # the real head is whatever landed first

    assert to_list(merge(build([1, 4]), build([2, 3]))) == [1, 2, 3, 4]
    assert to_list(merge(build([]), build([1]))) == [1]    # empty operand
    assert to_list(merge(build([]), build([]))) == []      # both empty


def main() -> None:
    empty_list()
    single_node()
    two_nodes()
    cycle_present()
    even_odd_middle()
    delete_head_vs_tail()
    dummy_node_need()
    print("edge_cases.py: all 7 edge-case categories verified ✔")


if __name__ == "__main__":
    main()
