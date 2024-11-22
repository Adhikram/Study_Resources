"""
# Question: Max Consecutive Ones
# Link: https://leetcode.com/problems/max-consecutive-ones/

# Problem Statement:
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example:
# Input: nums = [1, 1, 0, 1, 1, 1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Solution Approach:
# - Iterate through the array while keeping track of the current count of consecutive 1s.
# - Reset the count when a 0 is encountered.
# - Update the maximum count whenever the current count exceeds it.

# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(1) as we only use two variables

# Key Components:
# - find_max_consecutive_ones(): Main function implementing the counting logic
"""

from typing import List

class MaxConsecutive1:
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        """
        Function to find the maximum number of consecutive 1's in the array.
        """
        max_count = 0
        current_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0

        return max_count

def main():
    solution = MaxConsecutive1()
    test_cases = [
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2),
        ([0, 0, 0, 0], 0),
        ([1, 1, 1, 1], 4),
        ([1, 0, 1, 0, 1, 0], 1)
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = solution.find_max_consecutive_ones(nums)
        print(f"Test Case {i + 1}: Input: {nums}, Expected: {expected}, Result: {result}")
        assert result == expected, f"Test case {i + 1} failed"

if __name__ == "__main__":
    main()
