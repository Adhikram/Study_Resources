"""
# Question: Four Sum II
# Link: https://leetcode.com/problems/4sum-ii/

# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
# return the number of tuples (i, j, k, l) such that:
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

# Time Complexity: O(n^2) - computing all possible pairs from two arrays twice
# Space Complexity: O(n^2) - storing sums and counts in HashMap

# Algorithm:
# 1. Use HashMap to store sum frequencies of first two arrays
# 2. Check complementary sums in second two arrays
# 3. Count matching pairs that sum to zero

# Key Components:
# - four_sum_count(): Main function implementing the solution
# - HashMap to store sum frequencies
# - Two-phase approach: store and lookup
"""

from typing import List
from collections import defaultdict


class FourSumII:
    def four_sum_count(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        sum_count_map = defaultdict(int)
        count = 0

        # Compute all possible sums of pairs from nums1 and nums2
        for num1 in nums1:
            for num2 in nums2:
                sum_count_map[num1 + num2] += 1

        # Compute all possible sums of pairs from nums3 and nums4
        for num3 in nums3:
            for num4 in nums4:
                count += sum_count_map[-(num3 + num4)]

        return count


def main():
    solution = FourSumII()
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    result = solution.four_sum_count(nums1, nums2, nums3, nums4)
    print(result)  # Expected output: 2


if __name__ == "__main__":
    main()
