"""
# Question: Design Tic-Tac-Toe
# Link: https://leetcode.com/problems/design-tic-tac-toe/

# Time Complexity: O(1) per move
# Space Complexity: O(n)

# Algorithm:
# 1. Track row and column sums
# 2. Track diagonal sums
# 3. Check win conditions
# 4. Return winner or ongoing status
"""


class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        current_player = 1 if player == 1 else -1

        # Update row and column
        self.rows[row] += current_player
        self.cols[col] += current_player

        # Update diagonals
        if row == col:
            self.diagonal += current_player
        if row + col == self.n - 1:
            self.anti_diagonal += current_player

        # Check win condition
        if (
            abs(self.rows[row]) == self.n
            or abs(self.cols[col]) == self.n
            or abs(self.diagonal) == self.n
            or abs(self.anti_diagonal) == self.n
        ):
            return player

        return 0


def main():
    toe = TicTacToe(3)
    print(toe.move(0, 0, 1))  # Expected: 0
    print(toe.move(0, 2, 2))  # Expected: 0
    print(toe.move(2, 2, 1))  # Expected: 0
    print(toe.move(1, 1, 2))  # Expected: 0
    print(toe.move(2, 0, 1))  # Expected: 0
    print(toe.move(1, 0, 2))  # Expected: 0
    print(toe.move(2, 1, 1))  # Expected: 1


if __name__ == "__main__":
    main()
