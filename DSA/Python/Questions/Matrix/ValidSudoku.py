"""
# Question: Valid Sudoku
# Link: https://leetcode.com/problems/valid-sudoku/

# Time Complexity: O(1)
# Space Complexity: O(1)

# Algorithm:
# 1. Check each row for duplicates
# 2. Check each column for duplicates
# 3. Check each 3x3 box for duplicates
# 4. Return validity status
"""


class ValidSudoku:
    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue

                box_index = (i // 3) * 3 + j // 3

                # Check if number already exists
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False

                # Add number to sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        return True


def main():
    solution = ValidSudoku()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(solution.is_valid_sudoku(board))  # Expected: True


if __name__ == "__main__":
    main()
