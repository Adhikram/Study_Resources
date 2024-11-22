"""
# Question: Row with Maximum Ones
# Problem Statement:
# Given a boolean 2D array where each row is sorted, find the row with the maximum number of 1s.

# Example:
# Input: matrix = [
#     [0,1,1,1],
#     [0,0,1,1],
#     [1,1,1,1],
#     [0,0,0,0]
# ]
# Output: 2
# Explanation: Row 2 contains maximum number of 1s (4 ones)
"""

from typing import List


class RowWithMax1s:
    def find_row_binary(self, matrix: List[List[int]]) -> int:
        """
        Binary search approach
        Time Complexity: O(m * log n)
        Space Complexity: O(1)
        """
        if not matrix or not matrix[0]:
            return -1

        max_ones = 0
        result_row = -1
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            left, right = 0, n - 1
            first_one = n  # Position of first 1

            while left <= right:
                mid = (left + right) >> 1
                if matrix[i][mid] == 1:
                    first_one = mid
                    right = mid - 1
                else:
                    left = mid + 1

            ones_count = n - first_one
            if ones_count > max_ones:
                max_ones = ones_count
                result_row = i

        return result_row

    def find_row_optimal(self, matrix: List[List[int]]) -> int:
        """
        Optimal approach starting from top-right
        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        if not matrix or not matrix[0]:
            return -1

        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        max_row = -1

        while row < m and col >= 0:
            if matrix[row][col] == 1:
                max_row = row
                col -= 1
            else:
                row += 1

        return max_row

    def find_row_linear(self, matrix: List[List[int]]) -> int:
        """
        Linear counting approach
        Time Complexity: O(m * n)
        Space Complexity: O(1)
        """
        if not matrix or not matrix[0]:
            return -1

        max_ones = 0
        result_row = -1

        for i in range(len(matrix)):
            ones = sum(matrix[i])
            if ones > max_ones:
                max_ones = ones
                result_row = i

        return result_row


def main():
    test_cases = [
        {
            "matrix": [[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]],
            "expected": 2,
        },
        {"matrix": [[0, 0], [1, 1], [0, 0]], "expected": 1},
        {"matrix": [[0, 0], [0, 0]], "expected": -1},
    ]

    solution = RowWithMax1s()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Matrix: {test['matrix']}")

        result_binary = solution.find_row_binary(test["matrix"])
        result_optimal = solution.find_row_optimal(test["matrix"])
        result_linear = solution.find_row_linear(test["matrix"])

        print(f"Binary Search Result: {result_binary}")
        print(f"Optimal Result: {result_optimal}")
        print(f"Linear Search Result: {result_linear}")
        print(f"Expected: {test['expected']}")

        assert result_binary == result_optimal == result_linear == test["expected"]


if __name__ == "__main__":
    main()
