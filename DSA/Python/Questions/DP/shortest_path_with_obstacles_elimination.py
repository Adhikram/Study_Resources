"""
# Question: Shortest Path in Grid with Obstacles Elimination
# Link: https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

# Problem Statement:
# Given a m x n grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down,
# left, or right from and to an empty cell. Return the minimum number of steps to walk from the
# upper left corner to the lower right corner, given that you can eliminate at most k obstacles.

# Example:
# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
"""

from typing import List

# DFS Solution with Memoization
"""
Algorithm:
1. Use DFS to explore all possible paths
2. Track remaining obstacles that can be eliminated
3. Cache results for each state (i, j, k)
4. Return minimum steps needed

Time Complexity: O(m*n*k)
Space Complexity: O(m*n*k)
"""


def shortest_path(grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])

    # Early return conditions
    if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
        return -1

    if k >= m + n - 2:
        return m + n - 2

    # Initialize 3D DP array
    dp = [[[float("inf")] * (k + 1) for _ in range(n)] for _ in range(m)]

    def dfs(i: int, j: int, k: int) -> int:
        # Check bounds and visited cells
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == -1:
            return float("inf") - 1

        # Reached target
        if i == m - 1 and j == n - 1:
            return 0

        # Return cached result
        if dp[i][j][k] != float("inf"):
            return dp[i][j][k]

        # Manhattan distance optimization
        if k >= (m - i - 1) + (n - j - 1):
            return (m - i - 1) + (n - j - 1)

        # Handle obstacle
        if grid[i][j] == 1 and k <= 0:
            return float("inf") - 1

        # Mark cell as visited
        temp = grid[i][j]
        grid[i][j] = -1

        # Try all four directions
        left = dfs(i - 1, j, k - temp)
        right = dfs(i + 1, j, k - temp)
        up = dfs(i, j - 1, k - temp)
        down = dfs(i, j + 1, k - temp)

        # Restore cell
        grid[i][j] = temp

        # Store minimum path
        dp[i][j][k] = 1 + min(left, min(right, min(up, down)))
        return dp[i][j][k]

    result = dfs(0, 0, k)
    return result if result != float("inf") else -1


def main():
    # Test cases
    test_cases = [
        {"grid": [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], "k": 1},
        {"grid": [[0, 1, 1], [1, 1, 1], [1, 0, 0]], "k": 1},
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Grid: {test['grid']}")
        print(f"k: {test['k']}")
        print(f"Minimum steps: {shortest_path(test['grid'], test['k'])}")


if __name__ == "__main__":
    main()
