package Questions.BackTracking;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.HashSet;

/*
https://leetcode.com/problems/n-queens-ii/
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9
*/
public class NQueens2 {
    public int totalNQueens(int n) {
        // Array to keep track of the position of queens in each row
        int[] queens = new int[n];
        int[] count = new int[1];
        // Call the backtracking function starting from the first row
        backtrack(queens, 0, n, count);
        return count[0];
    }

    private void backtrack(int[] queens, int row, int n, int[] count) {
        // If all rows are filled, we found a valid solution
        if (row == n) {
            count[0]++;
            return;
        }
        // Try placing a queen in each column of the current row
        for (int col = 0; col < n; col++) {
            if (isSafe(queens, row, col)) {
                // Place the queen in the current position
                queens[row] = col;
                // Move to the next row
                backtrack(queens, row + 1, n, count);
                // Backtrack: remove the queen from the current position
                queens[row] = 0;
            }
        }
    }

    private boolean isSafe(int[] queens, int row, int col) {
        // Check if the current position is safe to place a queen
        for (int i = 0; i < row; i++) {
            int placedQueenCol = queens[i];
            // Check if the current column or diagonals are under attack
            if (placedQueenCol == col ||
                    placedQueenCol - i == col - row ||
                    placedQueenCol + i == col + row) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        NQueens2 nQueens2 = new NQueens2();
        System.out.println(nQueens2.totalNQueens(4));
    }

}
