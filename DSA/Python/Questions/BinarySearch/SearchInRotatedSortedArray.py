"""
# Question: Search in Rotated Sorted Array
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

# Problem Statement:
# Given a rotated sorted array nums and a target value, return the index of target if it exists, else return -1.
# The array was originally sorted in ascending order before being rotated between 1 and n times.

# Example:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
"""

from typing import List


class SearchInRotatedSortedArray:
    def search_binary(self, nums: List[int], target: int) -> int:
        """
        Binary search approach
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

    def search_pivot_based(self, nums: List[int], target: int) -> int:
        """
        Two-step approach: find pivot then binary search
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """

        def find_pivot(arr: List[int]) -> int:
            left, right = 0, len(arr) - 1
            while left < right:
                mid = (left + right) >> 1
                if arr[mid] > arr[right]:
                    left = mid + 1
                else:
                    right = mid
            return left

        def binary_search(arr: List[int], left: int, right: int, target: int) -> int:
            while left <= right:
                mid = (left + right) >> 1
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        pivot = find_pivot(nums)
        if target >= nums[pivot] and target <= nums[-1]:
            return binary_search(nums, pivot, len(nums) - 1, target)
        return binary_search(nums, 0, pivot - 1, target)

    def search_linear(self, nums: List[int], target: int) -> int:
        """
        Linear search approach (for comparison)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1


def main():
    test_cases = [
        {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 0, "expected": 4},
        {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 3, "expected": -1},
        {"nums": [1], "target": 0, "expected": -1},
    ]

    solution = SearchInRotatedSortedArray()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Array: {test['nums']}")
        print(f"Target: {test['target']}")

        result_binary = solution.search_binary(test["nums"], test["target"])
        result_pivot = solution.search_pivot_based(test["nums"], test["target"])
        result_linear = solution.search_linear(test["nums"], test["target"])

        print(f"Binary Search Result: {result_binary}")
        print(f"Pivot-based Result: {result_pivot}")
        print(f"Linear Search Result: {result_linear}")
        print(f"Expected: {test['expected']}")

        assert result_binary == result_pivot == result_linear == test["expected"]


if __name__ == "__main__":
    main()
