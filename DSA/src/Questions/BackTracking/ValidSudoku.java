package Questions.BackTracking;

/*
 https://leetcode.com/problems/valid-sudoku/description/
 Time Complexity: O(9^(n*n)) where n is the size of the board (9 in this case). This is because each cell can have 9 possible values.
Space Complexity: O(n*n) for the recursion stack and the board itself.

Backtracking Approach:
Use a recursive function solve to try placing digits from 1 to 9 in each empty cell.
For each cell, check if placing a digit is valid by ensuring it does not violate Sudoku rules.
If a valid placement is found, move to the next cell.
If no valid placement is found, backtrack and try the next possible digit.

Validation Function:
isValidPlacement(char[][] board, int row, int col, char num):
This function checks if placing num at (row, col) is valid by ensuring it does not already exist in the same row, column, or 3x3 sub-grid.

Recursive Function:
solve(char[][] board, int row, int col): This function tries to solve the Sudoku starting from (row, col).
Base Case: If row is equal to the board length, the entire board has been filled.
Recursive Case: Try placing each digit from 1 to 9 in the current cell and recursively solve the remaining cells.

Handling Edge Cases:
Skip cells that are already filled.
Move to the next row when the current row is fully filled.
 */
public class ValidSudoku {
    private boolean isValidPlacement(char[][] board, int row, int col, char num) {
        // Check if num is already in the same row, column or 3x3 sub-grid
        for (int i = 0; i < board.length; i++) {
            // Check row
            if (board[i][col] == num) {
                return false;
            }

            // Check column
            if (board[row][i] == num) {
                return false;
            }

            // Check 3x3 sub-grid
            int subGridRow = 3 * (row / 3) + i / 3; // Calculate row index of sub-grid
            int subGridCol = 3 * (col / 3) + i % 3; // Calculate column index of sub-grid

            if (board[subGridRow][subGridCol] == num) {
                return false;
            }
        }

        // Placement is valid
        return true;
    }

    public void solveSudoku(char[][] board) {
        // Start solving sudoku from the first cell
        solve(board, 0, 0);
    }

    private boolean solve(char[][] board, int row, int col) {
        // Base case: If row is equal to board length, entire board has been filled
        if (row == board.length) {
            return true;
        }

        // Move to next row when current row is fully filled
        if (col == board[0].length) {
            return solve(board, row + 1, 0);
        }

        // Skip cells that are already filled
        if (board[row][col] != '.') {
            return solve(board, row, col + 1);
        }

        // Try different numbers in current cell
        for (char num = '1'; num <= '9'; num++) {
            if (isValidPlacement(board, row, col, num)) {
                board[row][col] = num; // Fill current cell with valid number

                // Move to next cell
                if (solve(board, row, col + 1)) {
                    return true;
                }

                // Backtrack to previous state if solution not found
                board[row][col] = '.';
            }
        }

        // No valid solution found
        return false;
    }

    // Time complexity: O(9^(n*n))
    // Space complexity: O(n*n)

    public static void main(String[] args) {
        char[][] board = new char[][] {
                { '5', '3', '.', '.', '7', '.', '.', '.', '.' },
                { '6', '.', '.', '1', '9', '5', '.', '.', '.' },
                { '.', '9', '8', '.', '.', '.', '.', '6', '.' },
                { '8', '.', '.', '.', '6', '.', '.', '.', '3' },
                { '4', '.', '.', '8', '.', '3', '.', '.', '1' },
                { '7', '.', '.', '.', '2', '.', '.', '.', '6' },
                { '.', '6', '.', '.', '.', '.', '2', '8', '.' },
                { '.', '.', '.', '4', '1', '9', '.', '.', '5' },
                { '.', '.', '.', '.', '8', '.', '.', '7', '9' }
        };

        ValidSudoku validSudoku = new ValidSudoku();
        validSudoku.solveSudoku(board);
        for (char[] chars : board) {
            for (char aChar : chars) {
                System.out.print(aChar + " ");
            }
            System.out.println();
        }
    }
}
