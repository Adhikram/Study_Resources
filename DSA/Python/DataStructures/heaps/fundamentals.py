"""
Heap / priority-queue fundamentals for interviews — Python `heapq`.

Covers every `heapq` operation you are likely to use, its time complexity, and
the gotchas that cause real interview bugs. Each section is runnable and
verified with `assert`s. Run `python3 fundamentals.py` — if it exits cleanly,
every example behaved as documented.

A binary heap is a COMPLETE BINARY TREE stored in a plain list: for the node at
index `i`, its children live at `2i+1` and `2i+2` and its parent at `(i-1)//2`.
The heap property — every parent <= its children (min-heap) — guarantees the
smallest element is always at index 0.

KEY FACT: Python's `heapq` is a MIN-heap only. There is no max-heap flag. For a
max-heap you negate values (or wrap them) — see `max_heap_via_negation` below,
and `max_heap.py` in this folder for a full from-scratch class.
"""

import heapq
import itertools
from typing import List, Tuple


# ---------------------------------------------------------------------------
# 1. The index math — parent/child relationships in the array layout
# ---------------------------------------------------------------------------
def index_math() -> None:
    # A heap is just a list. The tree shape is implied by the indices.
    #
    #            index 0
    #           /       \
    #       index 1     index 2
    #       /    \       /
    #    idx 3  idx 4  idx 5
    #
    # parent(i)      = (i - 1) // 2
    # left_child(i)  = 2*i + 1
    # right_child(i) = 2*i + 2
    parent = lambda i: (i - 1) // 2
    left = lambda i: 2 * i + 1
    right = lambda i: 2 * i + 2

    assert left(0) == 1 and right(0) == 2
    assert parent(1) == 0 and parent(2) == 0
    assert left(2) == 5 and right(2) == 6
    assert parent(5) == 2 and parent(6) == 2
    # The last non-leaf node is at index n//2 - 1 (used by bottom-up heapify).
    n = 7
    assert n // 2 - 1 == 2


# ---------------------------------------------------------------------------
# 2. push / pop / peek — the core min-heap operations
# ---------------------------------------------------------------------------
def push_pop_peek() -> None:
    heap: List[int] = []
    for x in [5, 1, 3, 10, 2]:
        heapq.heappush(heap, x)        # O(log n) — sift the new leaf UP
    # heap[0] is ALWAYS the minimum. The rest is NOT sorted — see gotchas().
    assert heap[0] == 1                # peek = heap[0], O(1)

    # heappop removes & returns the smallest, O(log n) — move last leaf to root,
    # then sift it DOWN.
    out = [heapq.heappop(heap) for _ in range(len(heap))]
    assert out == [1, 2, 3, 5, 10]     # popping repeatedly yields sorted order


# ---------------------------------------------------------------------------
# 3. heapify — turn an arbitrary list into a heap in O(n), IN PLACE
# ---------------------------------------------------------------------------
def heapify_demo() -> None:
    data = [5, 1, 3, 10, 2]
    heapq.heapify(data)                # O(n), not O(n log n) — see COMPLEXITY.md
    assert data[0] == 1                # min bubbled to the front
    # Building by n pushes is O(n log n); heapify is the cheaper way to start.
    assert sorted(data) == [1, 2, 3, 5, 10]   # same multiset, just reordered


# ---------------------------------------------------------------------------
# 4. heappushpop / heapreplace — fused push+pop, one sift instead of two
# ---------------------------------------------------------------------------
def push_pop_combos() -> None:
    # heappushpop(h, x): push x THEN pop the smallest. If x is the new smallest,
    # x comes straight back out and the heap is untouched.
    h = [2, 4, 6]
    heapq.heapify(h)
    assert heapq.heappushpop(h, 5) == 2   # 5 pushed, then 2 (the min) popped
    assert h[0] == 4

    h2 = [2, 4, 6]
    heapq.heapify(h2)
    assert heapq.heappushpop(h2, 1) == 1  # 1 is smaller than every element ->
    assert h2 == [2, 4, 6]                # popped immediately, heap unchanged

    # heapreplace(h, x): pop the smallest FIRST, then push x. Returns the old
    # min even if x is smaller. Heap must be non-empty.
    h3 = [2, 4, 6]
    heapq.heapify(h3)
    assert heapq.heapreplace(h3, 1) == 2  # pops 2, then pushes 1
    assert h3[0] == 1
    # Both are O(log n) and do ONE sift, vs heappush+heappop doing two.


# ---------------------------------------------------------------------------
# 5. Max-heap via negation — heapq has no max-heap; negate on the way in & out
# ---------------------------------------------------------------------------
def max_heap_via_negation() -> None:
    heap: List[int] = []
    for x in [5, 1, 3, 10, 2]:
        heapq.heappush(heap, -x)       # store negatives
    assert -heap[0] == 10              # the negated min == the real max

    largest = [-heapq.heappop(heap) for _ in range(len(heap))]
    assert largest == [10, 5, 3, 2, 1]   # descending order

    # Negatives in the data are fine — negation is just sign flip, see edge_cases.
    h2: List[int] = []
    for x in [-5, -1, -8]:
        heapq.heappush(h2, -x)
    assert -h2[0] == -1                # max of [-5,-1,-8] is -1


# ---------------------------------------------------------------------------
# 6. Tuple-priority entries — a priority queue keyed by an explicit priority
# ---------------------------------------------------------------------------
def tuple_priority() -> None:
    # Push (priority, payload). Tuples compare lexicographically: priority first.
    pq: List[Tuple[int, str]] = []
    heapq.heappush(pq, (2, "medium"))
    heapq.heappush(pq, (1, "high"))     # smaller priority number == higher prio
    heapq.heappush(pq, (3, "low"))
    assert heapq.heappop(pq) == (1, "high")
    assert heapq.heappop(pq) == (2, "medium")

    # For a MAX-priority queue, negate the priority field:
    maxpq: List[Tuple[int, str]] = []
    heapq.heappush(maxpq, (-2, "medium"))
    heapq.heappush(maxpq, (-5, "highest"))
    assert heapq.heappop(maxpq)[1] == "highest"


