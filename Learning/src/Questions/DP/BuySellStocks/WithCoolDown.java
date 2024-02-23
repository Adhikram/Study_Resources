package Questions.DP.BuySellStocks;

import java.util.Arrays;

public class WithCoolDown {

    // Recursive function to calculate the maximum profit
    static int getAns(int[] Arr, int ind, int buy, int n, int[][] dp) {
        // Base case
        if (ind >= n) {
            return 0;
        }

        // If the result is already calculated, return it
        if (dp[ind][buy] != -1) {
            return dp[ind][buy];
        }

        int profit = 0;

        if (buy == 0) { // We can buy the stock
            profit = Math.max(0 + getAns(Arr, ind + 1, 0, n, dp),
                    -Arr[ind] + getAns(Arr, ind + 1, 1, n, dp));
        }

        if (buy == 1) { // We can sell the stock
            profit = Math.max(0 + getAns(Arr, ind + 1, 1, n, dp),
                    Arr[ind] + getAns(Arr, ind + 2, 0, n, dp));
        }

        // Store the result in dp and return it
        dp[ind][buy] = profit;
        return profit;
    }

    static int stockProfitRecursive(int[] Arr) {
        int n = Arr.length;
        int[][] dp = new int[n][2];

        // Initialize dp array with -1 to mark states as not calculated yet
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }

        int ans = getAns(Arr, 0, 0, n, dp);
        return ans;
    }
    // Time Complexity: O(N*2)

    // Reason: There are N*2 states therefore at max ‘N*2’ new problems will be
    // solved and we are running a for loop for ‘N’ times to calculate the total sum

    // Space Complexity: O(N*2) + O(N)

    // Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*2)).

    // Function to calculate the maximum profit from stock trading
    static int stockProfitTabulation(int[] Arr) {
        int n = Arr.length;
        // Each state is represented by two variables: ind and buy
        // ind: The index - 1 of the stock we are currently processing
        // buy: 0 if we can buy the stock, 1 if we can sell the stock
        // dp[ind + 1][buy] stores the maximum profit we can make at index 'ind' with
        int dp[][] = new int[n + 2][2];

        // Iterate through the array backwards
        for (int ind = n - 1; ind >= 0; ind--) {
            for (int buy = 0; buy <= 1; buy++) {
                int profit = 0;

                if (buy == 0) { // We can buy the stock
                    profit = Math.max(0 + dp[ind + 1][0], -Arr[ind] + dp[ind + 1][1]);
                }

                if (buy == 1) { // We can sell the stock
                    profit = Math.max(0 + dp[ind + 1][1], Arr[ind] + dp[ind + 2][0]);
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

    // Function to calculate the maximum profit from stock trading
    static int stockProfit(int[] Arr) {
        int n = Arr.length;
        int[] cur = new int[2];
        int[] front1 = new int[2];
        int[] front2 = new int[2];

        // Iterate through the array backwards
        for (int ind = n - 1; ind >= 0; ind--) {
            for (int buy = 0; buy <= 1; buy++) {
                int profit = 0;

                if (buy == 0) { // We can buy the stock
                    profit = Math.max(0 + front1[0], -Arr[ind] + front1[1]);
                }

                if (buy == 1) { // We can sell the stock
                    profit = Math.max(0 + front1[1], Arr[ind] + front2[0]);
                }

                cur[buy] = profit;
            }

            // Update front1 and front2 arrays
            System.arraycopy(front1, 0, front2, 0, 2);
            System.arraycopy(cur, 0, front1, 0, 2);
        }

        // The maximum profit is stored in cur[0]
        return cur[0];
    }
    // Time Complexity: O(N*2)

    // Reason: There are two nested loops that account for O(N*2) complexity

    // Space Complexity: O(1)

    // Reason: We are using three external arrays of size ‘2’.

    public static void main(String[] args) {
        int[] Arr = { 1, 2, 3, 0, 2 };
        System.out.println(stockProfitRecursive(Arr)); // 3
        System.out.println(stockProfitTabulation(Arr)); // 3
        System.out.println(stockProfit(Arr)); // 3
    }

}
