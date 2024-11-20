"""
# Question: Maximum Size Subarray Sum Equals k
# Link: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

# Given an array nums and target k, find length of longest subarray with sum equal to k.
# Implements both HashMap and Sliding Window approaches.

# Time Complexity: O(n) for both approaches
# Space Complexity: O(n) for HashMap, O(1) for Sliding Window

# Algorithm 1 (HashMap):
# 1. Track prefix sums and their earliest indices
# 2. For each prefix sum, check if (prefix_sum - k) exists
# 3. Update max length when target sum is found

# Algorithm 2 (Sliding Window):
# 1. Use two pointers to maintain window
# 2. Expand/contract window based on current sum
# 3. Update max length when sum equals k

# Key Components:
# - get_longest_sub_array(): HashMap approach
# - get_longest_sub_array_optimized(): Sliding Window approach
"""

from typing import List
from collections import defaultdict


class MaximumSubArrayWithSumK:
    def get_longest_sub_array(self, nums: List[int], k: int) -> int:
        hash_map = {0: -1}
        prefix_sum = result = 0

        for i, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum == k:
                result = i + 1

            if prefix_sum - k in hash_map:
                result = max(result, i - hash_map[prefix_sum - k])

            if prefix_sum not in hash_map:
                hash_map[prefix_sum] = i

        return result

    def get_longest_sub_array_optimized(self, nums: List[int], k: int) -> int:
        max_length = curr_sum = start = 0

        for end in range(len(nums)):
            curr_sum += nums[end]

            while curr_sum > k:
                curr_sum -= nums[start]
                start += 1

            if curr_sum == k:
                max_length = max(max_length, end - start + 1)

        return max_length


def main():
    solution = MaximumSubArrayWithSumK()
    nums = [1, -1, 1, 0, 2, -10]
    k = 3

    result1 = solution.get_longest_sub_array(nums, k)
    result2 = solution.get_longest_sub_array_optimized(nums, k)

    print(f"HashMap approach result: {result1}")
    print(f"Sliding Window approach result: {result2}")


if __name__ == "__main__":
    main()
