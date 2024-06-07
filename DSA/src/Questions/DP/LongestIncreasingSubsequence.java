package Questions.DP;

import java.util.Arrays;

public class LongestIncreasingSubsequence {
    // Problem:- The longest increasing subsequence is described as a subsequence of
    // an array where:

    static int getAns(int[] arr, int n, int ind, int prev_index, int[][] dp) {
        // Base condition
        if (ind == n) {
            return 0;
        }

        if (dp[ind][prev_index + 1] != -1) {
            return dp[ind][prev_index + 1];
        }

        int notTake = getAns(arr, n, ind + 1, prev_index, dp);

        int take = 0;

        if (prev_index == -1 || arr[ind] > arr[prev_index]) {
            take = 1 + getAns(arr, n, ind + 1, ind, dp);
        }

        dp[ind][prev_index + 1] = Math.max(notTake, take);

        return dp[ind][prev_index + 1];
    }

    // Function to find the length of the longest increasing subsequence
    static int lisRecursive(int[] arr, int n) {
        int[][] dp = new int[n][n + 1];

        // Initialize dp array with -1 to mark states as not calculated yet
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }

        return getAns(arr, n, 0, -1, dp);
    }
    // Time Complexity: O(N*N)

    // Reason: There are N*N states therefore at max ‘N*N’ new problems will be
    // solved.

    // Space Complexity: O(N*N) + O(N)

    // Reason: We are using an auxiliary recursion stack space(O(N)) (see the
    // recursive tree, in the worst case we will go till N calls at a time) and a 2D
    // array ( O(N*N+1))

    static int longestIncreasingSubsequenceTabulation(int[] arr, int n) {

        int[][] dp = new int[n + 1][n + 1];

        for (int ind = n - 1; ind >= 0; ind--) {
            for (int prev_index = ind - 1; prev_index >= -1; prev_index--) {

                int notTake = dp[ind + 1][prev_index + 1];

                int take = 0;

                if (prev_index == -1 || arr[ind] > arr[prev_index]) {

                    take = 1 + dp[ind + 1][ind + 1];
                }

                dp[ind][prev_index + 1] = Math.max(notTake, take);

            }
        }

        return dp[0][0];
    }
    // Time Complexity: O(N*N)

    // Reason: There are two nested loops

    // Space Complexity: O(N*N)

    // Reason: We are using an external array of size ‘(N+1)*(N+1)’. Stack Space is
    // eliminated.

    static int longestIncreasingSubsequenceOptimized(int arr[], int n) {

        int[] next = new int[n + 1];
        int[] cur = new int[n + 1];

        for (int ind = n - 1; ind >= 0; ind--) {
            for (int prev_index = ind - 1; prev_index >= -1; prev_index--) {

                int notTake = 0 + next[prev_index + 1];

                int take = 0;

                if (prev_index == -1 || arr[ind] > arr[prev_index]) {

                    take = 1 + next[ind + 1];
                }

                cur[prev_index + 1] = Math.max(notTake, take);
            }
            next = cur.clone();
        }

        return cur[0];
    }

    // Time Complexity: O(N*N)

    // Reason: There are two nested loops.

    // Space Complexity: O(N)

    // Reason: We are only using two rows of size n.

    public static void main(String[] args) {
        int[] arr = { 10, 22, 9, 33, 21, 50, 41, 60, 80 };
        int n = arr.length;
        System.out.println(lisRecursive(arr, n)); // 6
        System.out.println(longestIncreasingSubsequenceTabulation(arr, n)); // 6
        System.out.println(longestIncreasingSubsequenceOptimized(arr, n)); // 6
    }

}
