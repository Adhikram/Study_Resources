"""
# Question: Game of Life
# Link: https://leetcode.com/problems/game-of-life/

# Time Complexity: O(m*n)
# Space Complexity: O(1)

# Algorithm:
# 1. Use state transitions (2: live->dead, 3: dead->live)
# 2. Count live neighbors for each cell
# 3. Apply game rules in-place
# 4. Update final states
"""


class GameOfLife:
    def game_of_life(self, board: list[list[int]]) -> None:
        m, n = len(board), len(board[0])
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        # First pass: mark transitions
        for i in range(m):
            for j in range(n):
                live_neighbors = 0

                # Count live neighbors
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        if board[ni][nj] in [1, 2]:
                            live_neighbors += 1

                # Apply rules
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2  # live to dead
                else:
                    if live_neighbors == 3:
                        board[i][j] = 3  # dead to live

        # Second pass: update states
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1


def main():
    solution = GameOfLife()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    solution.game_of_life(board)
    print(board)


if __name__ == "__main__":
    main()
