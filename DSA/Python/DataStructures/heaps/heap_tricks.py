"""
Core heap / priority-queue patterns for coding interviews — runnable & self-testing.

Every pattern below is a real, callable function (or class) — not a stub — with
its time and space complexity, the edge cases it handles, and inline `assert`
tests in `_test()`. Run `python3 heap_tricks.py`; a clean exit means all
patterns passed their tests.

The unifying idea: a heap gives you O(1) access to the current min/max and
O(log n) insert/remove, so any time a problem says "k-th largest", "top k",
"closest k", "merge k", or "running median", a heap is usually the answer —
WITHOUT fully sorting the data.

Patterns:
    1. Kth largest element          — a size-k MIN-heap of the largest seen
    2. Top-k frequent elements      — count, then size-k heap by frequency
    3. Merge k sorted lists         — heap of one front element per list
    4. Median from a data stream    — two heaps (max-heap low half, min-heap high half)
    5. K closest points to origin   — size-k MAX-heap by distance
    6. Reorganize string            — greedy: always place the most frequent char
    7. Last stone weight            — repeatedly smash the two heaviest stones
"""

import heapq
import itertools
from collections import Counter
from typing import List, Optional, Tuple


# ===========================================================================
# 1. KTH LARGEST ELEMENT  — size-k min-heap
# ===========================================================================
def kth_largest(nums: List[int], k: int) -> int:
    """The k-th largest value in nums (k counted from the top, 1-indexed).
    Keep a MIN-heap of the k largest seen so far: its root is the k-th largest.
    Time O(n log k), Space O(k) — beats sorting (O(n log n)) when k << n.
    Edge: assumes 1 <= k <= len(nums)."""
    heap: List[int] = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)        # evict the smallest -> heap holds top k
    return heap[0]                     # smallest of the k largest = k-th largest


# ===========================================================================
# 2. TOP-K FREQUENT ELEMENTS  — count, then size-k heap by frequency
# ===========================================================================
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """The k most frequent values (any order). Count frequencies, then keep a
    size-k MIN-heap keyed by frequency so the least-frequent is evicted first.
    Time O(n log k), Space O(n). Edge: k <= number of distinct values."""
    freq = Counter(nums)
    heap: List[Tuple[int, int]] = []   # (frequency, value)
    for value, count in freq.items():
        heapq.heappush(heap, (count, value))
        if len(heap) > k:
            heapq.heappop(heap)        # drop the currently least frequent
    return [value for _, value in heap]


# ===========================================================================
# 3. MERGE K SORTED LISTS  — heap of the current front of each list
# ===========================================================================
def merge_k_sorted(lists: List[List[int]]) -> List[int]:
    """Merge k already-sorted lists into one sorted list.
    Push the first element of each list, then repeatedly pop the global min and
    push the next element from the SAME list it came from. The counter avoids
    comparing values when two lists tie (and works for unorderable payloads).
    Time O(N log k) for N total elements, Space O(k) for the heap.
    Edge cases: empty outer list -> []; empty inner lists are skipped."""
    counter = itertools.count()
    heap: List[Tuple[int, int, int, int]] = []  # (value, tiebreak, list_idx, elem_idx)
    for li, lst in enumerate(lists):
        if lst:                                  # skip empty lists
            heapq.heappush(heap, (lst[0], next(counter), li, 0))

    result: List[int] = []
    while heap:
        value, _, li, ei = heapq.heappop(heap)
        result.append(value)
        if ei + 1 < len(lists[li]):              # more elements in this list?
            nxt = lists[li][ei + 1]
            heapq.heappush(heap, (nxt, next(counter), li, ei + 1))
    return result


# ===========================================================================
# 4. MEDIAN FROM A DATA STREAM  — two heaps
# ===========================================================================
class MedianFinder:
    """Maintain the running median of a stream as numbers arrive.

    Split the values into two halves:
      - `low`  : a MAX-heap (stored negated) holding the smaller half
      - `high` : a MIN-heap holding the larger half
    Invariants kept after every insert:
      - every element in `low` <= every element in `high`
      - len(low) == len(high)  OR  len(low) == len(high) + 1
    The median is then either the top of `low` (odd count) or the average of
    the two tops (even count) — both O(1) to read.

    add_num: O(log n) per insert (one push + one rebalancing push/pop).
    find_median: O(1). Space O(n)."""

    def __init__(self) -> None:
        self.low: List[int] = []       # max-heap via negation (smaller half)
        self.high: List[int] = []      # min-heap (larger half)

    def add_num(self, num: int) -> None:
        # Step 1: push onto low (max-heap), then move low's max over to high.
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        # Step 2: rebalance so low is never smaller than high (low holds the
        # extra element when the total count is odd).
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self) -> float:
        if not self.low:
            raise ValueError("no numbers added yet")
        if len(self.low) > len(self.high):
            return float(-self.low[0])             # odd count -> middle element
        return (-self.low[0] + self.high[0]) / 2.0  # even -> average of two tops


