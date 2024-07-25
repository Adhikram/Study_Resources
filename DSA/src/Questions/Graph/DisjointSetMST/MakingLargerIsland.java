package Questions.Graph.DisjointSetMST;

import java.util.HashSet;

// Problem Description: Given a 2D grid of 0s and 1s, we may change at most one 0 to a 1.
// After, what is the size of the largest island? An island is a 4-directionally connected group of 1s.

// Intuition: We can solve this problem using Disjoint Set Data Structure. We can follow the below steps to solve this problem:
// 1. Union all the adjacent 1s in the grid.
// 2. For each 0 in the grid, find the size of the largest groups of connected 1s .
// 3. Find the Max size and update the answer if needed.

public class MakingLargerIsland {
    private static boolean isValid(int newr, int newc, int n) {
        return newr >= 0 && newr < n && newc >= 0 && newc < n;
    }

    private static Integer getNodeNo(int row, int col, int n) {
        return row * n + col;
    }

    public static int MaxConnection(int[][] grid) {
        int n = grid.length;
        int[] dr = { -1, 0, 1, 0 };
        int[] dc = { 0, -1, 0, 1 };
        DisjointSet ds = new DisjointSet(n * n);
        // Step 1: Union adjacent 1s in the grid
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n; col++) {
                if (grid[row][col] == 0)
                    continue;
                for (int ind = 0; ind < 4; ind++) {
                    int newr = row + dr[ind];
                    int newc = col + dc[ind];
                    if (isValid(newr, newc, n) && grid[newr][newc] == 1) {
                        int nodeNo = getNodeNo(row, col, n);
                        int adjNodeNo = getNodeNo(newr, newc, n);
                        ds.unionBySize(nodeNo, adjNodeNo);
                    }
                }
            }
        }
        // Step 2: Find the size of the largest group of connected 1s
        int mx = 0;
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n; col++) {
                if (grid[row][col] == 1)
                    continue;

                HashSet<Integer> components = new HashSet<>();
                for (int ind = 0; ind < 4; ind++) {
                    int newr = row + dr[ind];
                    int newc = col + dc[ind];
                    if (isValid(newr, newc, n)) {
                        if (grid[newr][newc] == 1) {
                            components.add(ds.findUPar(getNodeNo(newr, newc, n)));
                        }
                    }
                }
                int sizeTotal = 0;
                for (Integer parents : components) {
                    sizeTotal += ds.size.get(parents);
                }
                mx = Math.max(mx, sizeTotal + 1);
            }
        }
        // Step 3: Check the size of all disjoint sets and update mx if needed
        for (int cellNo = 0; cellNo < n * n; cellNo++) {
            mx = Math.max(mx, ds.size.get(ds.findUPar(cellNo)));
        }
        return mx;
    }

    // Time Complexity: O(N2)+O(N2) ~ O(N2) where N = total number of rows of the
    // grid. Inside those nested loops, all the operations are taking apparently
    // constant time. So, O(N2) for the nested loop only, is the time complexity.

    // Space Complexity: O(N2) where N = total number of rows of the grid. We are
    public static void main(String[] args) {
        int[][] grid = {
                { 1, 1, 0, 1, 1, 0 }, { 1, 1, 0, 1, 1, 0 },
                { 1, 1, 0, 1, 1, 0 }, { 0, 0, 1, 0, 0, 0 },
                { 0, 0, 1, 1, 1, 0 }, { 0, 0, 1, 1, 1, 0 }
        };

        int ans = MaxConnection(grid);
        System.out.println("The largest group of connected 1s is of size: " + ans);
    }
}
