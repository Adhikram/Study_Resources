"""
# Question: Unique Paths
# Link: https://leetcode.com/problems/unique-paths/

# Problem Statement:
# Given a grid of size m x n, find the number of unique paths from top-left
# to bottom-right corner. You can only move right or down at any point.

# Example:
# Input: m = 3, n = 7
# Output: 28
# Explanation: There are 28 unique paths from start to end.
"""

# 1. Tabulation Solution
"""
Algorithm:
1. Create m x n grid initialized with 1s
2. For each cell (i,j), paths = paths from above + paths from left
3. Process grid row by row, column by column
4. Bottom-right cell contains total unique paths

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""


def unique_paths(m: int, n: int) -> int:
    # Initialize grid with 1s
    grid = [[1] * n for _ in range(m)]

    # Fill grid with number of paths
    for i in range(1, m):
        for j in range(1, n):
            # Paths = paths from above + paths from left
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    # Return total paths from start to end
    return grid[m - 1][n - 1]


# 2. Space Optimized Solution
"""
Algorithm:
1. Use two arrays instead of full grid
2. Previous row and current row sufficient
3. Update arrays in alternating fashion

Time Complexity: O(m*n)
Space Complexity: O(n)
"""


def unique_paths_optimized(m: int, n: int) -> int:
    # Initialize previous and current rows with 1s
    prev = [1] * n
    curr = [1] * n

    # Process each row
    for i in range(1, m):
        # Process each column
        for j in range(1, n):
            # Current paths = paths from above + paths from left
            curr[j] = prev[j] + curr[j - 1]
        # Update previous row for next iteration
        prev = curr[:]

    # Return total paths
    return curr[n - 1]


def main():
    # Test cases
    test_cases = [
        (3, 7),  # Regular case
        (3, 2),  # Narrow grid
        (7, 3),  # Tall grid
        (1, 1),  # Single cell
        (10, 10),  # Large grid
    ]

    for i, (m, n) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: m = {m}, n = {n}")
        print(f"Tabulation Solution: {unique_paths(m, n)}")
        print(f"Optimized Solution: {unique_paths_optimized(m, n)}")


if __name__ == "__main__":
    main()
