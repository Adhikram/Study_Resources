package Questions.DP.BuySellStocks;

import java.util.Arrays;

public class MultipleBuySell {

    static long getMaximumProfitUtil(long[] Arr, int ind, int buy, int n, long[][] dp) {
        // Base case
        if (ind == n)
            return 0;

        // If the result is already computed, return it
        if (dp[ind][buy] != -1)
            return dp[ind][buy];

        long profit = 0;

        if (buy == 0) { // We can buy the stock
            profit = Math.max(0 + getMaximumProfitUtil(Arr, ind + 1, 0, n, dp),
                    -Arr[ind] + getMaximumProfitUtil(Arr, ind + 1, 1, n, dp));
        }

        if (buy == 1) { // We can sell the stock
            profit = Math.max(0 + getMaximumProfitUtil(Arr, ind + 1, 1, n, dp),
                    Arr[ind] + getMaximumProfitUtil(Arr, ind + 1, 0, n, dp));
        }

        // Store the result in the dp table and return it
        dp[ind][buy] = profit;
        return profit;
    }

    // Function to calculate the maximum profit
    static long getMaximumProfitRecursive(long[] Arr, int n) {
        // Create a 2D vector for memoization (dp)
        long[][] dp = new long[n][n];
        for (long[] row : dp)
            Arrays.fill(row, -1L);

        // Base case: If n is 0, return 0 profit
        if (n == 0)
            return 0;

        // Calculate the maximum profit using the recursive function
        long ans = getMaximumProfitUtil(Arr, 0, 0, n, dp);
        return ans;
    }
    // Time Complexity: O(N*2)

    // Reason: There are N*2 states therefore at max ‘N*2’ new problems will be
    // solved and we are running a for loop for ‘N’ times to calculate the total sum

    // Space Complexity: O(N*2) + O(N)

    // Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*2)).

    // Function to calculate the maximum profit
    static long getMaximumProfitTabulation(long[] Arr, int n) {
        // Create a 2D array for dynamic programming with dimensions [n+1][2]
        long[][] dp = new long[n + 1][2];

        // Initialize the entire dp table with -1
        for (long[] row : dp) {
            Arrays.fill(row, -1);
        }

        // Base condition: If we have no stocks to buy or sell, profit is 0
        dp[n][0] = dp[n][1] = 0;

        long profit = 0;

        // Iterate through the array in reverse to calculate the maximum profit
        for (int ind = n - 1; ind >= 0; ind--) {
            for (int buy = 0; buy <= 1; buy++) {
                if (buy == 0) { // We can buy the stock
                    profit = Math.max(0 + dp[ind + 1][0], -Arr[ind] + dp[ind + 1][1]);
                }

                if (buy == 1) { // We can sell the stock
                    profit = Math.max(0 + dp[ind + 1][1], Arr[ind] + dp[ind + 1][0]);
                }

                dp[ind][buy] = profit;
            }
        }
        return dp[0][0]; // The maximum profit is stored at dp[0][0]
    }
    // Time Complexity: O(N*2)

    // Reason: There are two nested loops that account for O(N*2) complexity.

    // Space Complexity: O(N*2)

    // Reason: We are using an external array of size ‘N*2’. Stack Space is
    // eliminated.

    // Function to calculate the maximum profit
    static long getMaximumProfitOptimized(long[] Arr, int n) {
        // Create arrays 'ahead' and 'cur' to store the maximum profit ahead and current
        // profit
        long[] ahead = new long[2];

        // Base condition: If we have no stocks to buy or sell, profit is 0
        ahead[0] = ahead[1] = 0;

        long profit = 0;

        // Iterate through the array in reverse to calculate the maximum profit
        for (int ind = n - 1; ind >= 0; ind--) {
            long[] cur = new long[2];
            for (int buy = 0; buy <= 1; buy++) {
                if (buy == 0) { // We can buy the stock
                    profit = Math.max(0 + ahead[0], -Arr[ind] + ahead[1]);
                }

                if (buy == 1) { // We can sell the stock
                    profit = Math.max(0 + ahead[1], Arr[ind] + ahead[0]);
                }
                cur[buy] = profit;
            }

            // Update the 'ahead' array with the current profit values
            ahead = cur;
        }
        return ahead[0]; // The maximum profit is stored in 'cur[0]'
    }
    // Time Complexity: O(N*2)

    // Reason: There are two nested loops that account for O(N*2) complexity

    // Space Complexity: O(1)

    // Reason: We are using an external array of size ‘2’.

    public static void main(String[] args) {
        long[] Arr = { 7, 1, 5, 3, 6, 4 };
        System.out.println(getMaximumProfitRecursive(Arr, Arr.length));
        System.out.println(getMaximumProfitTabulation(Arr, Arr.length));
        System.out.println(getMaximumProfitOptimized(Arr, Arr.length));
    }

}
