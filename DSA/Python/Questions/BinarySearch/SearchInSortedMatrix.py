"""
# Question: Search in Sorted Matrix
# Link: https://leetcode.com/problems/search-a-2d-matrix/

# Time Complexity: O(log(m*n))
# Space Complexity: O(1)

# Algorithm:
# 1. Treat matrix as 1D sorted array
# 2. Convert 1D index to 2D coordinates
# 3. Perform binary search
"""


class SearchInSortedMatrix:
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
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


def main():
    solution = SearchInSortedMatrix()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(solution.search_matrix(matrix, target))  # Expected: True


if __name__ == "__main__":
    main()
