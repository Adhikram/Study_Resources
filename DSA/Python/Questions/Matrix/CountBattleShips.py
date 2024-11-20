"""
# Question: Count Battleships
# Link: https://leetcode.com/problems/battleships-in-a-board/

# Time Complexity: O(m*n)
# Space Complexity: O(1)

# Algorithm:
# 1. Count only the start of each battleship
# 2. Check for valid battleship positions
# 3. Avoid counting middle or end parts
# 4. Return total count
"""


class CountBattleShips:
    def count_battleships(self, board: list[list[str]]) -> int:
        count = 0
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    # Check if it's the start of a battleship
                    if (i == 0 or board[i - 1][j] == ".") and (
                        j == 0 or board[i][j - 1] == "."
                    ):
                        count += 1

        return count


def main():
    solution = CountBattleShips()
    board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
    print(solution.count_battleships(board))  # Expected: 2


if __name__ == "__main__":
    main()
