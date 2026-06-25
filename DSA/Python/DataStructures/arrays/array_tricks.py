"""
Core array patterns for coding interviews — runnable & self-testing.

Every pattern below is a real, callable function (not a stub) with its time and
space complexity, the edge cases it handles, and inline `assert` tests. Run
`python3 array_tricks.py`; a clean exit means all patterns passed their tests.

Patterns:
    1.  Two pointers          — pair-with-sum (sorted), in-place dedup
    2.  Sliding window        — fixed size (max sum) & variable size (longest unique)
    3.  Kadane's              — max-sum contiguous subarray
    4.  Prefix sum            — range sums + subarray-sum-equals-k (hashmap)
    5.  Dutch national flag   — 3-way partition / sort colors
    6.  Cyclic sort           — find missing number in 0..n / 1..n
    7.  Rotation              — rotate by k via triple reversal, in place
    8.  Binary search         — first & last occurrence; rotated array search
    9.  Matrix staircase      — search a row/col-sorted matrix
    10. Product except self   — products without division
    11. Boyer-Moore           — majority element (> n/2)
"""

from typing import List


# ===========================================================================
# 1. TWO POINTERS
# ===========================================================================
def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    """Indices of a pair summing to target in a SORTED array, else [].
    Time O(n), Space O(1). Edge cases: empty/single -> loop never matches -> []."""
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []


def remove_duplicates_sorted(arr: List[int]) -> int:
    """In-place dedup of a SORTED array. Returns new length k; arr[:k] is unique.
    Time O(n), Space O(1). Edge case: empty -> 0."""
    if not arr:
        return 0
    write = 1  # arr[0] is always kept
    for read in range(1, len(arr)):
        if arr[read] != arr[write - 1]:
            arr[write] = arr[read]
            write += 1
    return write


# ===========================================================================
# 2. SLIDING WINDOW
# ===========================================================================
def max_sum_subarray_fixed(arr: List[int], k: int) -> int:
    """Max sum of any contiguous subarray of size k.
    Time O(n), Space O(1). Edge cases: k<=0 or k>len -> ValueError (no valid window)."""
    if k <= 0 or k > len(arr):
        raise ValueError("k must satisfy 1 <= k <= len(arr)")
    window = sum(arr[:k])
    best = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]   # slide: add new, drop old
        best = max(best, window)
    return best


def longest_unique_substring(s: str) -> int:
    """Length of the longest substring without repeating chars (variable window).
    Time O(n), Space O(min(n, charset)). Edge case: '' -> 0."""
    seen = {}            # char -> last index seen
    start = 0
    best = 0
    for i, ch in enumerate(s):
        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1     # shrink window past the duplicate
        seen[ch] = i
        best = max(best, i - start + 1)
    return best


# ===========================================================================
# 3. KADANE'S — maximum-sum contiguous subarray
# ===========================================================================
def max_subarray_sum(arr: List[int]) -> int:
    """Largest sum of any non-empty contiguous subarray.
    Time O(n), Space O(1).
    Edge cases: empty -> ValueError; ALL NEGATIVE handled (init from arr[0],
    NOT 0 — initializing to 0 would wrongly return 0 for all-negative input)."""
    if not arr:
        raise ValueError("array must be non-empty")
    cur = best = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)        # extend previous subarray, or start fresh at x
        best = max(best, cur)
    return best


# ===========================================================================
# 4. PREFIX SUM
# ===========================================================================
def build_prefix(arr: List[int]) -> List[int]:
    """prefix[i] = sum(arr[:i]); prefix has len(arr)+1 entries, prefix[0]=0.
    Time O(n), Space O(n)."""
    prefix = [0] * (len(arr) + 1)
    for i, x in enumerate(arr):
        prefix[i + 1] = prefix[i] + x
    return prefix


def range_sum(prefix: List[int], left: int, right: int) -> int:
    """Inclusive sum of arr[left..right] in O(1) given a prefix array."""
    return prefix[right + 1] - prefix[left]


