"""
Heap edge cases — the inputs that break naive solutions, with runnable proof.

Each function demonstrates ONE edge-case category: a naive approach that fails
and the robust version that doesn't. Run `python3 edge_cases.py`; a clean exit
means every "robust" version handled its edge case as documented.

Use this as a pre-submission checklist: walk your heap solution through each case.
"""

import heapq
import itertools
from typing import List, Optional, Tuple


# ---------------------------------------------------------------------------
# 1. EMPTY HEAP POP — heappop on [] raises IndexError, not a clean sentinel.
# ---------------------------------------------------------------------------
def empty_heap_pop() -> None:
    def naive_pop(heap):              # crashes on an empty heap
        return heapq.heappop(heap)

    def robust_pop(heap):             # explicit contract for empty input
        if not heap:
            return None
        return heapq.heappop(heap)

    assert robust_pop([]) is None
    h = [3, 1, 2]
    heapq.heapify(h)
    assert robust_pop(h) == 1
    try:
        naive_pop([])
        assert False
    except IndexError:
        pass                          # this is exactly the bug we avoid


# ---------------------------------------------------------------------------
# 2. k > n — asking for more elements than exist. Clamp k, don't over-pop.
# ---------------------------------------------------------------------------
def k_larger_than_n() -> None:
    def naive_k_largest(nums, k):     # pops k times -> IndexError when k > n
        heap = []
        for x in nums:
            heapq.heappush(heap, -x)
        return [-heapq.heappop(heap) for _ in range(k)]

    def robust_k_largest(nums, k):    # heapq.nlargest clamps k to len(nums)
        return heapq.nlargest(k, nums)

    assert robust_k_largest([3, 1, 2], 5) == [3, 2, 1]   # only 3 exist -> 3 back
    try:
        naive_k_largest([3, 1, 2], 5)
        assert False
    except IndexError:
        pass


# ---------------------------------------------------------------------------
# 3. k == 0 — degenerate "top zero". Must return empty, not crash or return all.
# ---------------------------------------------------------------------------
def k_equals_zero() -> None:
    def k_largest(nums, k):
        return heapq.nlargest(k, nums)

    assert k_largest([3, 1, 2], 0) == []   # nlargest(0, ...) is well-defined: []

    # A size-k heap loop must also behave: with k == 0 nothing is ever kept.
    def kth_largest_or_none(nums, k):
        if k <= 0 or k > len(nums):
            return None               # guard the degenerate / impossible cases
        heap: List[int] = []
        for x in nums:
            heapq.heappush(heap, x)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

    assert kth_largest_or_none([3, 1, 2], 0) is None


# ---------------------------------------------------------------------------
# 4. DUPLICATES — heaps handle equal keys fine; counts/ordering must not assume
#    uniqueness. heappop yields every duplicate, not a deduped stream.
# ---------------------------------------------------------------------------
def duplicates() -> None:
    h: List[int] = []
    for x in [5, 5, 5, 1, 1]:
        heapq.heappush(h, x)
    popped = [heapq.heappop(h) for _ in range(len(h))]
    assert popped == [1, 1, 5, 5, 5]   # all duplicates emitted in sorted order

    # nlargest/nsmallest keep duplicates too — they are not set operations.
    assert heapq.nsmallest(3, [1, 1, 1, 2]) == [1, 1, 1]


# ---------------------------------------------------------------------------
# 5. TIE-BREAKING WITH UNORDERABLE PAYLOADS — the counter trick.
#    On a priority tie Python compares the next tuple field; an unorderable
#    payload (dict / custom object) then raises TypeError.
# ---------------------------------------------------------------------------
def unorderable_payload() -> None:
    def naive_push(heap, priority, payload):     # crashes on a priority tie
        heapq.heappush(heap, (priority, payload))

    def robust_push(heap, priority, payload, counter):
        heapq.heappush(heap, (priority, next(counter), payload))  # counter breaks ties

    bad: List[Tuple[int, dict]] = []
    naive_push(bad, 1, {"a": 1})
    try:
        naive_push(bad, 1, {"b": 2})             # tie on 1 -> compares two dicts
        assert False
    except TypeError:
        pass                                     # '<' not supported for dicts

    counter = itertools.count()
    good: List[Tuple[int, int, dict]] = []
    robust_push(good, 1, {"a": 1}, counter)
    robust_push(good, 1, {"b": 2}, counter)      # no crash: counter decides order
    first = heapq.heappop(good)
    assert first[2] == {"a": 1}                  # FIFO among equal priorities


# ---------------------------------------------------------------------------
# 6. SINGLE ELEMENT — peek and pop must work when the heap has exactly one item.
# ---------------------------------------------------------------------------
def single_element() -> None:
    h = [42]
    heapq.heapify(h)
    assert h[0] == 42                 # peek
    assert heapq.heappop(h) == 42     # pop the only element
    assert h == []                    # now empty

    # heapreplace requires a NON-EMPTY heap — single element is the boundary.
    h2 = [5]
    assert heapq.heapreplace(h2, 9) == 5
    assert h2 == [9]


# ---------------------------------------------------------------------------
# 7. MAX-HEAP NEGATION WITH NEGATIVES — double-negation must round-trip exactly.
# ---------------------------------------------------------------------------
def max_heap_negation_with_negatives() -> None:
    def push_max(heap, x):
        heapq.heappush(heap, -x)      # store the negation

    def pop_max(heap):
        return -heapq.heappop(heap)   # negate back on the way out

    heap: List[int] = []
    for x in [-5, -1, -8, 0, -3]:
        push_max(heap, x)
    # Max of [-5, -1, -8, 0, -3] is 0; order should be descending.
    assert pop_max(heap) == 0
    assert pop_max(heap) == -1
    assert pop_max(heap) == -3
    assert pop_max(heap) == -5
    assert pop_max(heap) == -8        # the most negative comes out last

    # The sign flips cancel exactly even for the all-negative case.
    single: List[int] = []
    push_max(single, -7)
    assert pop_max(single) == -7


def main() -> None:
    empty_heap_pop()
    k_larger_than_n()
    k_equals_zero()
    duplicates()
    unorderable_payload()
    single_element()
    max_heap_negation_with_negatives()
    print("edge_cases.py: all 7 edge-case categories verified ✔")


if __name__ == "__main__":
    main()
