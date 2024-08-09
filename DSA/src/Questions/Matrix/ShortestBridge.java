package Questions.Matrix;

import java.util.LinkedList;
import java.util.Queue;
/*
https://leetcode.com/problems/shortest-bridge/description/
 You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
Time Complexity: O(n^2)
Space Complexity: O(n^2)
 */
public class ShortestBridge {
    public int shortestBridge(int[][] grid) {
        int n = grid.length;
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[n][n];
        boolean found = false;

        // Step 1: Find the first island using DFS and mark all its cells
        for (int i = 0; i < n; i++) {
            if (found)
                break;
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    dfs(grid, visited, i, j, queue);
                    found = true;
                    break;
                }
            }
        }

        // Step 2: Use BFS to expand the first island and find the shortest path to the
        // second island
        int steps = 0;
        int[][] directions = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cell = queue.poll();
                for (int[] dir : directions) {
                    int x = cell[0] + dir[0];
                    int y = cell[1] + dir[1];
                    if (x >= 0 && x < n && y >= 0 && y < n && !visited[x][y]) {
                        if (grid[x][y] == 1) {
                            return steps; // Reached the second island
                        }
                        queue.offer(new int[] { x, y });
                        visited[x][y] = true;
                    }
                }
            }
            steps++;
        }

        return -1; // This should never be reached as per problem constraints
    }

    private void dfs(int[][] grid, boolean[][] visited, int i, int j, Queue<int[]> queue) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || visited[i][j] || grid[i][j] == 0) {
            return;
        }
        visited[i][j] = true;
        queue.offer(new int[] { i, j });
        dfs(grid, visited, i + 1, j, queue);
        dfs(grid, visited, i - 1, j, queue);
        dfs(grid, visited, i, j + 1, queue);
        dfs(grid, visited, i, j - 1, queue);
    }
    public static void main(String[] args) {
        ShortestBridge obj = new ShortestBridge();
        int[][] grid = { { 0, 1 }, { 1, 0 } };
        System.out.println(obj.shortestBridge(grid)); // Output: 1

        grid = new int[][] { { 0, 1, 0 }, { 0, 0, 0 }, { 0, 0, 1 } };
        System.out.println(obj.shortestBridge(grid)); // Output: 2

        grid = new int[][] { { 1, 1, 1, 1, 1 }, { 1, 0, 0, 0, 1 }, { 1, 0, 1, 0, 1 }, { 1, 0, 0, 0, 1 },
                { 1, 1, 1, 1, 1 } };
        System.out.println(obj.shortestBridge(grid)); // Output: 1
    }
}