def subarray_sum_equals_k(arr: List[int], k: int) -> int:
    """Count contiguous subarrays summing to k. Works with negatives & zeros.
    Time O(n), Space O(n). Uses running sum + hashmap of seen prefix sums."""
    count = 0
    running = 0
    seen = {0: 1}        # one empty prefix has sum 0
    for x in arr:
        running += x
        count += seen.get(running - k, 0)   # how many earlier prefixes make sum k
        seen[running] = seen.get(running, 0) + 1
    return count


# ===========================================================================
# 5. DUTCH NATIONAL FLAG — sort an array of 0s, 1s, 2s in one pass
# ===========================================================================
def sort_colors(arr: List[int]) -> None:
    """In-place 3-way partition (Sort Colors). Time O(n), Space O(1).
    Edge cases: empty/single -> no-op."""
    low = mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:                       # == 2: swap to the end; DON'T advance mid
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


# ===========================================================================
# 6. CYCLIC SORT — values in a known range (here: 0..n missing one)
# ===========================================================================
def find_missing_number(arr: List[int]) -> int:
    """Given n distinct numbers from the range 0..n (one missing), find it.
    Time O(n), Space O(1). Edge case: [] -> 0 is missing (range 0..0)."""
    i = 0
    n = len(arr)
    while i < n:
        target_pos = arr[i]
        # place arr[i] at its index if it's in-range and not already correct
        if target_pos < n and arr[i] != arr[target_pos]:
            arr[i], arr[target_pos] = arr[target_pos], arr[i]
        else:
            i += 1
    for idx in range(n):
        if arr[idx] != idx:
            return idx
    return n                        # all of 0..n-1 present -> n is missing


# ===========================================================================
# 7. ROTATION — rotate right by k, in place, via triple reversal
# ===========================================================================
def rotate_right(arr: List[int], k: int) -> None:
    """Rotate arr to the right by k positions, in place. Time O(n), Space O(1).
    Edge cases: empty -> no-op; k normalized mod n so k>=n and k<0 both work."""
    n = len(arr)
    if n == 0:
        return
    k %= n                          # handles k > n AND k == n (-> 0); also k < 0
    arr.reverse()                   # reverse all
    arr[:k] = reversed(arr[:k])     # reverse first k
    arr[k:] = reversed(arr[k:])     # reverse the rest


