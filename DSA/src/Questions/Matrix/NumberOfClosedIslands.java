package Questions.Matrix;

/*
https://leetcode.com/problems/number-of-closed-islands/description/
 Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
Time Complexity: O(m * n)
Space Complexity: O(m * n)
 */
public class NumberOfClosedIslands {
    public int closedIsland(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int closedIslandsCount = 0;

        // Traverse the grid
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // Start a DFS if we find an unvisited land cell
                if (grid[i][j] == 0) {
                    // If the DFS returns true, it is a closed island
                    if (isClosedIsland(grid, i, j)) {
                        closedIslandsCount++;
                    }
                }
            }
        }

        return closedIslandsCount;
    }

    private boolean isClosedIsland(int[][] grid, int i, int j) {
        int rows = grid.length;
        int cols = grid[0].length;

        // If this cell is out of bounds or is water, return true
        if (i < 0 || i >= rows || j < 0 || j >= cols) {
            return false;
        }

        // If this cell is already water, return true
        if (grid[i][j] == 1) {
            return true;
        }

        // If this cell is on the boundary, it's not a closed island
        if (i == 0 || i == rows - 1 || j == 0 || j == cols - 1) {
            return false;
        }

        // Mark the current cell as visited by making it water
        grid[i][j] = 1;

        // Recursively check the four directions
        boolean up = isClosedIsland(grid, i - 1, j);
        boolean down = isClosedIsland(grid, i + 1, j);
        boolean left = isClosedIsland(grid, i, j - 1);
        boolean right = isClosedIsland(grid, i, j + 1);

        // A cell is part of a closed island if all its neighboring cells are
        return up && down && left && right;
    }

    public static void main(String[] args) {
        NumberOfClosedIslands solution = new NumberOfClosedIslands();
        int[][] grid = {
                { 1, 1, 1, 1, 1, 1, 1, 0 },
                { 1, 0, 0, 0, 0, 1, 1, 0 },
                { 1, 0, 1, 0, 1, 1, 1, 0 },
                { 1, 0, 0, 0, 0, 1, 0, 1 },
                { 1, 1, 1, 1, 1, 1, 1, 0 }
        };
        System.out.println(solution.closedIsland(grid)); // Output: 2
    }

}
