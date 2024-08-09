package Questions.Matrix;

import Interview.Solution;

/*
https://leetcode.com/problems/battleships-in-a-board/description/
 Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

 

Example 1:


Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Example 2:

Input: board = [["."]]
Output: 0
Time Complexity: O(m * n)
Space Complexity: O(1)
 */
public class CountBattleShips {
    public static int countBattleships(char[][] board) {
        int count = 0;
        int m = board.length;
        int n = board[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // If the cell is 'X' and is the head of a battleship
                if (board[i][j] == 'X') {
                    if (i > 0 && board[i - 1][j] == 'X')
                        continue; // Check above
                    if (j > 0 && board[i][j - 1] == 'X')
                        continue; // Check left
                    count++;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        char[][] board1 = {
                { 'X', '.', '.', 'X' },
                { '.', '.', '.', 'X' },
                { '.', '.', '.', 'X' }
        };
        System.out.println(countBattleships(board1)); // Output: 2

        char[][] board2 = {
                { '.' }
        };
        System.out.println(countBattleships(board2)); // Output: 0
    }

}
