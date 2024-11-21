"""
# Question: Matrix Chain Multiplication
# Link: https://leetcode.com/problems/matrix-chain-multiplication/

# Problem Statement:
# Given an array arr[] which represents the chain of matrices such that the
# ith matrix Ai is of dimension arr[i-1] x arr[i], find the minimum number
# of multiplications needed to multiply these matrices.

# Example:
# Input: arr = [40, 20, 30, 10, 30]
# Output: 26000
"""

from typing import List


# 1. Recursive Solution with Memoization
def matrix_chain_recursive(arr: List[int]) -> int:
    n = len(arr)
    # Initialize dp array with -1
    dp = [[-1] * n for _ in range(n)]

    def solve(i: int, j: int) -> int:
        # Base case: single matrix
        if i == j:
            return 0

        # Return memoized result if available
        if dp[i][j] != -1:
            return dp[i][j]

        # Initialize minimum operations
        min_ops = float("inf")

        # Try all possible partitions
        for k in range(i, j):
            # Calculate operations for current partition
            ops = solve(i, k) + solve(k + 1, j) + arr[i - 1] * arr[k] * arr[j]
            min_ops = min(min_ops, ops)

        # Store and return result
        dp[i][j] = min_ops
        return min_ops

    return solve(1, n - 1)


# 2. Tabulation Solution
def matrix_chain_tabulation(arr: List[int]) -> int:
    n = len(arr)
    # Create and initialize dp array
    dp = [[0] * n for _ in range(n)]

    # Fill dp table
    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")

            # Try all possible partitions
            for k in range(i, j):
                # Calculate operations for current partition
                ops = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], ops)

    return dp[1][n - 1]


def main():
    # Test cases
    test_cases = [
        [40, 20, 30, 10, 30],  # Regular case
        [10, 20, 30, 40, 30],  # Different dimensions
        [1, 2, 3, 4],  # Small matrices
        [10, 20, 30],  # Minimum chain
        [5, 10, 15, 20, 25],  # Sequential dimensions
    ]

    for i, arr in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {arr}")
        print(f"Recursive Solution: {matrix_chain_recursive(arr)}")
        print(f"Tabulation Solution: {matrix_chain_tabulation(arr)}")


if __name__ == "__main__":
    main()
