"""
# Question: Max Consecutive Ones III
# Link: https://leetcode.com/problems/max-consecutive-ones-iii/

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's 
# in the array if you can flip at most k 0's.

# Time Complexity: O(n) where n is the length of input array
# Space Complexity: O(1) using sliding window approach

# Algorithm:
# 1. Use sliding window technique with left and right pointers
# 2. Expand window while counting zeros
# 3. When zero count exceeds k, shrink window from left
# 4. Track maximum window length throughout process

# Key Components:
# - longest_ones(): Implements sliding window approach
# - Zero count tracking within window
# - Dynamic window size adjustment
"""

from typing import List


class MaxConsecutiveOnesIII:
    def longest_ones(self, nums: List[int], k: int) -> int:
        left = right = 0
        max_len = 0
        zero_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1

            # Shrink window if zero count exceeds k
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update maximum length
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len


def main():
    solution = MaxConsecutiveOnesIII()
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    result = solution.longest_ones(nums, k)
    print(result)  # Expected output: 6


if __name__ == "__main__":
    main()
