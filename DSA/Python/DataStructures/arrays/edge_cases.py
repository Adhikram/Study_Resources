"""
Array edge cases — the inputs that break naive solutions, with runnable proof.

Each function demonstrates ONE edge-case category: a naive approach that fails
and the robust version that doesn't. Run `python3 edge_cases.py`; a clean exit
means every "robust" version handled its edge case as documented.

Use this as a pre-submission checklist: walk your solution through each case.
"""

from typing import List


# ---------------------------------------------------------------------------
# 1. EMPTY ARRAY — the most common crash. Anything that does arr[0] or
#    len(arr)-1 indexing must guard against [].
# ---------------------------------------------------------------------------
def empty_array() -> None:
    def naive_max(arr):           # crashes on []
        m = arr[0]
        for x in arr:
            m = max(m, x)
        return m

    def robust_max(arr):          # explicit contract for empty input
        if not arr:
            return None
        return max(arr)

    assert robust_max([]) is None
    assert robust_max([3, 1, 2]) == 3
    try:
        naive_max([])
        assert False
    except IndexError:
        pass                      # this is exactly the bug we avoid


# ---------------------------------------------------------------------------
# 2. SINGLE ELEMENT — two-pointer / windowing loops may never execute.
# ---------------------------------------------------------------------------
def single_element() -> None:
    def is_palindrome(arr):       # two pointers; must work when left==right
        l, r = 0, len(arr) - 1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True               # single element / empty -> trivially True

    assert is_palindrome([7]) is True
    assert is_palindrome([]) is True
    assert is_palindrome([1, 2, 1]) is True
    assert is_palindrome([1, 2]) is False


# ---------------------------------------------------------------------------
# 3. ALL NEGATIVE — initializing "max" to 0 is a classic bug.
# ---------------------------------------------------------------------------
def all_negative() -> None:
    def naive_max_subarray(arr):  # WRONG: returns 0 for all-negative
        cur = best = 0
        for x in arr:
            cur = max(0, cur + x)
            best = max(best, cur)
        return best

    def robust_max_subarray(arr): # init from arr[0], not 0
        cur = best = arr[0]
        for x in arr[1:]: # start from the second element
            cur = max(x, cur + x)
            best = max(best, cur)
        return best

    assert naive_max_subarray([-3, -1, -2]) == 0        # the bug
    assert robust_max_subarray([-3, -1, -2]) == -1      # correct


# ---------------------------------------------------------------------------
# 4. ALL DUPLICATES / ALL SAME — dedup, unique counts, two-pointer skips.
# ---------------------------------------------------------------------------
def all_duplicates() -> None:
    def unique_count(arr):
        return len(set(arr))

    assert unique_count([5, 5, 5, 5]) == 1
    assert unique_count([]) == 0
    assert unique_count([1, 2, 2, 3]) == 3


# ---------------------------------------------------------------------------
# 5. ZEROS — break product/division-based approaches.
# ---------------------------------------------------------------------------
def zeros_present() -> None:
    def product_except_self(arr): # division-free -> survives zeros
        n = len(arr)
        res = [1] * n
        pre = 1
        for i in range(n):
            res[i] = pre
            pre *= arr[i]
        suf = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suf
            suf *= arr[i]
        return res

    # Two zeros -> every position is 0; one zero -> only that position nonzero.
    assert product_except_self([1, 2, 0, 4]) == [0, 0, 8, 0]
    assert product_except_self([0, 0, 3]) == [0, 0, 0]


# ---------------------------------------------------------------------------
# 6. SORTED / REVERSE-SORTED — boundary behavior & worst cases.
# ---------------------------------------------------------------------------
def sorted_inputs() -> None:
    def remove_dups_sorted(arr):
        if not arr:
            return 0
        w = 1
        for r in range(1, len(arr)):
            if arr[r] != arr[w - 1]:
                arr[w] = arr[r]
                w += 1
        return w

    a = [1, 2, 3]                 # already sorted, no dups
    assert remove_dups_sorted(a) == 3
    b = [9, 9, 9]                 # all same
    assert remove_dups_sorted(b) == 1


# ---------------------------------------------------------------------------
# 7. EVEN vs ODD LENGTH — median / middle index off-by-one.
# ---------------------------------------------------------------------------
def even_odd_length() -> None:
    def median_sorted(arr):       # arr assumed sorted
        n = len(arr)
        mid = n // 2
        if n % 2 == 1:
            return float(arr[mid])
        return (arr[mid - 1] + arr[mid]) / 2

    assert median_sorted([1, 2, 3]) == 2.0          # odd -> middle
    assert median_sorted([1, 2, 3, 4]) == 2.5       # even -> avg of two middles


# ---------------------------------------------------------------------------
# 8. TARGET NOT PRESENT — define & return a clear sentinel.
# ---------------------------------------------------------------------------
def target_absent() -> None:
    def binary_search(arr, target):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1                 # sentinel for "not found"

    assert binary_search([1, 3, 5, 7], 5) == 2
    assert binary_search([1, 3, 5, 7], 4) == -1
    assert binary_search([], 1) == -1


# ---------------------------------------------------------------------------
# 9. k BOUNDARIES — k == 0, k == n, k > n, k < 0 for windows/rotation.
# ---------------------------------------------------------------------------
def k_boundaries() -> None:
    def rotate_right(arr, k):
        n = len(arr)
        if n == 0:
            return
        k %= n                    # normalizes k>n, k==n (->0), and k<0
        arr[:] = arr[-k:] + arr[:-k] if k else arr[:]

    a = [1, 2, 3, 4, 5]
    rotate_right(a, 0)            # k == 0 -> unchanged
    assert a == [1, 2, 3, 4, 5]
    rotate_right(a, 5)            # k == n -> unchanged
    assert a == [1, 2, 3, 4, 5]
    rotate_right(a, 7)            # k > n -> k % n == 2
    assert a == [4, 5, 1, 2, 3]
    rotate_right(a, -2)           # negative k -> normalized
    assert a == [1, 2, 3, 4, 5]


# ---------------------------------------------------------------------------
# 10. MUTATION / ALIASING — don't clobber the caller's input unless asked.
# ---------------------------------------------------------------------------
def mutation_safety() -> None:
    def safe_sorted_copy(arr: List[int]) -> List[int]:
        return sorted(arr)        # returns NEW list; input untouched

    original = [3, 1, 2]
    result = safe_sorted_copy(original)
    assert result == [1, 2, 3]
    assert original == [3, 1, 2]  # caller's data preserved


def main() -> None:
    empty_array()
    single_element()
    all_negative()
    all_duplicates()
    zeros_present()
    sorted_inputs()
    even_odd_length()
    target_absent()
    k_boundaries()
    mutation_safety()
    print("edge_cases.py: all 10 edge-case categories verified ✔")


if __name__ == "__main__":
    main()
