"""
# Question: N-Queens II
# Link: https://leetcode.com/problems/n-queens-ii/

# Count total number of distinct N-Queens solutions

# Time Complexity: O(N!)
# Space Complexity: O(N)

# Algorithm:
# 1. Use backtracking to try queen placements
# 2. Track queen positions in each row
# 3. Validate diagonal and column conflicts
# 4. Count valid solutions

# Key Components:
# - total_n_queens(): Main solution counter
# - backtrack(): Recursive helper for queen placement
# - is_safe(): Position validation checker
"""


class NQueens2:
    def total_n_queens(self, n: int) -> int:
        queens = [0] * n
        count = [0]

        def is_safe(queens: list, row: int, col: int) -> bool:
            for i in range(row):
                placed_queen_col = queens[i]
                if (
                    placed_queen_col == col
                    or placed_queen_col - i == col - row
                    or placed_queen_col + i == col + row
                ):
                    return False
            return True

        def backtrack(queens: list, row: int, n: int, count: list):
            if row == n:
                count[0] += 1
                return

            for col in range(n):
                if is_safe(queens, row, col):
                    queens[row] = col
                    backtrack(queens, row + 1, n, count)
                    queens[row] = 0

        backtrack(queens, 0, n, count)
        return count[0]


def main():
    solution = NQueens2()
    print(solution.total_n_queens(4))  # Expected output: 2


if __name__ == "__main__":
    main()
