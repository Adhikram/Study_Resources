"""
# Question: Number of Islands
# Link: https://leetcode.com/problems/number-of-islands/

# Problem Statement:
# Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Example:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
"""

from typing import List

# DFS Solution
"""
Algorithm:
1. Iterate through each cell in the grid.
2. When a '1' is found, perform DFS to mark all connected '1's as visited.
3. Increment the island count for each DFS initiation.
4. Return the total number of islands.

Time Complexity: O(M * N) where M is the number of rows and N is the number of columns.
Space Complexity: O(M * N) for the visited array and recursion stack.
"""


def num_islands(grid: List[List[str]]) -> int:
    def dfs(r: int, c: int):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
            return
        grid[r][c] = "0"  # Mark the cell as visited by sinking the island
        # Explore all four directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    if not grid:
        return 0

    num_islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":  # Start a DFS if a new island is found
                dfs(r, c)
                num_islands += 1  # Increment the island count

    return num_islands


def main():
    test_cases = [
        {
            "grid": [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            "expected": 1,
        },
        {
            "grid": [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            "expected": 3,
        },
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Grid: {test['grid']}")
        result = num_islands(test["grid"])
        print(f"Result: {result}, Expected: {test['expected']}")
        assert result == test["expected"], f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
