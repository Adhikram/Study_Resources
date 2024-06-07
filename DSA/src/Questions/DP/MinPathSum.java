package Questions.DP;

import java.util.Arrays;

public class MinPathSum {
    static int minSumPathUtilRecursive(int i, int j, int[][] matrix, int[][] dp) {
        // Base cases
        if (i == 0 && j == 0)
            return matrix[0][0]; // If we're at the top-left cell, return its value
        if (i < 0 || j < 0)
            return (int) Math.pow(10, 9); // If we're out of bounds, return a large value
        if (dp[i][j] != -1)
            return dp[i][j]; // If we've already calculated this cell, return the stored result

        // Calculate the sum of the current cell plus the minimum sum path from above
        // and from the left
        int up = matrix[i][j] + minSumPathUtilRecursive(i - 1, j, matrix, dp);
        int left = matrix[i][j] + minSumPathUtilRecursive(i, j - 1, matrix, dp);

        // Store the minimum of the two possible paths
        return dp[i][j] = Math.min(up, left);
    }

    // Main function to calculate the minimum sum path in the matrix
    static int minSumPathRecursive(int n, int m, int[][] matrix) {
        int[][] dp = new int[n][m];

        // Initialize the DP matrix with -1
        for (int row[] : dp)
            Arrays.fill(row, -1);

        // Call the helper function starting from the bottom-right cell
        return minSumPathUtilRecursive(n - 1, m - 1, matrix, dp);
    }
    // Time Complexity: O(N*M)

    // Reason: At max, there will be N*M calls of recursion.

    // Space Complexity: O((M-1)+(N-1)) + O(N*M)

    // Reason: We are using a recursion stack space: O((M-1)+(N-1)), here
    // (M-1)+(N-1) is the path length and an external DP Array of size ‘N*M’.

    static int minSumPathDP(int n, int m, int[][] matrix) {
        int dp[][] = new int[n][m];

        // Iterate through the matrix
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i == 0 && j == 0)
                    dp[i][j] = matrix[i][j]; // If we're at the top-left cell, the minimum sum is its value
                else {
                    int up = matrix[i][j];
                    if (i > 0)
                        up += dp[i - 1][j]; // Add the value from above if it's not out of bounds
                    else
                        up += (int) Math.pow(10, 9); // Add a large value if out of bounds in the up direction

                    int left = matrix[i][j];
                    if (j > 0)
                        left += dp[i][j - 1]; // Add the value from the left if it's not out of bounds
                    else
                        left += (int) Math.pow(10, 9); // Add a large value if out of bounds in the left direction

                    // Store the minimum of the two possible paths
                    dp[i][j] = Math.min(up, left);
                }
            }
        }

        // The final result is stored in the bottom-right cell of the DP matrix
        return dp[n - 1][m - 1];
    }

    // Time Complexity: O(N*M)

    // Reason: There are two nested loops

    // Space Complexity: O(N*M)

    // Reason: We are using an external array of size ‘N*M’’.

    static int minSumPathOptimizedDP(int n, int m, int[][] matrix) {
        // Initialize an array to store the previous row values
        int prev[] = new int[m];

        for (int i = 0; i < n; i++) {
            // Create a temporary array to store the current row values
            int temp[] = new int[m];

            for (int j = 0; j < m; j++) {
                if (i == 0 && j == 0)
                    temp[j] = matrix[i][j]; // If we're at the top-left cell, the minimum sum is its value
                else {
                    int up = matrix[i][j];
                    if (i > 0)
                        up += prev[j]; // Add the value from above if it's not out of bounds
                    else
                        up += (int) Math.pow(10, 9); // Add a large value if out of bounds in the up direction

                    int left = matrix[i][j];
                    if (j > 0)
                        left += temp[j - 1]; // Add the value from the left if it's not out of bounds
                    else
                        left += (int) Math.pow(10, 9); // Add a large value if out of bounds in the left direction

                    // Store the minimum of the two possible paths in the current cell
                    temp[j] = Math.min(up, left);
                }
            }
            // Update the previous row with the values of the current row
            prev = temp;
        }

        // The final result is stored in the last element of the previous row
        return prev[m - 1];
    }
    // Time Complexity: O(M*N)

    // Reason: There are two nested loops

    // Space Complexity: O(N)

    // Reason: We are using an external array of size ‘N’ to store only one row.

    public static void main(String[] args) {
        int[][] matrix = { { 1, 3, 1 }, { 1, 5, 1 }, { 4, 2, 1 } };
        System.out.println(minSumPathRecursive(3, 3, matrix));
        System.out.println(minSumPathOptimizedDP(3, 3, matrix));
        System.out.println(minSumPathDP(3, 3, matrix));
    }
}