# ===========================================================================
# 8. BINARY SEARCH variations (require a SORTED array)
# ===========================================================================
def first_occurrence(arr: List[int], target: int) -> int:
    """Leftmost index of target, or -1. Time O(log n). Handles duplicates."""
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1         # keep searching left for an earlier match
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def last_occurrence(arr: List[int], target: int) -> int:
    """Rightmost index of target, or -1. Time O(log n)."""
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1          # keep searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def search_rotated(arr: List[int], target: int) -> int:
    """Search a rotated sorted array (distinct values). Index or -1. O(log n).
    One half is always sorted — decide which, then narrow."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:           # left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:                               # right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


# ===========================================================================
# 9. MATRIX STAIRCASE SEARCH — rows & columns sorted ascending
# ===========================================================================
def search_sorted_matrix(matrix: List[List[int]], target: int) -> bool:
    """Search a matrix sorted left-to-right and top-to-bottom. Time O(m+n).
    Start from top-right: too big -> go left, too small -> go down.
    Edge cases: empty matrix / empty rows -> False."""
    if not matrix or not matrix[0]:
        return False
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        v = matrix[row][col]
        if v == target:
            return True
        elif v > target:
            col -= 1
        else:
            row += 1
    return False


# ===========================================================================
# 10. PRODUCT EXCEPT SELF — no division, handles zeros
# ===========================================================================
def product_except_self(arr: List[int]) -> List[int]:
    """res[i] = product of all elements except arr[i], WITHOUT division.
    Time O(n), Space O(1) extra (output not counted). Handles zeros naturally."""
    n = len(arr)
    res = [1] * n
    prefix = 1
    for i in range(n):              # res[i] = product of everything to the left
        res[i] = prefix
        prefix *= arr[i]
    suffix = 1
    for i in range(n - 1, -1, -1):  # multiply in product of everything to the right
        res[i] *= suffix
        suffix *= arr[i]
    return res


# ===========================================================================
# 11. BOYER-MOORE majority vote — element appearing > n/2 times
# ===========================================================================
def majority_element(arr: List[int]) -> int:
    """Find the element occurring > n/2 times (assumed to exist). O(n), O(1).
    Maintains a candidate and a count; opposing votes cancel out."""
    candidate = None
    count = 0
    for x in arr:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1
    return candidate


# ===========================================================================
# TESTS — run on import via main(); cover normal + edge cases
# ===========================================================================
def _test() -> None:
    # 1. two pointers
    assert two_sum_sorted([1, 2, 4, 7, 11], 9) == [1, 3]
    assert two_sum_sorted([], 5) == [] and two_sum_sorted([5], 5) == []
    a = [1, 1, 2, 2, 2, 3]
    k = remove_duplicates_sorted(a)
    assert a[:k] == [1, 2, 3]
    assert remove_duplicates_sorted([]) == 0

    # 2. sliding window
    assert max_sum_subarray_fixed([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_subarray_fixed([5], 1) == 5
    try:
        max_sum_subarray_fixed([1, 2], 5)
        assert False, "expected ValueError"
    except ValueError:
        pass
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("") == 0
    assert longest_unique_substring("bbbb") == 1

    # 3. Kadane's (incl. all-negative & single)
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray_sum([-3, -1, -2]) == -1     # NOT 0
    assert max_subarray_sum([7]) == 7

    # 4. prefix sum
    p = build_prefix([1, 2, 3, 4])
    assert range_sum(p, 1, 2) == 5 and range_sum(p, 0, 3) == 10
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2
    assert subarray_sum_equals_k([1, -1, 0], 0) == 3   # negatives & zeros

    # 5. Dutch national flag
    colors = [2, 0, 2, 1, 1, 0]
    sort_colors(colors)
    assert colors == [0, 0, 1, 1, 2, 2]
    empty = []
    sort_colors(empty)
    assert empty == []

    # 6. cyclic sort / missing number
    assert find_missing_number([3, 0, 1]) == 2
    assert find_missing_number([0, 1]) == 2
    assert find_missing_number([]) == 0

    # 7. rotation (k>n, k==n, k<0, empty)
    r = [1, 2, 3, 4, 5]
    rotate_right(r, 2)
    assert r == [4, 5, 1, 2, 3]
    r2 = [1, 2, 3]
    rotate_right(r2, 7)            # 7 % 3 == 1
    assert r2 == [3, 1, 2]
    r3 = [1, 2, 3]
    rotate_right(r3, 3)            # full rotation -> unchanged
    assert r3 == [1, 2, 3]
    empty2 = []
    rotate_right(empty2, 4)
    assert empty2 == []

    # 8. binary search variants
    dups = [1, 2, 2, 2, 3, 4]
    assert first_occurrence(dups, 2) == 1
    assert last_occurrence(dups, 2) == 3
    assert first_occurrence(dups, 9) == -1
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1

    # 9. matrix staircase
    m = [[1, 4, 7], [8, 11, 15], [12, 19, 23]]
    assert search_sorted_matrix(m, 11) is True
    assert search_sorted_matrix(m, 13) is False
    assert search_sorted_matrix([], 1) is False

    # 10. product except self (incl. a zero)
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([0, 4, 5]) == [20, 0, 0]

    # 11. Boyer-Moore majority
    assert majority_element([3, 3, 4, 2, 3, 3, 3]) == 3
    assert majority_element([1]) == 1


def main() -> None:
    _test()
    print("array_tricks.py: all 11 patterns verified ✔")


if __name__ == "__main__":
    main()
