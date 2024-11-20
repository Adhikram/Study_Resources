"""
# Question: Diagonal Traverse
# Link: https://leetcode.com/problems/diagonal-traverse/

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

# Algorithm:
# 1. Track direction (up/down)
# 2. Process each diagonal
# 3. Handle boundary conditions
# 4. Return traversal result
"""


class DiagonalTraversal:
    def find_diagonal_order(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        result = []
        row = col = 0
        direction = 1  # 1 for up, -1 for down

        while len(result) < m * n:
            result.append(matrix[row][col])

            if direction == 1:
                if col == n - 1:
                    row += 1
                    direction = -1
                elif row == 0:
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            else:
                if row == m - 1:
                    col += 1
                    direction = 1
                elif col == 0:
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1

        return result


def main():
    solution = DiagonalTraversal()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.find_diagonal_order(matrix))


if __name__ == "__main__":
    main()
