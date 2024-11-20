"""
# Question: Search a 2D Matrix II
# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/

# Time Complexity: O(m + n)
# Space Complexity: O(1)

# Algorithm:
# 1. Start from top right corner
# 2. Move left if current > target
# 3. Move down if current < target
"""


class SearchIn2DMatrixII:
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
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


def main():
    solution = SearchIn2DMatrixII()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    target = 5
    print(solution.search_matrix(matrix, target))  # Expected: True


if __name__ == "__main__":
    main()
