"""
# Question: Max Consecutive Ones
# Link: https://leetcode.com/problems/max-consecutive-ones/

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Time Complexity: O(n) where n is the length of input array
# Space Complexity: O(1) as we only use two variables

# Algorithm:
# 1. Keep track of current count and maximum count of consecutive ones
# 2. Reset count when encountering zero
# 3. Update maximum count whenever current count increases
# 4. Return the maximum count found

# Key Components:
# - find_max_consecutive_ones(): Main function implementing the counting logic
# - Running counter approach with max tracking
"""

from typing import List


class MaxConsecutive1:
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        result = 0
        count = 0

        for num in nums:
            if num == 0:
                result = max(result, count)
                count = 0
            else:
                count += 1

        return max(result, count)


def main():
    solution = MaxConsecutive1()
    nums = [1, 1, 0, 1, 1, 1]
    result = solution.find_max_consecutive_ones(nums)
    print(result)  # Expected output: 3


if __name__ == "__main__":
    main()
