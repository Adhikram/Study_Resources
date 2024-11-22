"""
# Question: Search a 2D Matrix II
# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/

# Problem Statement:
# Write an efficient algorithm that searches for a target value in an m x n integer matrix.
# The matrix has the following properties:
# - Integers in each row are sorted in ascending from left to right.
# - Integers in each column are sorted in ascending from top to bottom.

# Example:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22]], target = 5
# Output: true
"""

from typing import List


class SearchIn2DMatrixII:
    def search_matrix_optimal(self, matrix: List[List[int]], target: int) -> bool:
        """
        Start from top-right corner approach
        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False

    def search_matrix_binary(self, matrix: List[List[int]], target: int) -> bool:
        """
        Binary search on each row
        Time Complexity: O(m * log n)
        Space Complexity: O(1)
        """
        if not matrix or not matrix[0]:
            return False

        for row in matrix:
            left, right = 0, len(row) - 1
            while left <= right:
                mid = (left + right) >> 1
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

    def search_matrix_divide_conquer(
        self, matrix: List[List[int]], target: int
    ) -> bool:
        """
        Divide and conquer approach
        Time Complexity: O(n^log n)
        Space Complexity: O(log n)
        """

        def search_submatrix(left: int, right: int, top: int, bottom: int) -> bool:
            if left > right or top > bottom:
                return False
            if target < matrix[top][left] or target > matrix[bottom][right]:
                return False

            mid = (left + right) >> 1

            row = top
            while row <= bottom and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1

            return search_submatrix(left, mid - 1, row, bottom) or search_submatrix(
                mid + 1, right, top, row - 1
            )

        if not matrix or not matrix[0]:
            return False

        return search_submatrix(0, len(matrix[0]) - 1, 0, len(matrix) - 1)


def main():
    test_cases = [
        {
            "matrix": [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22]],
            "target": 5,
            "expected": True,
        },
        {
            "matrix": [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22]],
            "target": 20,
            "expected": False,
        },
    ]

    solution = SearchIn2DMatrixII()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Matrix: {test['matrix']}")
        print(f"Target: {test['target']}")

        result_optimal = solution.search_matrix_optimal(test["matrix"], test["target"])
        result_binary = solution.search_matrix_binary(test["matrix"], test["target"])
        result_divide_conquer = solution.search_matrix_divide_conquer(
            test["matrix"], test["target"]
        )

        print(f"Optimal Result: {result_optimal}")
        print(f"Binary Search Result: {result_binary}")
        print(f"Divide & Conquer Result: {result_divide_conquer}")
        print(f"Expected: {test['expected']}")

        assert (
            result_optimal == result_binary == result_divide_conquer == test["expected"]
        )


if __name__ == "__main__":
    main()
