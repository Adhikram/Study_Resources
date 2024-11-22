"""
# Question: Matrix Square Finder
# Problem Statement:
# Find the largest square submatrix containing all 1s in a binary matrix.

# Example:
# Input: matrix = [
#     [1,1,1],
#     [1,1,1],
#     [1,1,1]
# ]
# Output: 3
# Explanation: The entire matrix forms a 3x3 square of 1s
"""

from typing import List


class MatrixSquareFinder:
    def largest_square_binary(self, matrix: List[List[int]]) -> int:
        """
        Binary search approach
        Time Complexity: O(m*n*log(min(m,n)))
        Space Complexity: O(1)
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        left, right = 0, min(m, n)

        while left < right:
            mid = (left + right + 1) >> 1
            if self.has_square(matrix, mid):
                left = mid
            else:
                right = mid - 1

        return left

    def has_square(self, matrix: List[List[int]], size: int) -> bool:
        """Helper function to check if square of given size exists"""
        m, n = len(matrix), len(matrix[0])
        for i in range(m - size + 1):
            for j in range(n - size + 1):
                if self.check_square(matrix, i, j, size):
                    return True
        return False

    def check_square(
        self, matrix: List[List[int]], row: int, col: int, size: int
    ) -> bool:
        """Helper function to verify if square at given position is valid"""
        for i in range(row, row + size):
            for j in range(col, col + size):
                if matrix[i][j] == 0:
                    return False
        return True

    def largest_square_dp(self, matrix: List[List[int]]) -> int:
        """
        Dynamic programming approach
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_size = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_size = max(max_size, dp[i][j])

        return max_size

    def largest_square_optimized(self, matrix: List[List[int]]) -> int:
        """
        Space optimized approach using two rows
        Time Complexity: O(m*n)
        Space Complexity: O(n)
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        prev = [0] * (n + 1)
        max_size = 0

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 1:
                    curr[j] = min(prev[j], curr[j - 1], prev[j - 1]) + 1
                    max_size = max(max_size, curr[j])
            prev = curr

        return max_size


def main():
    test_cases = [
        {"matrix": [[1, 1, 1], [1, 1, 1], [1, 1, 1]], "expected": 3},
        {"matrix": [[1, 0, 1], [1, 1, 0], [1, 1, 0]], "expected": 1},
        {"matrix": [[0, 1], [1, 0]], "expected": 1},
    ]

    solution = MatrixSquareFinder()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Matrix: {test['matrix']}")

        result_binary = solution.largest_square_binary(test["matrix"])
        result_dp = solution.largest_square_dp(test["matrix"])
        result_optimized = solution.largest_square_optimized(test["matrix"])

        print(f"Binary Search Result: {result_binary}")
        print(f"DP Result: {result_dp}")
        print(f"Optimized Result: {result_optimized}")
        print(f"Expected: {test['expected']}")

        assert result_binary == result_dp == result_optimized == test["expected"]


if __name__ == "__main__":
    main()
