"""
# Question: Minimum Path Sum
# Link: https://leetcode.com/problems/minimum-path-sum/

# Problem Statement:
# Given a m x n grid filled with non-negative numbers, find a path from top left
# to bottom right, which minimizes the sum of all numbers along its path.
# You can only move right or down at any point.

# Example:
# Input: grid = [[1,3,1],
#                [1,5,1],
#                [4,2,1]]
# Output: 7
# Explanation: Path is: 1 → 3 → 1 → 1 → 1
"""

from typing import List

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. Start from target cell (bottom-right)
2. For each cell, try moving up and left
3. Take minimum of both paths plus current cell value
4. Use memoization to store results

Time Complexity: O(n*m)
Space Complexity: O(n*m) + O(n+m) recursion stack
"""


def min_path_sum_recursive(matrix: List[List[int]]) -> int:
    n, m = len(matrix), len(matrix[0])
    # Initialize dp array for memoization
    dp = [[-1] * m for _ in range(n)]

    def solve(i: int, j: int) -> int:
        # Base case: reached start
        if i == 0 and j == 0:
            return matrix[0][0]

        # Base case: out of bounds
        if i < 0 or j < 0:
            return float("inf")

        # Return memoized result if available
        if dp[i][j] != -1:
            return dp[i][j]

        # Calculate minimum path from up and left
        up = matrix[i][j] + solve(i - 1, j)
        left = matrix[i][j] + solve(i, j - 1)

        # Store and return result
        dp[i][j] = min(up, left)
        return dp[i][j]

    return solve(n - 1, m - 1)


# 2. Tabulation Solution
"""
Algorithm:
1. Create 2D dp array of size n*m
2. Fill dp table bottom-up:
   - For each cell, calculate min path from top and left
   - Add current cell value to minimum path
3. Final answer in bottom-right cell

Time Complexity: O(n*m)
Space Complexity: O(n*m)
"""


def min_path_sum_tabulation(matrix: List[List[int]]) -> int:
    n, m = len(matrix), len(matrix[0])
    # Create dp array
    dp = [[0] * m for _ in range(n)]

    # Fill dp table
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = matrix[i][j]
            else:
                up = matrix[i][j]
                if i > 0:
                    up += dp[i - 1][j]
                else:
                    up = float("inf")

                left = matrix[i][j]
                if j > 0:
                    left += dp[i][j - 1]
                else:
                    left = float("inf")

                dp[i][j] = min(up, left)

    return dp[n - 1][m - 1]


# 3. Space Optimized Solution
"""
Algorithm:
1. Use two arrays instead of 2D array
2. Previous row and current row sufficient
3. Update arrays in alternating fashion

Time Complexity: O(n*m)
Space Complexity: O(m)
"""


def min_path_sum_optimized(matrix: List[List[int]]) -> int:
    n, m = len(matrix), len(matrix[0])
    # Initialize previous row
    prev = [0] * m

    # Process matrix row by row
    for i in range(n):
        curr = [0] * m
        for j in range(m):
            if i == 0 and j == 0:
                curr[j] = matrix[i][j]
            else:
                up = matrix[i][j]
                if i > 0:
                    up += prev[j]
                else:
                    up = float("inf")

                left = matrix[i][j]
                if j > 0:
                    left += curr[j - 1]
                else:
                    left = float("inf")

                curr[j] = min(up, left)
        prev = curr[:]

    return prev[m - 1]


def main():
    # Test cases
    test_cases = [
        [[1, 3, 1], [1, 5, 1], [4, 2, 1]],  # Regular case
        [[1, 2, 3], [4, 5, 6]],  # Rectangle matrix
        [[1]],  # Single cell
        [[1, 2, 3]],  # Single row
        [[1], [2], [3]],  # Single column
    ]

    for i, matrix in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {matrix}")
        print(f"Recursive Solution: {min_path_sum_recursive(matrix)}")
        print(f"Tabulation Solution: {min_path_sum_tabulation(matrix)}")
        print(f"Optimized Solution: {min_path_sum_optimized(matrix)}")


if __name__ == "__main__":
    main()
