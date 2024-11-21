"""
# Question: Minimum/Maximum Falling Path Sum
# Link: https://leetcode.com/problems/minimum-falling-path-sum/

# Problem Statement:
# Given an N*M matrix, find the maximum path sum from any cell of the first row
# to any cell of the last row. At every cell we can move to:
# - Bottom cell (↓)
# - Bottom-right cell (↘)
# - Bottom-left cell (↙)

# Example:
# Input: matrix = [[1,2,3],
#                 [4,5,6],
#                 [7,8,9]]
# Output: 28
"""

from typing import List
import math

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. Start from any cell in last row
2. For each cell, try all three possible moves up
3. Track maximum path sum encountered
4. Use memoization to store results

Time Complexity: O(N*M)
Space Complexity: O(N*M) + O(N) recursion stack
"""


def get_max_path_sum_recursive(matrix: List[List[int]]) -> int:
    n, m = len(matrix), len(matrix[0])
    # Initialize dp array for memoization
    dp = [[-1] * m for _ in range(n)]

    def solve(i: int, j: int) -> int:
        # Base case: out of bounds
        if j < 0 or j >= m:
            return -math.inf
        # Base case: reached first row
        if i == 0:
            return matrix[0][j]

        # Return memoized result if available
        if dp[i][j] != -1:
            return dp[i][j]

        # Calculate three possible paths
        up = matrix[i][j] + solve(i - 1, j)  # Bottom path
        left_diag = matrix[i][j] + solve(i - 1, j - 1)  # Bottom-left diagonal
        right_diag = matrix[i][j] + solve(i - 1, j + 1)  # Bottom-right diagonal

        # Store maximum path sum
        dp[i][j] = max(up, max(left_diag, right_diag))
        return dp[i][j]

    # Try all positions in last row
    max_path = -math.inf
    for j in range(m):
        max_path = max(max_path, solve(n - 1, j))

    return max_path


# 2. Tabulation Solution
"""
Algorithm:
1. Create 2D dp array
2. Initialize first row with matrix values
3. For each cell, calculate max path from three possible moves
4. Store maximum value at each step

Time Complexity: O(N*M)
Space Complexity: O(N*M)
"""


def get_max_path_sum_tabulation(matrix: List[List[int]]) -> int:
    # Get matrix dimensions
    n, m = len(matrix), len(matrix[0])
    # Initialize dp table with zeros
    dp = [[0] * m for _ in range(n)]

    # Copy first row as is - base case
    dp[0] = matrix[0].copy()

    # Process each cell row by row
    for i in range(1, n):
        for j in range(m):
            # Calculate straight up path
            up = matrix[i][j] + dp[i - 1][j]

            # Calculate diagonal left path
            left_diag = matrix[i][j]
            if j > 0:  # Check if left diagonal exists
                left_diag += dp[i - 1][j - 1]
            else:
                left_diag = -math.inf

            # Calculate diagonal right path
            right_diag = matrix[i][j]
            if j < m - 1:  # Check if right diagonal exists
                right_diag += dp[i - 1][j + 1]
            else:
                right_diag = -math.inf

            # Store maximum of all three paths
            dp[i][j] = max(up, max(left_diag, right_diag))

    # Return maximum value from last row
    return max(dp[n - 1])


# 3. Space Optimized Solution
"""
Algorithm:
1. Use single array instead of 2D array
2. Keep track of previous row values
3. Update array in-place for current row

Time Complexity: O(N*M)
Space Complexity: O(M)
"""


def get_max_path_sum_optimized(matrix: List[List[int]]) -> int:
    # Get matrix dimensions
    n, m = len(matrix), len(matrix[0])
    # Initialize previous row with first row values
    prev = matrix[0].copy()

    # Process matrix row by row
    for i in range(1, n):
        # Create current row array
        curr = [0] * m
        for j in range(m):
            # Calculate straight up path using previous row
            up = matrix[i][j] + prev[j]

            # Calculate diagonal left path
            left_diag = matrix[i][j]
            if j > 0:  # Check if left diagonal exists
                left_diag += prev[j - 1]
            else:
                left_diag = -math.inf

            # Calculate diagonal right path
            right_diag = matrix[i][j]
            if j < m - 1:  # Check if right diagonal exists
                right_diag += prev[j + 1]
            else:
                right_diag = -math.inf

            # Store maximum path in current row
            curr[j] = max(up, max(left_diag, right_diag))

        # Update previous row with current row values
        prev = curr[:]

    # Return maximum value from final row
    return max(prev)


def main():
    # Test cases
    test_cases = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # Regular case
        [[1, 2, 10], [4, 5, 6], [7, 8, 9]],  # Path with large number
        [[1], [2], [3]],  # Single column matrix
    ]

    for i, matrix in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Recursive Solution: {get_max_path_sum_recursive(matrix)}")
        print(f"Tabulation Solution: {get_max_path_sum_tabulation(matrix)}")
        print(f"Optimized Solution: {get_max_path_sum_optimized(matrix)}")


if __name__ == "__main__":
    main()
