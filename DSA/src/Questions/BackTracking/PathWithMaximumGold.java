package Questions.BackTracking;

/*
https://leetcode.com/problems/path-with-maximum-gold/description/
 In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
Time Complexity: O(4^(m*n)) because each cell can lead to four possible directions and we explore all possible paths.
Space Complexity: O(m*n) for the recursion stack.
 */
public class PathWithMaximumGold {
    private int[] dx = { 0, 0, 1, -1 }; // directions for row movement
    private int[] dy = { 1, -1, 0, 0 }; // directions for column movement

    public int getMaximumGold(int[][] grid) {
        int maxGold = 0;
        int m = grid.length;
        int n = grid[0].length;

        // Try to start from each cell containing gold
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 0) {
                    maxGold = Math.max(maxGold, collectGold(grid, i, j, m, n));
                }
            }
        }

        return maxGold;
    }

    private int collectGold(int[][] grid, int x, int y, int m, int n) {
        if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == 0) {
            return 0;
        }

        // Collect the gold at the current cell
        int gold = grid[x][y];
        grid[x][y] = 0; // mark as visited by setting it to 0

        int maxGold = 0;
        for (int i = 0; i < 4; i++) {
            int newX = x + dx[i];
            int newY = y + dy[i];
            maxGold = Math.max(maxGold, collectGold(grid, newX, newY, m, n));
        }

        // Backtrack: restore the cell's value
        grid[x][y] = gold;

        return maxGold + gold;
    }

    public static void main(String[] args) {
        PathWithMaximumGold pathWithMaximumGold = new PathWithMaximumGold();
        System.out.println(pathWithMaximumGold.getMaximumGold(new int[][] { { 0, 6, 0 }, { 5, 8, 7 }, { 0, 9, 0 } }));
        System.out.println(pathWithMaximumGold
                .getMaximumGold(new int[][] { { 1, 0, 7 }, { 2, 0, 6 }, { 3, 4, 5 }, { 0, 3, 0 }, { 9, 0, 20 } }));
    }

}
