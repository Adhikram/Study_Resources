"""
# Question: Matrix Square Finder
# Find largest square submatrix with all 1s

# Time Complexity: O(m*n*log(min(m,n)))
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search on square size
# 2. Check if square exists
# 3. Return maximum size
"""


class MatrixSquareFinder:
    def largest_square(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        left, right = 0, min(m, n)

        def has_square(size: int) -> bool:
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    if self.check_square(matrix, i, j, size):
                        return True
            return False

        while left < right:
            mid = (left + right + 1) >> 1
            if has_square(mid):
                left = mid
            else:
                right = mid - 1

        return left

    def check_square(
        self, matrix: list[list[int]], row: int, col: int, size: int
    ) -> bool:
        for i in range(row, row + size):
            for j in range(col, col + size):
                if matrix[i][j] == 0:
                    return False
        return True


def main():
    solution = MatrixSquareFinder()
    matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(solution.largest_square(matrix))  # Expected: 3


if __name__ == "__main__":
    main()
