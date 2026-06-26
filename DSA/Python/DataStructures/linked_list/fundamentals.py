"""
Linked-list fundamentals for interviews — a real, node-based singly linked list.

Covers every operation you are likely to implement, its time complexity, and the
gotchas that cause real interview bugs. Each section is runnable and verified
with `assert`s. Run `python3 fundamentals.py` — if it exits cleanly, every
example behaved as documented.

A LINKED LIST is a chain of NODES, each holding a value and a pointer (`next`) to
the following node. There is NO contiguous memory and NO index: you reach the
k-th element only by walking from the head. That single fact explains every
complexity below — O(1) at a node you already hold, O(n) for anything you must
search for.

Three flavours worth knowing (this file implements the first):
    - Singly linked  : node has `next` only. Forward traversal. Cheapest memory.
    - Doubly linked  : node has `next` AND `prev`. O(1) delete given the node,
                       O(1) at both ends. `collections.deque` is a doubly linked
                       list under the hood (the practical interview choice).
    - Circular       : the tail's `next` points back to the head (or to some
                       node) instead of None — the basis of cycle problems.
"""

from typing import Optional, Iterator, List


# ---------------------------------------------------------------------------
# 1. The NODE — the building block. Value + pointer to the next node.
# ---------------------------------------------------------------------------
class Node:
    """A single singly-linked-list node. `next` is None at the tail."""

    __slots__ = ("val", "next")          # tiny memory win; common in interviews

    def __init__(self, val: int, next: "Optional[Node]" = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:           # handy when debugging
        return f"Node({self.val})"


# ---------------------------------------------------------------------------
# 2. The LIST — holds a `head` pointer (and a cached `size` so len is O(1)).
# ---------------------------------------------------------------------------
class LinkedList:
    """Singly linked list. Keeps `head` and a cached `_size`.

    We cache the length so `__len__` is O(1) (mirrors how Python's own
    containers store their size rather than counting on demand). A `tail`
    pointer could also be cached to make append O(1); here append walks to the
    end (O(n)) to keep the teaching code minimal — the trade-off is noted on
    `insert_tail`.
    """

    def __init__(self, values: Optional[List[int]] = None) -> None:
        self.head: Optional[Node] = None
        self._size = 0
        if values:                       # convenience builder for tests/demos
            for v in values:
                self.insert_tail(v)

    # -- size & emptiness ---------------------------------------------------
    def __len__(self) -> int:
        """O(1) — size is maintained on every insert/delete, never counted."""
        return self._size

    def is_empty(self) -> bool:
        """O(1). The canonical empty check: the head is None."""
        return self.head is None

    # -- traversal helpers --------------------------------------------------
    def __iter__(self) -> Iterator[int]:
        """Walk head -> tail yielding values. O(n)."""
        cur = self.head
        while cur is not None:
            yield cur.val
            cur = cur.next

    def to_list(self) -> List[int]:
        """Materialize values into a Python list. O(n). Used heavily in tests."""
        return list(self)

    def __repr__(self) -> str:
        return " -> ".join(str(v) for v in self) + " -> None"

    # -- insertion ----------------------------------------------------------
    def insert_head(self, val: int) -> None:
        """Prepend. O(1) — the WHOLE POINT of a linked list.
        New node's `next` is the old head; head now points at the new node.
        Order matters: build the new node pointing at the old head FIRST, then
        move head — otherwise you lose the rest of the list (see GOTCHAS)."""
        self.head = Node(val, self.head)
        self._size += 1

    def insert_tail(self, val: int) -> None:
        """Append. O(n) here — we must walk to the last node first.
        (Cache a `tail` pointer to make this O(1); deque does exactly that.)
        Edge case: empty list -> the new node becomes the head."""
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:   # stop AT the last node, not past it
                cur = cur.next
            cur.next = node
        self._size += 1

    def insert_at(self, index: int, val: int) -> None:
        """Insert so the new node ends up at position `index`. O(n).
        index 0 == insert_head; index == len == insert_tail.
        Out-of-range index raises IndexError."""
        if index < 0 or index > self._size:
            raise IndexError("index out of range")
        if index == 0:
            self.insert_head(val)
            return
        prev = self.head
        for _ in range(index - 1):        # stop at the node BEFORE the slot
            assert prev is not None
            prev = prev.next
        assert prev is not None
        prev.next = Node(val, prev.next)  # splice in: link new -> rest, prev -> new
        self._size += 1

    # -- deletion -----------------------------------------------------------
    def delete_value(self, val: int) -> bool:
        """Delete the FIRST node whose value == val. O(n). Returns whether found.
        A DUMMY (sentinel) node before the head removes the 'delete the head'
        special case — `prev` always exists, so one branch handles every node."""
        dummy = Node(0, self.head)        # dummy.next == head
        prev = dummy
        while prev.next is not None:
            if prev.next.val == val:
                prev.next = prev.next.next  # unlink: skip over the target node
                self._size -= 1
                self.head = dummy.next      # head may have changed
                return True
            prev = prev.next
        self.head = dummy.next
        return False

    def delete_at(self, index: int) -> int:
        """Delete and return the value at `index`. O(n).
        Out-of-range index raises IndexError. Uses a dummy to unify head/middle."""
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        dummy = Node(0, self.head)
        prev = dummy
        for _ in range(index):            # walk to the node BEFORE the target
            assert prev.next is not None
            prev = prev.next
        target = prev.next
        assert target is not None
        prev.next = target.next           # unlink the target
        self.head = dummy.next
        self._size -= 1
        return target.val

    # -- search & access ----------------------------------------------------
    def search(self, val: int) -> int:
        """Index of the first node with this value, or -1. O(n) — must walk."""
        idx = 0
        for v in self:
            if v == val:
                return idx
            idx += 1
        return -1

    def get(self, index: int) -> int:
        """Value at `index`. O(n) — NO random access; you walk from the head.
        This O(n) (vs an array's O(1)) is the core linked-list trade-off."""
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        cur = self.head
        for _ in range(index):
            assert cur is not None
            cur = cur.next
        assert cur is not None
        return cur.val

    # -- reverse ------------------------------------------------------------
    def reverse(self) -> None:
        """Reverse the list IN PLACE. O(n) time, O(1) space.
        Re-point each node's `next` to its predecessor while walking forward.
        You must stash `next` BEFORE overwriting it or you lose the rest."""
        prev: Optional[Node] = None
        cur = self.head
        while cur is not None:
            nxt = cur.next        # 1. remember the rest of the list
            cur.next = prev       # 2. flip this node's pointer backwards
            prev = cur            # 3. advance prev
            cur = nxt             # 4. advance cur
        self.head = prev          # prev is the old tail = new head


# ---------------------------------------------------------------------------
# 3. Per-operation verification (the docstrings above, proven)
# ---------------------------------------------------------------------------
def insertion() -> None:
    ll = LinkedList()
    assert ll.is_empty() and len(ll) == 0

    ll.insert_head(2)             # 2
    ll.insert_head(1)             # 1 -> 2          (head insert prepends)
    ll.insert_tail(3)             # 1 -> 2 -> 3     (tail insert appends)
    assert ll.to_list() == [1, 2, 3]
    assert len(ll) == 3

    ll.insert_at(0, 0)            # 0 -> 1 -> 2 -> 3   (index 0 == head)
    ll.insert_at(4, 9)            # 0 -> 1 -> 2 -> 3 -> 9 (index==len == tail)
    ll.insert_at(2, 5)            # 0 -> 1 -> 5 -> 2 -> 3 -> 9 (middle splice)
    assert ll.to_list() == [0, 1, 5, 2, 3, 9]

    try:
        ll.insert_at(99, 0)
        assert False, "expected IndexError"
    except IndexError:
        pass


def deletion() -> None:
    ll = LinkedList([1, 2, 3, 2, 4])
    assert ll.delete_value(2) is True       # first 2 removed -> 1,3,2,4
    assert ll.to_list() == [1, 3, 2, 4]
    assert ll.delete_value(99) is False     # absent value
    assert ll.to_list() == [1, 3, 2, 4]

    assert ll.delete_value(1) is True        # delete the HEAD via dummy node
    assert ll.to_list() == [3, 2, 4]

    assert ll.delete_at(0) == 3              # delete head by index
    assert ll.delete_at(1) == 4              # delete tail by index -> [2]
    assert ll.to_list() == [2]
    assert len(ll) == 1

    try:
        ll.delete_at(5)
        assert False, "expected IndexError"
    except IndexError:
        pass


def search_and_access() -> None:
    ll = LinkedList([10, 20, 30])
    assert ll.search(20) == 1
    assert ll.search(99) == -1               # sentinel for "not found"
    assert ll.get(0) == 10 and ll.get(2) == 30
    try:
        ll.get(3)
        assert False, "expected IndexError"
    except IndexError:
        pass


def traversal_and_reverse() -> None:
    ll = LinkedList([1, 2, 3, 4])
    assert list(ll) == [1, 2, 3, 4]          # __iter__
    assert repr(ll) == "1 -> 2 -> 3 -> 4 -> None"

    ll.reverse()
    assert ll.to_list() == [4, 3, 2, 1]      # O(n) time, O(1) space

    # reversing twice is the identity
    ll.reverse()
    assert ll.to_list() == [1, 2, 3, 4]

    # reverse on empty / single is a no-op
    empty = LinkedList()
    empty.reverse()
    assert empty.to_list() == []
    one = LinkedList([7])
    one.reverse()
    assert one.to_list() == [7]


# ---------------------------------------------------------------------------
# 4. GOTCHAS — the bugs that cost interviews
# ---------------------------------------------------------------------------
def gotchas() -> None:
    # (a) LOSING THE HEAD: when prepending you must point the new node at the
    #     old head BEFORE moving head. Do it backwards and you orphan the list.
    head = Node(2, Node(3))            # 2 -> 3
    #   WRONG (conceptually):  head = Node(1); head_ref = head  ... loses 2 -> 3
    new_head = Node(1)
    new_head.next = head               # link new -> old head FIRST
    head = new_head                    # THEN move head
    assert [head.val, head.next.val, head.next.next.val] == [1, 2, 3]

    # (b) OFF-BY-ONE while walking: to insert/delete you stop at the node BEFORE
    #     the target. Walking `while cur.next` lands on the last node; walking
    #     `while cur` lands on None (one step too far -> AttributeError).
    ll = LinkedList([1, 2, 3])
    cur = ll.head
    steps = 0
    while cur.next is not None:         # stops AT the tail, not past it
        cur = cur.next
        steps += 1
    assert cur.val == 3 and steps == 2  # 2 hops from head to tail of length 3

    # (c) NULL/None DEREFERENCE: reading `.next.val` on the last node crashes
    #     because `last.next is None`. ALWAYS guard `if node and node.next`.
    last = Node(5)                     # last.next is None
    safe = last.next.val if last.next is not None else None
    assert safe is None                # no crash because we guarded

    # (d) DUMMY-NODE TECHNIQUE: deleting the head is a special case (there's no
    #     predecessor). A sentinel `dummy -> head` gives every real node a
    #     predecessor, so ONE loop body handles head, middle, and tail.
    ll2 = LinkedList([1, 2, 3])
    assert ll2.delete_value(1) is True  # head deleted cleanly, no special branch
    assert ll2.to_list() == [2, 3]

    # (e) CACHED SIZE must move with the structure: every insert/delete updates
    #     `_size`, so len() stays correct and O(1). Forgetting one path is a
    #     silent bug — verify after a mixed sequence.
    ll3 = LinkedList([1, 2])
    ll3.insert_head(0)
    ll3.delete_at(2)
    assert len(ll3) == len(ll3.to_list()) == 2


def main() -> None:
    insertion()
    deletion()
    search_and_access()
    traversal_and_reverse()
    gotchas()
    print("fundamentals.py: all examples verified ✔")


if __name__ == "__main__":
    main()
