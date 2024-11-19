"""
# Question: Count Pairs

# Given two arrays 'a' and 'b' of equal length, count the number of pairs that can be formed
# where the sum of elements at corresponding indices is equal.

# Time Complexity: O(n) where n is the length of input arrays
# Space Complexity: O(n) for storing hashmap

# Algorithm:
# 1. Use a hashmap to store the frequency of sums (a[i] + b[i])
# 2. For each pair of elements:
#    - Calculate sum of elements at current index
#    - Update frequency in hashmap
#    - Add current frequency to result
# 3. Return total count of pairs

# Key Components:
# - count_pairs(): Main function that processes input arrays
# - HashMap: To store frequency of sums

# Data Structures:
# - dict: Python dictionary to store frequency of sums
# - Return format: Integer representing total count of pairs
"""

from typing import List


class CountPairs:
    def count_pairs(self, a: List[int], b: List[int]) -> int:
        result = 0
        freq_map = {}

        for i in range(len(a)):
            diff = a[i] + b[i]
            freq_map[diff] = freq_map.get(diff, 0) + 1
            result += freq_map[diff]

        return result


def main():
    count_pairs = CountPairs()
    a = [2, -2, 5, 3]
    b = [1, 5, -1, 1]
    print(count_pairs.count_pairs(a, b))  # Output should be 6


if __name__ == "__main__":
    main()