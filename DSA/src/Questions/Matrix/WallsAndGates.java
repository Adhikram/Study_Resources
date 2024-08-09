package Questions.Matrix;

import java.util.LinkedList;
import java.util.Queue;

/*
https://leetcode.com/problems/walls-and-gates/description/
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
 

Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
Tine Complexity: O(m * n)
Space Complexity: O(m * n)
 */
public class WallsAndGates {
    private static final int INF = 2147483647;
    private static final int[][] DIRECTIONS = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };

    public void wallsAndGates(int[][] rooms) {
        int m = rooms.length;
        int n = rooms[0].length;
        Queue<int[]> queue = new LinkedList<>();

        // Step 1: Initialize the queue with all gate positions.
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (rooms[i][j] == 0) {
                    queue.offer(new int[] { i, j });
                }
            }
        }

        // Step 2: Perform BFS from all gates simultaneously.
        while (!queue.isEmpty()) {
            int[] point = queue.poll();
            int row = point[0];
            int col = point[1];

            for (int[] direction : DIRECTIONS) {
                int newRow = row + direction[0];
                int newCol = col + direction[1];

                // Check if the new position is valid and is an empty room (INF)
                if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n && rooms[newRow][newCol] == INF) {
                    rooms[newRow][newCol] = rooms[row][col] + 1; // Update distance
                    queue.offer(new int[] { newRow, newCol }); // Enqueue new position
                }
            }
        }
    }

    public static void main(String[] args) {
        WallsAndGates solution = new WallsAndGates();
        int[][] rooms = {
                { 2147483647, -1, 0, 2147483647 },
                { 2147483647, 2147483647, 2147483647, -1 },
                { 2147483647, -1, 2147483647, -1 },
                { 0, -1, 2147483647, 2147483647 }
        };
        solution.wallsAndGates(rooms);

        // Print the result
        for (int[] row : rooms) {
            for (int cell : row) {
                System.out.print(cell + " ");
            }
            System.out.println();
        }
    }
}
