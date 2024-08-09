package Questions.Matrix;

import java.util.LinkedList;
import java.util.Queue;

/*
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
 Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
Time Complexity: O(n^2)
Space Complexity: O(n^2)
 */
public class ShortestPathInBinaryMatrix {
    private static final int[][] DIRECTIONS = {
            { -1, -1 }, { -1, 0 }, { -1, 1 },
            { 0, -1 }, { 0, 1 },
            { 1, -1 }, { 1, 0 }, { 1, 1 }
    };

    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;

        // Edge case: start or end point is blocked
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) {
            return -1;
        }

        // BFS initialization
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] { 0, 0 });
        grid[0][0] = 1; // Mark the start cell as visited

        int pathLength = 1;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cell = queue.poll();
                int row = cell[0];
                int col = cell[1];

                // If we have reached the bottom-right corner, return the path length
                if (row == n - 1 && col == n - 1) {
                    return pathLength;
                }

                // Explore all 8 directions
                for (int[] direction : DIRECTIONS) {
                    int newRow = row + direction[0];
                    int newCol = col + direction[1];

                    // Check if the new position is within bounds and unvisited
                    if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < n && grid[newRow][newCol] == 0) {
                        queue.add(new int[] { newRow, newCol });
                        grid[newRow][newCol] = 1; // Mark new cell as visited
                    }
                }
            }
            pathLength++;
        }

        // If we exit the loop, it means there is no path to the bottom-right corner
        return -1;

    }

    public static void main(String[] args) {
        ShortestPathInBinaryMatrix obj = new ShortestPathInBinaryMatrix();

        int[][] grid1 = {
                { 0, 1 },
                { 1, 0 }
        };
        System.out.println(obj.shortestPathBinaryMatrix(grid1)); // Output: 2

        int[][] grid2 = {
                { 0, 0, 0 },
                { 1, 1, 0 },
                { 1, 1, 0 }
        };
        System.out.println(obj.shortestPathBinaryMatrix(grid2)); // Output: 4

        int[][] grid3 = {
                { 1, 0, 0 },
                { 1, 1, 0 },
                { 1, 1, 0 }
        };
        System.out.println(obj.shortestPathBinaryMatrix(grid3)); // Output: -1
    }
}