# ===========================================================================
# 5. K CLOSEST POINTS TO ORIGIN  — size-k max-heap by distance
# ===========================================================================
def k_closest_points(points: List[Tuple[int, int]], k: int) -> List[Tuple[int, int]]:
    """The k points nearest the origin (any order). Keep a size-k MAX-heap keyed
    by squared distance (no sqrt needed — it's monotonic); evict the farthest so
    the heap always holds the k closest. Time O(n log k), Space O(k).
    Edge: k >= len(points) -> all points returned."""
    heap: List[Tuple[int, int, Tuple[int, int]]] = []  # (-dist2, tiebreak, point)
    counter = itertools.count()
    for x, y in points:
        dist2 = x * x + y * y
        # Negate distance so the LARGEST distance sits at the heap root, ready
        # to be evicted when a closer point arrives.
        heapq.heappush(heap, (-dist2, next(counter), (x, y)))
        if len(heap) > k:
            heapq.heappop(heap)
    return [point for _, _, point in heap]


# ===========================================================================
# 6. REORGANIZE STRING  — greedily place the most frequent char each step
# ===========================================================================
def reorganize_string(s: str) -> str:
    """Rearrange s so no two adjacent chars are equal; "" if impossible.
    Greedy with a MAX-heap of (count, char): place the most frequent available
    char that ISN'T the one just placed, holding the previous char back one step
    so it can't be used twice in a row.
    Time O(n log a) (a = alphabet size), Space O(a).
    Edge: if any char count > (n+1)//2 it's impossible -> ""."""
    freq = Counter(s)
    heap: List[Tuple[int, str]] = [(-c, ch) for ch, c in freq.items()]
    heapq.heapify(heap)

    result: List[str] = []
    prev: Optional[Tuple[int, str]] = None     # the char placed last (held back)
    while heap:
        count, ch = heapq.heappop(heap)        # most frequent remaining
        result.append(ch)
        # We've now used one of `ch`; it becomes the held-back char for next turn.
        if prev is not None:
            heapq.heappush(heap, prev)         # release the previously held char
        count += 1                             # used one (count is negative)
        prev = (count, ch) if count != 0 else None
    out = "".join(result)
    return out if len(out) == len(s) else ""   # incomplete -> impossible


# ===========================================================================
# 7. LAST STONE WEIGHT  — smash the two heaviest repeatedly
# ===========================================================================
def last_stone_weight(stones: List[int]) -> int:
    """Repeatedly take the two heaviest stones; if unequal, the difference goes
    back. Return the weight of the last remaining stone (0 if none remain).
    A MAX-heap (via negation) gives the two heaviest in O(log n) each.
    Time O(n log n), Space O(n). Edge: [] -> 0; single stone -> itself."""
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        first = -heapq.heappop(heap)           # heaviest
        second = -heapq.heappop(heap)          # second heaviest
        if first != second:
            heapq.heappush(heap, -(first - second))   # remainder goes back
    return -heap[0] if heap else 0


# ===========================================================================
# TESTS — run via main(); cover normal + edge cases
# ===========================================================================
def _test() -> None:
    # 1. kth largest
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert kth_largest([7], 1) == 7                 # single element

    # 2. top-k frequent (order-independent -> compare as sets)
    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert set(top_k_frequent([1], 1)) == {1}
    assert set(top_k_frequent([4, 4, 5, 5, 6], 3)) == {4, 5, 6}

    # 3. merge k sorted (incl. empties and a single list)
    assert merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert merge_k_sorted([]) == []
    assert merge_k_sorted([[], [1], []]) == [1]
    assert merge_k_sorted([[2, 2], [2]]) == [2, 2, 2]   # ties on value

    # 4. median from a stream (odd & even counts)
    mf = MedianFinder()
    mf.add_num(1)
    assert mf.find_median() == 1.0                  # odd
    mf.add_num(2)
    assert mf.find_median() == 1.5                  # even -> average
    mf.add_num(3)
    assert mf.find_median() == 2.0
    mf2 = MedianFinder()
    for v in [5, 15, 1, 3]:                          # unsorted arrival order
        mf2.add_num(v)
    assert mf2.find_median() == 4.0                 # sorted: [1,3,5,15] -> (3+5)/2

    # 5. k closest points
    res = k_closest_points([(1, 3), (-2, 2)], 1)
    assert res == [(-2, 2)]                          # dist 8 < dist 10
    res2 = set(k_closest_points([(3, 3), (5, -1), (-2, 4)], 2))
    assert res2 == {(3, 3), (-2, 4)}                 # dists 18, 26, 20 -> keep 18,20
    assert set(k_closest_points([(0, 0)], 5)) == {(0, 0)}   # k > n

    # 6. reorganize string (valid + impossible)
    out = reorganize_string("aab")
    assert sorted(out) == ["a", "a", "b"]
    assert all(out[i] != out[i + 1] for i in range(len(out) - 1))
    assert reorganize_string("aaab") == ""           # impossible
    assert reorganize_string("a") == "a"             # single char

    # 7. last stone weight
    assert last_stone_weight([2, 7, 4, 1, 8, 1]) == 1
    assert last_stone_weight([1]) == 1
    assert last_stone_weight([]) == 0
    assert last_stone_weight([3, 3]) == 0            # equal stones cancel


def main() -> None:
    _test()
    print("heap_tricks.py: all 7 patterns verified ✔")


if __name__ == "__main__":
    main()
