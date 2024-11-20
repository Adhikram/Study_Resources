"""
# Question: Maximum Frequency of the Most Frequent Element
# Link: https://leetcode.com/problems/frequency-of-the-most-frequent-element/

# Given an integer array nums and an integer k, return the maximum possible frequency
# of an element after performing at most k operations where each operation increments
# an element by 1.

# Time Complexity: O(n log n) due to initial sorting
# Space Complexity: O(1) using sliding window approach

# Algorithm:
# 1. Sort the array to group similar elements
# 2. Use sliding window to track potential frequency
# 3. Calculate total increments needed in current window
# 4. Adjust window size based on available operations (k)

# Key Components:
# - max_frequency(): Main function implementing sliding window
# - Total sum tracking within window
# - Dynamic window adjustment based on k operations
"""

from typing import List


class MaxFrequencyOfTheMostFrequentElement:
    def max_frequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = right = 0
        res = total = 0

        while right < len(nums):
            total += nums[right]

            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1

            res = max(res, right - left + 1)
            right += 1

        return res


def main():
    solution = MaxFrequencyOfTheMostFrequentElement()
    nums = [1, 2, 4]
    k = 5
    result = solution.max_frequency(nums, k)
    print(result)  # Expected output: 3


if __name__ == "__main__":
    main()
