"""
# Question: Largest Submatrix With Rearrangements
# Link: https://leetcode.com/problems/largest-submatrix-with-rearrangements/

# Time Complexity: O(m*n*log(n))
# Space Complexity: O(n)

# Algorithm:
# 1. Calculate consecutive ones for each column
# 2. Sort each row in descending order
# 3. Find maximum area for each row
# 4. Return largest possible rectangle
"""


class LargestSubMatrixWithRearrangements:
    def largest_submatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0

        # Calculate heights (consecutive ones)
        for j in range(n):
            for i in range(1, m):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        # Process each row
        for i in range(m):
            # Sort current row in descending order
            curr_row = sorted(matrix[i], reverse=True)

            # Calculate maximum area for current row
            for j in range(n):
                max_area = max(max_area, curr_row[j] * (j + 1))

        return max_area


def main():
    solution = LargestSubMatrixWithRearrangements()
    matrix = [[0, 0, 1], [1, 1, 1], [1, 0, 1]]
    print(solution.largest_submatrix(matrix))  # Expected: 4


if __name__ == "__main__":
    main()
