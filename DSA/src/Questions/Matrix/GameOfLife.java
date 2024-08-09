package Questions.Matrix;

import java.util.Arrays;

/*
https://leetcode.com/problems/game-of-life/description/
 According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
Time Complexity: O(m * n)
Space Complexity: O(1)
 
*/
public class GameOfLife {
    private static final int[][] DIRECTIONS = {
            { -1, -1 }, { -1, 0 }, { -1, 1 },
            { 0, -1 }, { 0, 1 },
            { 1, -1 }, { 1, 0 }, { 1, 1 }
    };

    public void gameOfLife(int[][] board) {
        int m = board.length, n = board[0].length;

        // Step 1: Compute and store the next state in 2-bit encoded form
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int liveNeighbors = countLiveNeighbors(board, i, j, m, n);

                // Rule 1 & Rule 3: Cell dies
                if (board[i][j] == 1 && (liveNeighbors < 2 || liveNeighbors > 3)) {
                    // 01: live cell becomes dead
                    board[i][j] = 1;
                }
                // Rule 2: Cell stays alive
                else if (board[i][j] == 1 && (liveNeighbors == 2 || liveNeighbors == 3)) {
                    // 11: live cell remains alive
                    board[i][j] = 3;
                }
                // Rule 4: Cell becomes alive
                else if (board[i][j] == 0 && liveNeighbors == 3) {
                    // 10: dead cell becomes alive
                    board[i][j] = 2;
                }
            }
        }

        // Step 2: Update the board with the new state
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] >>= 1; // Right shift to get the next state
            }
        }
    }

    private int countLiveNeighbors(int[][] board, int row, int col, int m, int n) {
        int count = 0;
        for (int[] dir : DIRECTIONS) {
            int newRow = row + dir[0];
            int newCol = col + dir[1];
            if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n) {
                count += board[newRow][newCol] & 1; // Extract the least significant bit
            }
        }
        return count;
    }

    public static void main(String[] args) {
        GameOfLife obj = new GameOfLife();
        int[][] board = {
                { 0, 1, 0 },
                { 0, 0, 1 },
                { 1, 1, 1 },
                { 0, 0, 0 }
        };
        obj.gameOfLife(board);
        for (int[] row : board) {
            System.out.println(Arrays.toString(row));
        }
    }
}
