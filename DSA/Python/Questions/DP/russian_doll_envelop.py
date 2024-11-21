"""
# Question: Russian Doll Envelopes
# Link: https://leetcode.com/problems/russian-doll-envelopes/

# Problem Statement:
# Given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width 
# and height of an envelope. One envelope can fit into another if both width and height are greater.
# Return the maximum number of envelopes you can Russian doll (put one inside another).

# Example:
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""

from typing import List

# Binary Search Implementation
"""
Algorithm:
1. Sort envelopes by width ascending and height descending
2. Find longest increasing subsequence based on height
3. Use binary search to optimize LIS calculation

Time Complexity: O(NlogN)
Space Complexity: O(N)
"""


def binary_search(dp: List[int], val: int) -> int:
    left, right = 0, len(dp) - 1
    while left <= right:
        mid = (left + right) >> 1
        if dp[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return left


def max_envelopes(envelopes: List[List[int]]) -> int:
    # Sort by width ascending and height descending
    envelopes.sort(key=lambda x: (x[0], -x[1]))

    # Initialize LIS array
    n = len(envelopes)
    LIS = [float("inf")] * (n + 1)
    LIS[0] = float("-inf")

    # Find longest increasing subsequence
    ans = 0
    for i in range(n):
        height = envelopes[i][1]
        insert_index = binary_search(LIS, height)
        ans = max(ans, insert_index)
        LIS[insert_index] = height

    return ans


def main():
    # Test cases
    test_cases = [
        [[5, 4], [6, 4], [6, 7], [2, 3]],  # Regular case
        [[1, 1], [1, 1], [1, 1]],  # Same size envelopes
        [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],  # Strictly increasing
        [[5, 4], [6, 4], [6, 7], [2, 3], [1, 2]],  # Mixed sizes
    ]

    for i, envelopes in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {envelopes}")
        print(f"Maximum number of nested envelopes: {max_envelopes(envelopes)}")


if __name__ == "__main__":
    main()
