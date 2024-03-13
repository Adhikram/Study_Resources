package Questions.DP;

import java.util.Arrays;

public class CoinChange {
    // Problem:- We are given an array Arr with N distinct coins and a target. We
    // have an infinite supply of each coin denomination. We need to find the number
    // of ways we sum up the coin values to give us the target.

    // Recursive function to count the ways to make change
    static long countWaysToMakeChangeUtil(int[] arr, int ind, int T, long[][] dp) {
        // Base case: If the current index is 0
        if (ind == 0) {
            // If T is divisible by the first element of the array, return 1, else return 0
            if (T % arr[0] == 0)
                return 1;
            else
                return 0;
        }

        // If the result for this subproblem has already been calculated, return it
        if (dp[ind][T] != -1)
            return dp[ind][T];

        // Calculate the number of ways without taking the current element
        long notTaken = countWaysToMakeChangeUtil(arr, ind - 1, T, dp);

        // Initialize the number of ways taking the current element as 0
        long taken = 0;

        // If the current element is less than or equal to T, calculate 'taken'
        if (arr[ind] <= T)
            taken = countWaysToMakeChangeUtil(arr, ind, T - arr[ind], dp);

        // Store the result in the dp array and return it
        return dp[ind][T] = notTaken + taken;
    }

    // Function to count the ways to make change
    static long countWaysToMakeChangeRecursive(int[] arr, int n, int T) {
        // Create a 2D array to store results of subproblems
        long dp[][] = new long[n][T + 1];

        // Initialize the dp array with -1 to indicate that subproblems are not solved
        // yet
        for (long row[] : dp)
            Arrays.fill(row, -1);

        // Call the countWaysToMakeChangeUtil function to calculate the number of ways
        return countWaysToMakeChangeUtil(arr, n - 1, T, dp);
    }
    // Time Complexity: O(N*T)

    // Reason: There are N*W states therefore at max ‘N*T’ new problems will be
    // solved.

    // Space Complexity: O(N*T) + O(N)

    // Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*T)).

    // Function to count the ways to make change
    static long countWaysToMakeChangeTabulation(int[] arr, int n, int T) {
        // Each cell dp[i][j] stores the number of ways to make change for the target
        // 'j' using the first 'i' coins
        long dp[][] = new long[n][T + 1];

        // Initialize the first column of the dp array
        // If the target is divisible by the first element of the array, set the value
        // to
        // 1, else set it to 0
        for (int i = 0; i <= T; i++) {
            if (i % arr[0] == 0)
                dp[0][i] = 1;
            // Else condition is automatically fulfilled, as dp array is initialized to zero
        }

        // Fill the dp array using dynamic programming
        for (int ind = 1; ind < n; ind++) {
            for (int target = 0; target <= T; target++) {
                long notTaken = dp[ind - 1][target];

                long taken = 0;
                if (arr[ind] <= target)
                    taken = dp[ind][target - arr[ind]];

                dp[ind][target] = notTaken + taken;
            }
        }

        return dp[n - 1][T];
    }
    // Time Complexity: O(N*T)

    // Reason: There are two nested loops

    // Space Complexity: O(N*T)

    // Reason: We are using an external array of size ‘N*T’. Stack Space is
    // eliminated.

    // Function to count the ways to make change
    static long countWaysToMakeChangeOptimized(int[] arr, int n, int T) {
        // Create an array to store results of subproblems for the previous element
        long[] prev = new long[T + 1];

        // Initialize base condition for the first element of the array
        for (int i = 0; i <= T; i++) {
            if (i % arr[0] == 0)
                prev[i] = 1;
            // Else condition is automatically fulfilled, as prev array is initialized to
            // zero
        }

        // Fill the prev array using dynamic programming
        for (int ind = 1; ind < n; ind++) {
            // Create an array to store results of subproblems for the current element
            long[] cur = new long[T + 1];
            for (int target = 0; target <= T; target++) {
                long notTaken = prev[target];

                long taken = 0;
                if (arr[ind] <= target)
                    taken = cur[target - arr[ind]];

                cur[target] = notTaken + taken;
            }
            prev = cur;
        }

        return prev[T];
    }
    // Time Complexity: O(N*T)

    // Reason: There are two nested loops.

    // Space Complexity: O(T)

    // Reason: We are using an external array of size ‘T+1’ to store two rows only.
    public static void main(String[] args) {
        int arr[] = { 1, 2, 3 };
        int N = arr.length;
        int T = 4;

        System.out.println(countWaysToMakeChangeRecursive(arr, N, T));
        System.out.println(countWaysToMakeChangeTabulation(arr, N, T));
        System.out.println(countWaysToMakeChangeOptimized(arr, N, T));
    }

}
