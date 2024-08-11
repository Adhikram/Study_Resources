package Questions.DP;

import java.util.Arrays;

/*
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
 You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:


Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:


Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.
 
 */
public class ShortestPathWithObstaclesElimination {
    public int shortestPath(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;

        if (grid[0][0] == 1 || grid[m - 1][n - 1] == 1)
            return -1;

        if (k >= m + n - 2) {
            return m + n - 2;
        }

        int[][][] dp = new int[m][n][k + 1];
        for (int[][] i : dp) {
            for (int[] j : i) {
                Arrays.fill(j, Integer.MAX_VALUE);
            }
        }

        int res = dfs(grid, 0, 0, k, dp);
        return res == Integer.MAX_VALUE ? -1 : res;

    }

    private int dfs(int[][] grid, int i, int j, int k, int[][][] dp) {
        int m = grid.length;
        int n = grid[0].length;
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == -1)
            return Integer.MAX_VALUE - 1;

        if (i == m - 1 && j == n - 1) {
            // Reached the target
            return 0;

        }
        if (dp[i][j][k] != Integer.MAX_VALUE) {
            // This means we have visited this cell before
            return dp[i][j][k];
        }

        if (k >= (m - i - 1) + (n - j - 1)) {
            // The quota is larger or equal to the manhattanDistance. We can just stop here.
            return dp[i][j][k] = (m - i - 1) + (n - j - 1);
        }

        if (grid[i][j] == 1 && k-- <= 0) {
            // Cur is an obstacle but not enough quota.
            return Integer.MAX_VALUE - 1;
        }

        int temp = grid[i][j];
        grid[i][j] = -1;
        int left = dfs(grid, i - 1, j, k, dp);
        int right = dfs(grid, i + 1, j, k, dp);
        int up = dfs(grid, i, j - 1, k, dp);
        int down = dfs(grid, i, j + 1, k, dp);
        grid[i][j] = temp; // Backtrack;
        dp[i][j][k] = 1 + Math.min(left, Math.min(right, Math.min(up, down)));
        return dp[i][j][k];
    }

    public static void main(String[] args) {
        ShortestPathWithObstaclesElimination shortestPathWithObstaclesElimination = new ShortestPathWithObstaclesElimination();
        int[][] grid = new int[][]{{0, 0, 0}, {1, 1, 0}, {0, 0, 0}, {0, 1, 1}, {0, 0, 0}};
        int k = 1;
        System.out.println(shortestPathWithObstaclesElimination.shortestPath(grid, k));
    }
}
