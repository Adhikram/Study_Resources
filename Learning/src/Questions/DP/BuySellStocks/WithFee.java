package Questions.DP.BuySellStocks;

import java.util.Arrays;

public class WithFee {

    // Function to calculate the maximum profit
    static int getAns(int[] Arr, int ind, int buy, int n, int fee, int[][] dp) {
        // Base case
        if (ind == n) {
            return 0;
        }

        // If the result is already calculated, return it
        if (dp[ind][buy] != -1) {
            return dp[ind][buy];
        }

        int profit = 0;

        if (buy == 0) { // We can buy the stock
            profit = Math.max(0 + getAns(Arr, ind + 1, 0, n, fee, dp), -Arr[ind] + getAns(Arr, ind + 1, 1, n, fee, dp));
        }

        if (buy == 1) { // We can sell the stock
            profit = Math.max(0 + getAns(Arr, ind + 1, 1, n, fee, dp),
                    Arr[ind] - fee + getAns(Arr, ind + 1, 0, n, fee, dp));
        }

        // Store the result in dp and return it
        dp[ind][buy] = profit;
        return profit;
    }

    // Function to calculate the maximum profit with a transaction fee
    static int maximumProfitRecursive(int n, int fee, int[] Arr) {
        int dp[][] = new int[n][2];

        // Initialize dp array with -1 to mark states as not calculated yet
        for (int row[] : dp) {
            Arrays.fill(row, -1);
        }

        if (n == 0) {
            return 0;
        }

        int ans = getAns(Arr, 0, 0, n, fee, dp);
        return ans;
    }
    // Time Complexity: O(N*2)

    // Reason: There are N*2 states therefore at max ‘N*2’ new problems will be
    // solved and we are running a for loop for ‘N’ times to calculate the total sum

    // Space Complexity: O(N*2) + O(N)

    // Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*2)).

    // Function to calculate the maximum profit
    static int maximumProfitTabulation(int n, int fee, int[] Arr) {
        // Handle the base case when n is 0
        if (n == 0) {
            return 0;
        }

        // Each state is represented by two variables: ind and buy
        // ind represents the index of the stock
        // buy: 0 if we can buy the stock, 1 if we can sell the stock
        // dp[ind][buy] stores the maximum profit we can make at index 'ind' with
        int dp[][] = new int[n + 1][2];

        // Iterate through the array backwards
        for (int ind = n - 1; ind >= 0; ind--) {
            for (int buy = 0; buy <= 1; buy++) {
                int profit = 0;

                if (buy == 0) { // We can buy the stock
                    profit = Math.max(0 + dp[ind + 1][0], -Arr[ind] + dp[ind + 1][1]);
                }

                if (buy == 1) { // We can sell the stock
                    profit = Math.max(0 + dp[ind + 1][1], Arr[ind] - fee + dp[ind + 1][0]);
                }

                dp[ind][buy] = profit;
            }
        }

        // The maximum profit is stored in dp[0][0]
        return dp[0][0];
    }
    // Time Complexity: O(N*2)

    // Reason: There are two nested loops that account for O(N*2) complexity.

    // Space Complexity: O(N*2)

    // Reason: We are using an external array of size ‘N*2’. Stack Space is
    // eliminated.

    // Function to calculate the maximum profit
    static long maximumProfitOptimized(int n, int fee, int[] Arr) {
        // Handle the base case when n is 0
        if (n == 0) {
            return 0;
        }

        long ahead[] = new long[2];

        // Initialize base conditions
        ahead[0] = ahead[1] = 0;
        long profit = 0;

        for (int ind = n - 1; ind >= 0; ind--) {
            long cur[] = new long[2];
            for (int buy = 0; buy <= 1; buy++) {
                if (buy == 0) { // We can buy the stock
                    profit = Math.max(0 + ahead[0], -Arr[ind] + ahead[1]);
                }

                if (buy == 1) { // We can sell the stock
                    profit = Math.max(0 + ahead[1], Arr[ind] - fee + ahead[0]);
                }
                cur[buy] = profit;
            }

            ahead = cur;
        }
        return ahead[0];
    }
    // Time Complexity: O(N*2)

    // Reason: There are two nested loops that account for O(N*2) complexity

    // Space Complexity: O(1)

    // Reason: We are using an external array of size ‘2’.

    public static void main(String[] args) {
        int n = 6;
        int fee = 2;
        int Arr[] = { 1, 3, 2, 8, 4, 9 };

        System.out.println(maximumProfitRecursive(n, fee, Arr));
        System.out.println(maximumProfitTabulation(n, fee, Arr));
        System.out.println(maximumProfitOptimized(n, fee, Arr));
    }

}