# ---------------------------------------------------------------------------
# 7. The (priority, counter, item) STABILITY pattern — the most important idiom
# ---------------------------------------------------------------------------
def stable_priority_queue() -> None:
    # PROBLEM: if two entries tie on priority, Python compares the NEXT tuple
    # field — the payload. If the payload is unorderable (a dict, or two objects
    # without __lt__), that raises TypeError. See gotchas() for the crash.
    #
    # FIX: insert a monotonically increasing counter BETWEEN priority and item.
    # The counter is unique, so it breaks every tie before the item is reached,
    # and it preserves FIFO order among equal priorities (a stable PQ).
    counter = itertools.count()        # 0, 1, 2, ...  unique & increasing
    pq: List[Tuple[int, int, dict]] = []

    def push(priority: int, item: dict) -> None:
        heapq.heappush(pq, (priority, next(counter), item))

    push(1, {"task": "a"})
    push(1, {"task": "b"})             # same priority as "a" — counter decides
    push(0, {"task": "c"})

    assert heapq.heappop(pq)[2]["task"] == "c"   # priority 0 first
    assert heapq.heappop(pq)[2]["task"] == "a"   # tie -> earlier counter wins
    assert heapq.heappop(pq)[2]["task"] == "b"   # FIFO preserved


# ---------------------------------------------------------------------------
# 8. nlargest / nsmallest — top-k without managing a heap yourself
# ---------------------------------------------------------------------------
def nlargest_nsmallest() -> None:
    data = [5, 1, 3, 10, 2, 8]
    assert heapq.nlargest(3, data) == [10, 8, 5]    # descending
    assert heapq.nsmallest(3, data) == [1, 2, 3]    # ascending

    # With a key, like sorted(): find the 2 longest words.
    words = ["a", "bbbb", "cc", "ddd"]
    assert heapq.nlargest(2, words, key=len) == ["bbbb", "ddd"]

    # Complexity: O(n log k) for small k — heapq keeps a size-k heap internally,
    # cheaper than sorting all n (O(n log n)) when k << n. For k == 1 it's just
    # min()/max(); for k near n, sorting is simpler.
    assert heapq.nlargest(1, data) == [max(data)]


# ---------------------------------------------------------------------------
# 9. merge — lazily merge multiple SORTED inputs into one sorted stream
# ---------------------------------------------------------------------------
def merge_demo() -> None:
    a = [1, 4, 7]
    b = [2, 3, 8]
    c = [0, 5, 6]
    merged = list(heapq.merge(a, b, c))             # O(total log k) streaming
    assert merged == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # heapq.merge returns an ITERATOR and never builds the inputs in memory —
    # ideal for merging k sorted files/streams. See heap_tricks.merge_k_sorted.


# ---------------------------------------------------------------------------
# 10. GOTCHAS — the bugs that cost interviews
# ---------------------------------------------------------------------------
def gotchas() -> None:
    # (a) heapq is MIN-ONLY. There is no reverse=True. Forgetting this and
    #     expecting heappop to give the max is the #1 heap bug. Negate for max.
    h = [3, 1, 2]
    heapq.heapify(h)
    assert heapq.heappop(h) == 1       # smallest, NOT largest

    # (b) heap[0] is the min, but the REST of the list is NOT sorted. Never
    #     assume heap[1] is the 2nd smallest, or that you can read it in order.
    h2 = [5, 1, 3, 10, 2]
    heapq.heapify(h2)
    assert h2[0] == 1
    assert h2 != sorted(h2)            # the array order is heap order, not sorted

    # (c) Comparing UNORDERABLE payloads raises TypeError. On a priority tie,
    #     Python falls through to comparing the next field. If that's a dict (or
    #     any type without __lt__), it crashes. Use the counter tiebreaker.
    bad: List[Tuple[int, dict]] = []
    heapq.heappush(bad, (1, {"x": 1}))
    try:
        heapq.heappush(bad, (1, {"y": 2}))   # tie on 1 -> compares the dicts
        assert False, "expected TypeError"
    except TypeError:
        pass                           # '<' not supported between dicts

    # The robust version inserts a unique counter between priority and payload:
    counter = itertools.count()
    good: List[Tuple[int, int, dict]] = []
    heapq.heappush(good, (1, next(counter), {"x": 1}))
    heapq.heappush(good, (1, next(counter), {"y": 2}))   # counter breaks the tie
    assert len(good) == 2              # no crash

    # (d) heapq operates on a PLAIN list and MUTATES IT IN PLACE. After
    #     heapify/heappush, the original list IS the heap — its order changed.
    original = [3, 1, 2]
    heapq.heapify(original)
    assert original[0] == 1            # the caller's list was reordered

    # (e) Popping from an EMPTY heap raises IndexError (not a clean sentinel).
    try:
        heapq.heappop([])
        assert False, "expected IndexError"
    except IndexError:
        pass                           # always guard `if heap:` before popping


def main() -> None:
    index_math()
    push_pop_peek()
    heapify_demo()
    push_pop_combos()
    max_heap_via_negation()
    tuple_priority()
    stable_priority_queue()
    nlargest_nsmallest()
    merge_demo()
    gotchas()
    print("fundamentals.py: all examples verified ✔")


if __name__ == "__main__":
    main()
