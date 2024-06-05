package Questions.DP;

import java.util.Arrays;

// We are given an ‘N*M’ matrix. We need to find the maximum path sum from any
// cell of the first row to any cell of the last row.

// At every cell we can move in three directions: to the bottom cell (↓), to the
// bottom-right cell(↘), or to the bottom-left cell(↙).

// Function to find the maximum path sum in the matrix using dynamic programming
public class MinimumMaximumFallingPath {

    static int solveUtil(int i, int j, int m, int[][] matrix, int[][] dp) {
        // Base Conditions
        if (j < 0 || j >= m)
            return (int) Math.pow(-10, 9);
        if (i == 0)
            return matrix[0][j];

        if (dp[i][j] != -1)
            return dp[i][j];

        // Calculate three possible paths: moving up, left diagonal, and right diagonal
        int up = matrix[i][j] + solveUtil(i - 1, j, m, matrix, dp);
        int leftDiagonal = matrix[i][j] + solveUtil(i - 1, j - 1, m, matrix, dp);
        int rightDiagonal = matrix[i][j] + solveUtil(i - 1, j + 1, m, matrix, dp);

        // Store the maximum of the three paths in dp
        return dp[i][j] = Math.max(up, Math.max(leftDiagonal, rightDiagonal));
    }

    // Function to find the maximum path sum in the matrix
    static int getMaxPathSumMemorization(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;

        int[][] dp = new int[n][m];
        // Arrays.stream(dp).forEach(row -> Arrays.fill(row, -1));
        for (int[] row : dp)
            Arrays.fill(row, -1);

        int maxi = Integer.MIN_VALUE;

        // For each starting column, find the maximum path sum and update maxi
        for (int j = 0; j < m; j++) {
            int ans = solveUtil(n - 1, j, m, matrix, dp);
            maxi = Math.max(maxi, ans);
        }

        return maxi;
    }

    // Function to find the maximum path sum in the matrix using dynamic programming
    static int getMaxPathSumTabulation(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;

        int[][] dp = new int[n][m];

        // Initializing the first row - base condition
        for (int j = 0; j < m; j++) {
            dp[0][j] = matrix[0][j];
        }

        // Calculate the maximum path sum for each cell in the matrix
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int up = matrix[i][j] + dp[i - 1][j];

                int leftDiagonal = matrix[i][j];
                if (j - 1 >= 0) {
                    leftDiagonal += dp[i - 1][j - 1];
                } else {
                    leftDiagonal += (int) Math.pow(-10, 9);
                }

                int rightDiagonal = matrix[i][j];
                if (j + 1 < m) {
                    rightDiagonal += dp[i - 1][j + 1];
                } else {
                    rightDiagonal += (int) Math.pow(-10, 9);
                }

                // Store the maximum of the three paths in dp
                dp[i][j] = Math.max(up, Math.max(leftDiagonal, rightDiagonal));
            }
        }

        // Find the maximum value in the last row of dp
        int maxi = Integer.MIN_VALUE;
        for (int j = 0; j < m; j++) {
            maxi = Math.max(maxi, dp[n - 1][j]);
        }

        return maxi;
    }

    // Function to find the maximum path sum in the matrix using dynamic programming
    static int getMaxPathSumOptimized(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;

        int[] prev = new int[m];
        // int [] cur = new int[m];

        // Initializing the first row - base condition
        for (int j = 0; j < m; j++) {
            prev[j] = matrix[0][j];
        }

        for (int i = 1; i < n; i++) {
            int[] cur = new int[m];
            for (int j = 0; j < m; j++) {
                int up = matrix[i][j] + prev[j];

                int leftDiagonal = matrix[i][j];
                if (j - 1 >= 0) {
                    leftDiagonal += prev[j - 1];
                } else {
                    leftDiagonal += -1e9;
                }

                int rightDiagonal = matrix[i][j];
                if (j + 1 < m) {
                    rightDiagonal += prev[j + 1];
                } else {
                    rightDiagonal += -1e9;
                }

                // Store the maximum of the three paths in cur
                cur[j] = Math.max(up, Math.max(leftDiagonal, rightDiagonal));
            }

            // Update the prev list with the values from the cur list for the next row
            prev = cur;
            // prev = Arrays.copyOf(cur, m); // Create a copy of cur for prev If we keep cur
            // globally then we should use this
        }

        int maxi = Integer.MIN_VALUE;

        for (int j = 0; j < m; j++) {
            maxi = Math.max(maxi, prev[j]);
        }

        return maxi;
    }

    public static void main(String[] args) {
        int matrix[][] = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };

        System.out.println(getMaxPathSumMemorization(matrix));
        System.out.println(getMaxPathSumTabulation(matrix));
        System.out.println(getMaxPathSumOptimized(matrix));
    }

}
