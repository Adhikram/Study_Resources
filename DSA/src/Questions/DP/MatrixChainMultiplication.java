package Questions.DP;

import java.util.Arrays;

public class MatrixChainMultiplication {
    static int f(int[] arr, int i, int j, int[][] dp) {

        // When there is only one matrix in the chain i.e. i==j then the cost is 0
        if (i == j)
            return 0;
        if (dp[i][j] != -1)
            return dp[i][j];

        int mini = Integer.MAX_VALUE;

        // k is the index of the matrix after which the chain is split into two parts
        for (int k = i; k <= j - 1; k++) {

            int ans = f(arr, i, k, dp) + f(arr, k + 1, j, dp) + arr[i - 1] * arr[k] * arr[j];

            mini = Math.min(mini, ans);

        }

        dp[i][j] = mini;
        return mini;
    }

    static int matrixMultiplicationRecursive(int[] arr, int N) {

        int i = 1;
        int j = N - 1;
        int[][] dp = new int[N][N];

        for (int[] row : dp)
            Arrays.fill(row, -1);
        return f(arr, i, j, dp);

    }

    // Time Complexity: O(N*N*N)

    // Reason: There are N*N states and we explicitly run a loop inside the function
    // which will run for N times, therefore at max ‘N*N*N’ new problems will be
    // solved.

    // Space Complexity: O(N*N) + O(N)

    // Reason: We are using an auxiliary recursion stack space(O(N))and a 2D array (
    // O(N*N)).

    static int matrixMultiplicationTabulation(int[] arr, int N) {
        // Each cell dp[i][j] stores the minimum cost of multiplying the matrices from
        // i to j
        int[][] dp = new int[N][N];

        // When there is only one matrix in the chain i.e. i==j then the cost is 0
        for (int i = 1; i < N; i++)
            dp[i][i] = 0;

        // l is the chain length
        for (int l = 2; l < N; l++) {
            // i is the starting index of the chain
            for (int i = 1; i < N - l + 1; i++) {
                // j is the ending index of the chain
                int j = i + l - 1;
                dp[i][j] = Integer.MAX_VALUE;
                for (int k = i; k <= j - 1; k++) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]);
                }
            }
        }
        return dp[1][N - 1];
    }
    // Time Complexity: O(N*N*N)
    // Reason: There are N*N states and we explicitly run a loop inside the function
    // which will run for N times, therefore at max ‘N*N*N’ new problems will be
    // Space Complexity: O(N*N)
    // Reason: We are using a 2D array (O(N*N)).

    public static void main(String[] args) {
        int arr[] = { 40, 20, 30, 10, 30 };
        System.out.println(matrixMultiplicationRecursive(arr, arr.length)); // 26000
        System.out.println(matrixMultiplicationTabulation(arr, arr.length)); // 26000
    }

}
