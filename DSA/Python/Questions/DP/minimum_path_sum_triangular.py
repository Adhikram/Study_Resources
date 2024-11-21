"""
# Question: Minimum Path Sum in Triangle
# Link: https://leetcode.com/problems/triangle/

# Problem Statement:
# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below.

# Example:
# Input: triangle = [[1],
#                   [2,3],
#                   [3,6,7],
#                   [8,9,6,10]]
# Output: 11
"""

from typing import List

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. Start from top of triangle (0,0)
2. For each cell, try both possible moves:
   - Directly down (i+1, j)
   - Diagonally down (i+1, j+1)
3. Cache results in dp table
4. Return minimum path sum

Time Complexity: O(N*N) - visit each cell once
Space Complexity: O(N*N) + O(N) for dp table and recursion stack
"""


def min_path_sum_recursive(triangle: List[List[int]]) -> int:
    n = len(triangle)
    dp = [[-1] * n for _ in range(n)]

    def solve(i: int, j: int) -> int:
        # Base case: reached bottom row
        if i == n - 1:
            return triangle[i][j]

        if dp[i][j] != -1:
            return dp[i][j]

        # Calculate minimum path sum through down and diagonal moves
        down = triangle[i][j] + solve(i + 1, j)
        diagonal = triangle[i][j] + solve(i + 1, j + 1)

        dp[i][j] = min(down, diagonal)
        return dp[i][j]

    return solve(0, 0)


# 2. Tabulation Solution
"""
Algorithm:
1. Create dp table of triangle size
2. Initialize bottom row with triangle values
3. For each cell from bottom-up:
   - Calculate min path through down and diagonal
   - Store minimum sum at current cell
4. Return value at dp[0][0]

Time Complexity: O(N*N) - process each cell once
Space Complexity: O(N*N) for dp table
"""


def min_path_sum_tabulation(triangle: List[List[int]]) -> int:
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]

    # Initialize bottom row
    for j in range(n):
        dp[n - 1][j] = triangle[n - 1][j]

    # Fill dp table bottom-up
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            down = triangle[i][j] + dp[i + 1][j]
            diagonal = triangle[i][j] + dp[i + 1][j + 1]
            dp[i][j] = min(down, diagonal)

    return dp[0][0]


# 3. Space Optimized Solution
"""
Algorithm:
1. Use single array starting with bottom row
2. Process triangle bottom-up:
   - Create current row array
   - Calculate min path for each position
   - Update front array for next iteration
3. Return final value in front[0]

Time Complexity: O(N*N) - process each cell once
Space Complexity: O(N) for single row storage
"""


def min_path_sum_optimized(triangle: List[List[int]]) -> int:
    n = len(triangle)
    front = triangle[-1].copy()

    # Process each row bottom-up
    for i in range(n - 2, -1, -1):
        curr = [0] * (i + 1)
        for j in range(i + 1):
            down = triangle[i][j] + front[j]
            diagonal = triangle[i][j] + front[j + 1]
            curr[j] = min(down, diagonal)
        front = curr[:]

    return front[0]


def main():
    # Test cases with different scenarios
    test_cases = [
        # Regular case with multiple paths
        [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]],
        # Small triangle
        [[2], [3, 4], [6, 5, 7]],
        # Minimum case: single element
        [[-10]],
    ]

    # Test each case with all three solutions
    for i, triangle in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {triangle}")
        print(f"Recursive Solution: {min_path_sum_recursive(triangle)}")
        print(f"Tabulation Solution: {min_path_sum_tabulation(triangle)}")
        print(f"Optimized Solution: {min_path_sum_optimized(triangle)}")


if __name__ == "__main__":
    main()
