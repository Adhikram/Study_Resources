package Questions.Graph.DisjointSetMST;

import java.util.ArrayList;
import java.util.List;

// Intuition: We can use DisjointSet to keep track of connected components. We can use a 2D array to mark visited cells.
// We can iterate through each operation and check if the cell is already visited. If it is, we add the current island count to the result list.
// Otherwise, we mark the cell as visited and increment the island count. We then check the adjacent cells and merge the islands if they belong to different islands.
// We add the current island count to the result list and continue to the next operation. Finally, we return the list containing island counts after each operation.    
// Time Complexity: O(Q*4α) ~ O(Q) where Q = no. of queries. The term 4α is so small that it can be considered constant.

// Space Complexity:O(Q)+O(N*M)+O(N*M),where Q=no.of queries,N=total no.of rows,M=total no.of columns.
// The last two terms are for the parent and the size array used inside the Disjoint set data structure.The first term is to store the answer.

public class NumberOfIsland2 {
    // Method to check if a given cell is within the bounds of the grid
    private static boolean isValid(int adjr, int adjc, int n, int m) {
        return adjr >= 0 && adjr < n && adjc >= 0 && adjc < m;
    }

    // Method to count the number of islands after performing given operations
    public static List<Integer> numOfIslands(int n, int m, int[][] operators) {
        // Initialize DisjointSet to track connected components
        DisjointSet ds = new DisjointSet(n * m);

        // Array to mark visited cells
        int[][] vis = new int[n][m];

        // Define directions: up, right, down, left
        int[] dr = { -1, 0, 1, 0 };
        int[] dc = { 0, 1, 0, -1 };

        // Initialize island count and result list
        int cnt = 0;
        List<Integer> ans = new ArrayList<>();

        // Process each operation
        for (int[] operator : operators) {
            int row = operator[0];
            int col = operator[1];

            // If cell is already visited, add current island count to result list and
            // continue
            if (vis[row][col] == 1) {
                ans.add(cnt);
                continue;
            }

            // Mark cell as visited
            vis[row][col] = 1;
            cnt++; // Increment island count

            // Check adjacent cells
            for (int ind = 0; ind < 4; ind++) {
                int adjr = row + dr[ind];
                int adjc = col + dc[ind];

                // If adjacent cell is within bounds and visited
                if (isValid(adjr, adjc, n, m) && vis[adjr][adjc] == 1) {
                    int nodeNo = row * m + col;
                    int adjNodeNo = adjr * m + adjc;

                    // If the current cell and adjacent cell belong to different islands
                    if (ds.findUPar(nodeNo) != ds.findUPar(adjNodeNo)) {
                        cnt--; // Decrement island count
                        ds.unionBySize(nodeNo, adjNodeNo); // Merge islands
                    }
                }
            }

            ans.add(cnt); // Add current island count to result list
        }

        return ans; // Return the list containing island counts after each operation
    }

    public static void main(String[] args) {
        int n = 4, m = 5;
        int[][] operators = {
                { 0, 0 }, { 0, 0 }, { 1, 1 }, { 1, 0 }, { 0, 1 },
                { 0, 3 }, { 1, 3 }, { 0, 4 }, { 3, 2 }, { 2, 2 }, { 1, 2 }, { 0, 2 }
        };

        List<Integer> ans = numOfIslands(n, m, operators);

        // Print the island counts after each operation
        for (int islandCount : ans) {
            System.out.print(islandCount + " ");
        }
        System.out.println();
        // Output: 1 1 2 1 1 2 2 2 3 3 1 1
    }
}
