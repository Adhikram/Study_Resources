"""
# Question: Find Peak Element
# Link: https://leetcode.com/problems/find-peak-element/

# Problem Statement:
# A peak element is an element that is strictly greater than its neighbors.
# Given an integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return any of the peaks' index.

# Example:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
"""

from typing import List


class PeakElement:
    def find_peak_binary(self, nums: List[int]) -> int:
        """
        Binary search approach
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left

    def find_peak_linear(self, nums: List[int]) -> int:
        """
        Linear search approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1

    def find_peak_recursive(self, nums: List[int]) -> int:
        """
        Recursive approach
        Time Complexity: O(log n)
        Space Complexity: O(log n)
        """

        def find_peak_helper(left: int, right: int) -> int:
            if left == right:
                return left

            mid = (left + right) >> 1
            if nums[mid] > nums[mid + 1]:
                return find_peak_helper(left, mid)
            return find_peak_helper(mid + 1, right)

        return find_peak_helper(0, len(nums) - 1)


def main():
    test_cases = [
        {"nums": [1, 2, 3, 1], "expected_values": {2}},
        {"nums": [1, 2, 1, 3, 5, 6, 4], "expected_values": {1, 5}},
        {"nums": [1], "expected_values": {0}},
    ]

    solution = PeakElement()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Input: {test['nums']}")

        result_binary = solution.find_peak_binary(test["nums"])
        result_linear = solution.find_peak_linear(test["nums"])
        result_recursive = solution.find_peak_recursive(test["nums"])

        print(f"Binary Search Result: {result_binary}")
        print(f"Linear Search Result: {result_linear}")
        print(f"Recursive Result: {result_recursive}")

        # Verify results are valid peaks
        assert result_binary in test["expected_values"]
        assert result_linear in test["expected_values"]
        assert result_recursive in test["expected_values"]


if __name__ == "__main__":
    main()
