package Questions.DP.BuySellStocks;

import java.util.Arrays;

public class KTransactions {

    static int getAns(int[] Arr, int n, int ind, int buy, int cap, int[][][] dp) {
        // Base case: If we have processed all stocks or have no capital left, return 0
        // profit
        if (ind == n || cap == 0)
            return 0;

        // If the result for this state is already calculated, return it
        if (dp[ind][buy][cap] != -1)
            return dp[ind][buy][cap];

        int profit = 0;

        if (buy == 0) { // We can buy the stock
            profit = Math.max(0 + getAns(Arr, n, ind + 1, 0, cap, dp),
                    -Arr[ind] + getAns(Arr, n, ind + 1, 1, cap, dp));
        }

        if (buy == 1) { // We can sell the stock
            profit = Math.max(0 + getAns(Arr, n, ind + 1, 1, cap, dp),
                    Arr[ind] + getAns(Arr, n, ind + 1, 0, cap - 1, dp));
        }

        // Store the calculated profit in the dp array and return it
        return dp[ind][buy][cap] = profit;
    }

    static int maxProfitRecursive(int[] prices, int k) {
        int n = prices.length;

        // Creating a 3D dp array of size [n][2][3]

        int[][][] dp = new int[n][2][k + 1];

        // Initialize the dp array with -1
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 2; j++) {
                Arrays.fill(dp[i][j], -1);
            }
        }

        // Calculate and return the maximum profit
        return getAns(prices, n, 0, 0, k, dp);
    }
    // Time Complexity: O(N*K*3)

    // Reason: There are N*K*3 states therefore at max ‘N*2*3’ new problems will be
    // solved.

    // Space Complexity: O(N*K*3) + O(N)

    // Reason: We are using a recursion stack space(O(N)) and a 3D array (
    // O(N*K*3)).

    static int maxProfitTabulation(int[] prices, int k) {
        int n = prices.length;

        // Creating a 3D dp array of size [n+1][2][3] initialized to 0
        int[][][] dp = new int[n + 1][2][k+1];
        // Each Cell dp[i][j][k] talk about the maximum profit that can be made by
        // performing j transactions till ith day with k limits in hand.

        // Loop through the dp array, starting from the second last stock (ind=n-1)
        for (int ind = n - 1; ind >= 0; ind--) {
            for (int buy = 0; buy <= 1; buy++) {
                for (int cap = 1; cap <= k; cap++) {

                    if (buy == 0) { // We can buy the stock
                        dp[ind][buy][cap] = Math.max(0 + dp[ind + 1][0][cap],
                                -prices[ind] + dp[ind + 1][1][cap]);
                    }

                    if (buy == 1) { // We can sell the stock
                        dp[ind][buy][cap] = Math.max(0 + dp[ind + 1][1][cap],
                                prices[ind] + dp[ind + 1][0][cap - 1]);
                    }
                }
            }
        }

        // The maximum profit with 2 transactions is stored in dp[0][0][2]
        return dp[0][0][k];
    }
    // Time Complexity: O(N*k*3)

    // Reason: There are three nested loops that account for O(N*k*3) complexity.

    // Space Complexity: O(N*k*3)

    // Reason: We are using an external array of size ‘N*k*3’. Stack Space is
    // eliminated.

    static int maxProfitOptimized(int[] prices, int k) {
        int n = prices.length;

        // Create a 2D array 'ahead' and 'cur' to store profit values
        int[][] ahead = new int[3][k + 1];
        int[][] cur = new int[3][k + 1 ];

        // Loop through the prices array, starting from the second last stock (ind=n-1)
        for (int ind = n - 1; ind >= 0; ind--) {
            for (int buy = 0; buy <= 1; buy++) {
                for (int cap = 1; cap <= k; cap++) {

                    if (buy == 0) { // We can buy the stock
                        cur[buy][cap] = Math.max(0 + ahead[0][cap],
                                -prices[ind] + ahead[1][cap]);
                    }

                    if (buy == 1) { // We can sell the stock
                        cur[buy][cap] = Math.max(0 + ahead[1][cap],
                                prices[ind] + ahead[0][cap - 1]);
                    }
                }
            }

            // Copy the values of 'cur' to 'ahead'
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j <= k; j++) {
                    ahead[i][j] = cur[i][j];
                }
            }
        }

        // The maximum profit with 2 transactions is stored in ahead[0][2]
        return ahead[0][k];
    }
    // Time Complexity: O(N*k*3)

    // Reason: There are three nested loops that account for O(N*k*3) complexity

    // Space Complexity: O(1)

    // Reason: We are using two external arrays of size ‘k*3’.

    public static void main(String[] args) {
        int[] prices = {3, 3, 5, 0, 0, 3, 1, 4};
        int k = 5;
        System.out.println(maxProfitRecursive(prices, k));
        System.out.println(maxProfitTabulation(prices, k));
        System.out.println(maxProfitOptimized(prices, k));
    }
}
