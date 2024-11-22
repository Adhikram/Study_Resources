"""
# Question: Search in Rotated Sorted Array II
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

# Problem Statement:
# Given a rotated sorted array nums that may contain duplicates and a target value,
# return true if target is in nums, or false if it is not in nums.

# Example:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
"""

from typing import List


class SearchInRotatedSortedArray2:
    def search_binary(self, nums: List[int], target: int) -> bool:
        """
        Binary search approach handling duplicates
        Time Complexity: O(log n) average, O(n) worst case
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1

            if nums[mid] == target:
                return True

            # Handle duplicates
            if nums[left] == nums[mid]:
                left += 1
                continue

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

        return False

    def search_two_pointer(self, nums: List[int], target: int) -> bool:
        """
        Two pointer approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == target or nums[right] == target:
                return True
            if nums[left] < target:
                left += 1
            if nums[right] > target:
                right -= 1
            if nums[left] > target and nums[right] < target:
                return False

        return False

    def search_set(self, nums: List[int], target: int) -> bool:
        """
        Set-based approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return target in set(nums)


def main():
    test_cases = [
        {"nums": [2, 5, 6, 0, 0, 1, 2], "target": 0, "expected": True},
        {"nums": [2, 5, 6, 0, 0, 1, 2], "target": 3, "expected": False},
        {"nums": [1, 1, 1, 1, 1, 1, 1], "target": 1, "expected": True},
    ]

    solution = SearchInRotatedSortedArray2()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Array: {test['nums']}")
        print(f"Target: {test['target']}")

        result_binary = solution.search_binary(test["nums"], test["target"])
        result_two_pointer = solution.search_two_pointer(test["nums"], test["target"])
        result_set = solution.search_set(test["nums"], test["target"])

        print(f"Binary Search Result: {result_binary}")
        print(f"Two Pointer Result: {result_two_pointer}")
        print(f"Set-based Result: {result_set}")
        print(f"Expected: {test['expected']}")

        assert result_binary == result_two_pointer == result_set == test["expected"]


if __name__ == "__main__":
    main()
