"""
# Question: Rotate Image
# Link: https://leetcode.com/problems/rotate-image/

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Algorithm:
# 1. Transpose matrix (swap across diagonal)
# 2. Reverse each row
# 3. Complete rotation in-place
"""


class Rotate90:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        # Transpose matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1


def main():
    solution = Rotate90()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(matrix)
    print(matrix)  # Expected: [[7,4,1],[8,5,2],[9,6,3]]


if __name__ == "__main__":
    main()
