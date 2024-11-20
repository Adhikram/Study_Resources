"""
# Question: Row with Maximum Ones
# Find row with maximum number of 1s in sorted binary matrix

# Time Complexity: O(m + n)
# Space Complexity: O(1)

# Algorithm:
# 1. Start from top right
# 2. Move left when 1 is found
# 3. Move down when 0 is found
"""


class RowWithMax1s:
    def row_with_max_1s(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return -1

        m, n = len(matrix), len(matrix[0])
        row = 0
        col = n - 1
        max_row = -1

        while row < m and col >= 0:
            if matrix[row][col] == 1:
                max_row = row
                col -= 1
            else:
                row += 1

        return max_row


def main():
    solution = RowWithMax1s()
    matrix = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
    print(solution.row_with_max_1s(matrix))  # Expected: 2


if __name__ == "__main__":
    main()
