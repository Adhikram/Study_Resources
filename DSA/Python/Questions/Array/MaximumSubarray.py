"""
# Question: Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the subarray with the largest sum and return its sum.
# Uses Kadane's Algorithm for optimal solution.

# Time Complexity: O(n) where n is the length of input array
# Space Complexity: O(1) as we only track two variables

# Algorithm:
# 1. Initialize maxSum as minimum integer and curSum as 0
# 2. Iterate through array:
#    - Add current element to curSum
#    - Update maxSum if curSum is larger
#    - Reset curSum to 0 if it becomes negative
# 3. Return maxSum

# Key Components:
# - kadens_algo(): Implements Kadane's Algorithm
# - Running sum tracking with maximum value updates
"""

from typing import List


class MaximumSubarray:
    def kadens_algo(self, arr: List[int]) -> int:
        max_sum = float("-inf")
        cur_sum = 0

        for num in arr:
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
            cur_sum = max(cur_sum, 0)

        return max_sum


def main():
    solution = MaximumSubarray()
    arr = [1, -2, 3, -9, 5]
    result = solution.kadens_algo(arr)
    print(result)  # Expected output: 5


if __name__ == "__main__":
    main()
