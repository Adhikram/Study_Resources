"""
# Question: Majority Element
# Link: https://leetcode.com/problems/majority-element/

# Problem Statement:
# Given an array nums of size n, return the majority element that appears more than ⌊n/2⌋ times.
# You may assume that the majority element always exists in the array.

# Example:
# Input: nums = [3, 2, 3]
# Output: 3

# Solution Approach:
# Boyer-Moore Voting Algorithm:
# - Time Complexity: O(n) where n is the length of the input array
# - Space Complexity: O(1) as we only use two variables

# Key Components:
# - majority_element(): Implements Boyer-Moore Voting Algorithm
"""

from typing import List

class MajorityElement:
    def majority_element(self, nums: List[int]) -> int:
        """
        Boyer-Moore Voting Algorithm to find the majority element.
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

def main():
    solution = MajorityElement()
    test_cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([1, 1, 2], 1)
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = solution.majority_element(nums)
        print(f"Test Case {i + 1}: Input: {nums}, Expected: {expected}, Result: {result}")
        assert result == expected, f"Test case {i + 1} failed"

if __name__ == "__main__":
    main()
