package Questions.Matrix;

import java.util.LinkedList;
import java.util.Queue;

/*
https://leetcode.com/problems/the-maze/description/
 There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).

 

Example 1:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
Example 2:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
Example 3:

Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: false
 

Constraints:

m == maze.length
n == maze[i].length
1 <= m, n <= 100
maze[i][j] is 0 or 1.
start.length == 2
destination.length == 2
0 <= startrow, destinationrow <= m
0 <= startcol, destinationcol <= n
Both the ball and the destination exist in an empty space, and they will not be in the same position initially.
The maze contains at least 2 empty spaces.
Time Complexity: O(m * n)
Space Complexity: O(m * n)
 */
public class TheMaze {
    private static final int[][] DIRECTIONS = {
            { 0, 1 }, // right
            { 0, -1 }, // left
            { 1, 0 }, // down
            { -1, 0 } // up
    };

    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        int m = maze.length, n = maze[0].length;
        boolean[][] visited = new boolean[m][n];
        Queue<int[]> queue = new LinkedList<>();
        queue.add(start);
        visited[start[0]][start[1]] = true;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            if (curr[0] == destination[0] && curr[1] == destination[1]) {
                return true;
            }

            for (int[] dir : DIRECTIONS) {
                int x = curr[0], y = curr[1];

                // Move in the direction until hitting a wall
                while (x >= 0 && x < m && y >= 0 && y < n && maze[x][y] == 0) {
                    x += dir[0];
                    y += dir[1];
                }

                // Step back to the last valid position
                x -= dir[0];
                y -= dir[1];

                // If not visited, mark as visited and add to queue
                if (!visited[x][y]) {
                    visited[x][y] = true;
                    queue.add(new int[] { x, y });
                }
            }
        }

        return false; // No path found
    }
    public static void main(String[] args) {
        TheMaze obj = new TheMaze();
        int[][] maze1 = {
                { 0, 0, 1, 0, 0 },
                { 0, 0, 0, 0, 0 },
                { 0, 0, 0, 1, 0 },
                { 1, 1, 0, 1, 1 },
                { 0, 0, 0, 0, 0 }
        };
        int[] start1 = { 0, 4 };
        int[] destination1 = { 4, 4 };
        System.out.println(obj.hasPath(maze1, start1, destination1)); // Output: true

        int[][] maze2 = {
                { 0, 0, 1, 0, 0 },
                { 0, 0, 0, 0, 0 },
                { 0, 0, 0, 1, 0 },
                { 1, 1, 0, 1, 1 },
                { 0, 0, 0, 0, 0 }
        };
        int[] start2 = { 0, 4 };
        int[] destination2 = { 3, 2 };
        System.out.println(obj.hasPath(maze2, start2, destination2)); // Output: false

        int[][] maze3 = {
                { 0, 0, 0, 0, 0 },
                { 1, 1, 0, 0, 1 },
                { 0, 0, 0, 0, 0 },
                { 0, 1, 0, 0, 1 },
                { 0, 1, 0, 0, 0 }
        };
        int[] start3 = { 4, 3 };
        int[] destination3 = { 0, 1 };
        System.out.println(obj.hasPath(maze3, start3, destination3)); // Output: false
    }
}
