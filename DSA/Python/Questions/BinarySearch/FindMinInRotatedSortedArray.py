"""
# Question: Find Minimum in Rotated Sorted Array
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Problem Statement:
# Given a sorted array that has been rotated between 1 and n times, find the minimum element.
# The array does not contain duplicates.

# Example:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: Original array was [1,2,3,4,5] and it was rotated 3 times.
"""

from typing import List


class FindMinInRotatedSortedArray:
    def find_min_binary(self, nums: List[int]) -> int:
        """
        Binary search approach
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) >> 1

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

    def find_min_linear(self, nums: List[int]) -> int:
        """
        Linear search approach (for comparison)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]
        return nums[0]

    def find_min_divide_conquer(self, nums: List[int]) -> int:
        """
        Divide and conquer approach
        Time Complexity: O(log n)
        Space Complexity: O(log n) due to recursion
        """

        def find_min_recursive(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            mid = (left + right) >> 1

            if nums[mid] > nums[right]:
                return find_min_recursive(mid + 1, right)
            return find_min_recursive(left, mid)

        return find_min_recursive(0, len(nums) - 1)


def main():
    test_cases = [
        {"nums": [3, 4, 5, 1, 2], "expected": 1},
        {"nums": [4, 5, 6, 7, 0, 1, 2], "expected": 0},
        {"nums": [11, 13, 15, 17], "expected": 11},
        {"nums": [2, 1], "expected": 1},
    ]

    solution = FindMinInRotatedSortedArray()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Input: {test['nums']}")

        result_binary = solution.find_min_binary(test["nums"])
        result_linear = solution.find_min_linear(test["nums"])
        result_divide_conquer = solution.find_min_divide_conquer(test["nums"])

        print(f"Binary Search Result: {result_binary}")
        print(f"Linear Search Result: {result_linear}")
        print(f"Divide & Conquer Result: {result_divide_conquer}")
        print(f"Expected: {test['expected']}")

        assert (
            result_binary == result_linear == result_divide_conquer == test["expected"]
        )


if __name__ == "__main__":
    main()
