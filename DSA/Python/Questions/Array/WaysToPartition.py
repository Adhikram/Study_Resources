"""
# Question: Maximum Number of Ways to Partition an Array
# Link: https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

# Find max ways to partition array after changing at most one element to k

# Time Complexity: O(n) where n is length of array
# Space Complexity: O(n) for storing prefix sums

# Algorithm:
# 1. Calculate total sum and build prefix/suffix maps
# 2. Track partition points with and without changes
# 3. Handle both unchanged array and single element changes
# 4. Update counts based on prefix and suffix sums

# Key Components:
# - ways_to_partition(): Main function implementing partition counting
# - HashMap for sum frequency tracking
# - Dynamic prefix/suffix handling
"""

from typing import List
from collections import defaultdict


class WaysToPartition:
    def ways_to_partition(self, nums: List[int], k: int) -> int:
        total_sum = sum(nums)
        sum_map = defaultdict(int)
        right_sum = 0

        # Build suffix map
        for i in range(len(nums) - 1, 0, -1):
            right_sum += nums[i]
            target = total_sum - right_sum * 2 + k
            sum_map[target] += 1

        left_sum = 0
        response = sum_map.get(nums[0], 0)
        unchanged_count = 0

        # Process each position
        for i in range(1, len(nums)):
            left_sum += nums[i - 1]
            if left_sum * 2 == total_sum:
                unchanged_count += 1

            target = total_sum - left_sum * 2
            sum_map[target + k] = sum_map.get(target + k, 0) + 1
            sum_map[-target + k] = sum_map.get(-target + k, 0) - 1
            response = max(response, sum_map.get(nums[i], 0))

        return max(response, unchanged_count)


def main():
    solution = WaysToPartition()
    nums = [2, -1, 2]
    k = 3
    result = solution.ways_to_partition(nums, k)
    print(result)  # Expected output: 1


if __name__ == "__main__":
    main()
