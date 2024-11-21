"""
# Question: Longest Increasing Subsequence
# Link: https://leetcode.com/problems/longest-increasing-subsequence/

# Problem Statement:
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements
# without changing the order of the remaining elements.

# Example:
# Input: nums = [10,22,9,33,21,50,41,60,80]
# Output: 6
# Explanation: The longest increasing subsequence is [10,22,33,50,60,80]
"""

from typing import List

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. For each element, two choices:
   - Include if greater than previous element
   - Skip current element
2. Track previous index for comparison
3. Use memoization to store results

Time Complexity: O(n^2)
Space Complexity: O(n^2) + O(n) recursion stack
"""


def lis_recursive(arr: List[int]) -> int:
    n = len(arr)
    # Initialize dp array for memoization
    dp = [[-1] * (n + 1) for _ in range(n)]

    def solve(ind: int, prev_ind: int) -> int:
        # Base case: reached end of array
        if ind == n:
            return 0

        # Return memoized result if available
        if dp[ind][prev_ind + 1] != -1:
            return dp[ind][prev_ind + 1]

        # Don't take current element
        length = solve(ind + 1, prev_ind)

        # Take current element if valid
        if prev_ind == -1 or arr[ind] > arr[prev_ind]:
            length = max(length, 1 + solve(ind + 1, ind))

        # Store and return result
        dp[ind][prev_ind + 1] = length
        return length

    return solve(0, -1)


# 2. Tabulation Solution
"""
Algorithm:
1. Create 2D dp array
2. Process array from end to start
3. For each position, try all possible previous elements
4. Track maximum length at each step

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""


def lis_tabulation(arr: List[int]) -> int:
    n = len(arr)
    # Create dp array
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill dp table
    for ind in range(n - 1, -1, -1):
        for prev_ind in range(ind - 1, -2, -1):
            # Don't take current element
            length = dp[ind + 1][prev_ind + 1]

            # Take current element if valid
            if prev_ind == -1 or arr[ind] > arr[prev_ind]:
                length = max(length, 1 + dp[ind + 1][ind + 1])

            dp[ind][prev_ind + 1] = length

    return dp[0][0]


# 3. Space Optimized Solution
"""
Algorithm:
1. Use two arrays instead of 2D array
2. Next and current arrays sufficient
3. Update arrays in alternating fashion

Time Complexity: O(n^2)
Space Complexity: O(n)
"""


def lis_optimized(arr: List[int]) -> int:
    n = len(arr)
    # Initialize arrays
    next = [0] * (n + 1)
    curr = [0] * (n + 1)

    # Process array
    for ind in range(n - 1, -1, -1):
        for prev_ind in range(ind - 1, -2, -1):
            # Don't take current element
            length = next[prev_ind + 1]

            # Take current element if valid
            if prev_ind == -1 or arr[ind] > arr[prev_ind]:
                length = max(length, 1 + next[ind + 1])

            curr[prev_ind + 1] = length

        next = curr[:]

    return curr[0]


def main():
    # Test cases
    test_cases = [
        [10, 22, 9, 33, 21, 50, 41, 60, 80],  # Regular case
        [3, 10, 2, 1, 20],  # Multiple increasing sequences
        [7, 7, 7, 7],  # Equal elements
        [1],  # Single element
        [5, 4, 3, 2, 1],  # Decreasing sequence
    ]

    for i, arr in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {arr}")
        print(f"Recursive Solution: {lis_recursive(arr)}")
        print(f"Tabulation Solution: {lis_tabulation(arr)}")
        print(f"Optimized Solution: {lis_optimized(arr)}")


if __name__ == "__main__":
    main()
