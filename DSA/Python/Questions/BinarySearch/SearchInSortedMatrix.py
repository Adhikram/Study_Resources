"""
# Question: Search in Sorted Matrix
# Link: https://leetcode.com/problems/search-a-2d-matrix/

# Problem Statement:
# Write an efficient algorithm to search for a value target in an m x n matrix.
# Matrix properties:
# - Integers in each row are sorted from left to right
# - The first integer of each row is greater than the last integer of the previous row

# Example:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
"""

from typing import List


class SearchInSortedMatrix:
    def search_binary_2d(self, matrix: List[List[int]], target: int) -> bool:
        """
        Binary search treating matrix as 1D array
        Time Complexity: O(log(m*n))
        Space Complexity: O(1)
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) >> 1
            row, col = mid // n, mid % n
            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def search_row_col(self, matrix: List[List[int]], target: int) -> bool:
        """
        Row and column binary search approach
        Time Complexity: O(log m + log n)
        Space Complexity: O(1)
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        # Search for potential row
        top, bottom = 0, m - 1
        while top <= bottom:
            mid = (top + bottom) >> 1
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                # Search in the row
                left, right = 0, n - 1
                while left <= right:
                    col_mid = (left + right) >> 1
                    if matrix[mid][col_mid] == target:
                        return True
                    elif matrix[mid][col_mid] < target:
                        left = col_mid + 1
                    else:
                        right = col_mid - 1
                return False
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1

        return False

    def search_linear(self, matrix: List[List[int]], target: int) -> bool:
        """
        Linear search approach (for comparison)
        Time Complexity: O(m*n)
        Space Complexity: O(1)
        """
        for row in matrix:
            for value in row:
                if value == target:
                    return True
        return False


def main():
    test_cases = [
        {
            "matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            "target": 3,
            "expected": True,
        },
        {
            "matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            "target": 13,
            "expected": False,
        },
        {"matrix": [[1]], "target": 1, "expected": True},
    ]

    solution = SearchInSortedMatrix()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Matrix: {test['matrix']}")
        print(f"Target: {test['target']}")

        result_binary = solution.search_binary_2d(test["matrix"], test["target"])
        result_row_col = solution.search_row_col(test["matrix"], test["target"])
        result_linear = solution.search_linear(test["matrix"], test["target"])

        print(f"Binary Search Result: {result_binary}")
        print(f"Row-Col Search Result: {result_row_col}")
        print(f"Linear Search Result: {result_linear}")
        print(f"Expected: {test['expected']}")

        assert result_binary == result_row_col == result_linear == test["expected"]


if __name__ == "__main__":
    main()
