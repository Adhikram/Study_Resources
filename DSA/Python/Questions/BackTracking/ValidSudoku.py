"""
# Question: Valid Sudoku
# Link: https://leetcode.com/problems/valid-sudoku/

# Solve a Sudoku puzzle using backtracking

# Time Complexity: O(9^(n*n))
# Space Complexity: O(n*n)

# Algorithm:
# 1. Try placing digits 1-9 in empty cells
# 2. Validate row, column, and 3x3 box constraints
# 3. Recursively solve remaining cells
# 4. Backtrack if no valid placement found

# Key Components:
# - solve_sudoku(): Main solver implementation
# - is_valid_placement(): Validator for number placement
# - solve(): Recursive helper for board filling
"""

class ValidSudoku:
    def is_valid_placement(self, board: list[list[str]], row: int, col: int, num: str) -> bool:
        for i in range(9):
            # Check row
            if board[i][col] == num:
                return False
                
            # Check column
            if board[row][i] == num:
                return False
                
            # Check 3x3 sub-grid
            sub_grid_row = 3 * (row // 3) + i // 3
            sub_grid_col = 3 * (col // 3) + i % 3
            
            if board[sub_grid_row][sub_grid_col] == num:
                return False
                
        return True
        
    def solve_sudoku(self, board: list[list[str]]) -> None:
        self.solve(board, 0, 0)
        
    def solve(self, board: list[list[str]], row: int, col: int) -> bool:
        if row == 9:
            return True
            
        if col == 9:
            return self.solve(board, row + 1, 0)
            
        if board[row][col] != '.':
            return self.solve(board, row, col + 1)
            
        for num in '123456789':
            if self.is_valid_placement(board, row, col, num):
                board[row][col] = num
                
                if self.solve(board, row, col + 1):
                    return True
                    
                board[row][col] = '.'
                
        return False

def main():
    solution = ValidSudoku()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    solution.solve_sudoku(board)
    for row in board:
        print(" ".join(row))

if __name__ == "__main__":
    main()
