package Questions.DP;

import java.sql.Time;
import java.util.Arrays;

/*
https://leetcode.com/problems/target-sum/description/
 You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
 */
public class TargetSum {
    // Function to count partitions using dynamic programming
    static int countPartitionsUtil(int ind, int target, int[] arr, int[][] dp) {
        // Base case: If we have reached the first element
        if (ind == 0) {
            // Check if the target is 0 and the first element is also 0
            if (target == 0 && arr[0] == 0)
                return 2;
            // Check if the target is equal to the first element or 0
            if (target == 0 || target == arr[0])
                return 1;
            return 0;
        }

        // If the result for this subproblem has already been calculated, return it
        if (dp[ind][target] != -1)
            return dp[ind][target];

        // Calculate the number of ways without taking the current element
        int notTaken = countPartitionsUtil(ind - 1, target, arr, dp);

        // Initialize the number of ways taking the current element as 0
        int taken = 0;

        // If the current element is less than or equal to the target, calculate 'taken'
        if (arr[ind] <= target)
            taken = countPartitionsUtil(ind - 1, target - arr[ind], arr, dp);

        // Store the result in the dp array and return it
        return dp[ind][target] = (notTaken + taken);
    }

    // Function to find the number of ways to achieve the target sum
    static int targetSum(int n, int target, int[] arr) {
        int totSum = 0;

        // Calculate the total sum of elements in the array
        for (int i = 0; i < arr.length; i++) {
            totSum += arr[i];
        }

        // Checking for edge cases
        if (totSum - target < 0)
            return 0;
        if ((totSum - target) % 2 == 1)
            return 0;

        // Calculate the second sum based on the total sum and the target
        int s2 = (totSum - target) / 2;

        // Create a 2D array to store results of subproblems
        int dp[][] = new int[n][s2 + 1];

        // Initialize the dp array with -1 to indicate that subproblems are not solved
        // yet
        for (int row[] : dp)
            Arrays.fill(row, -1);

        // Call the countPartitionsUtil function to calculate the number of ways
        return countPartitionsUtil(n - 1, s2, arr, dp);
    }

    // Function to find the number of ways to achieve the target sum
    static int findWays(int[] num, int tar) {
        int n = num.length;

        // Create a 2D array to store results of subproblems
        int[][] dp = new int[n][tar + 1];

        // Initialize the dp array for the first element of the array
        if (num[0] == 0)
            dp[0][0] = 2; // 2 cases - pick and not pick
        else
            dp[0][0] = 1; // 1 case - not pick

        if (num[0] != 0 && num[0] <= tar)
            dp[0][num[0]] = 1; // 1 case - pick

        // Fill the dp array using dynamic programming
        for (int ind = 1; ind < n; ind++) {
            for (int target = 0; target <= tar; target++) {
                int notTaken = dp[ind - 1][target];

                int taken = 0;
                if (num[ind] <= target)
                    taken = dp[ind - 1][target - num[ind]];

                dp[ind][target] = (notTaken + taken) % mod;
            }
        }

        return dp[n - 1][tar];
    }

    // Function to calculate the number of ways to achieve the target sum
    static int targetSumDP(int n, int target, int[] arr) {
        int totSum = 0;

        // Calculate the total sum of elements in the array
        for (int i = 0; i < n; i++) {
            totSum += arr[i];
        }

        // Checking for edge cases
        if (totSum - target < 0 || (totSum - target) % 2 == 1)
            return 0;

        return findWays(arr, (totSum - target) / 2);
    }

    static int mod = (int) (Math.pow(10, 9) + 7);

    // Function to find the number of ways to achieve the target sum
    static int findWaysOP(int[] num, int tar) {
        int n = num.length;

        // Create an array to store results of subproblems for the current element
        int prev[] = new int[tar + 1];

        // Initialize the prev array for the first element of the array
        if (num[0] == 0)
            prev[0] = 2; // 2 cases - pick and not pick
        else
            prev[0] = 1; // 1 case - not pick

        if (num[0] != 0 && num[0] <= tar)
            prev[num[0]] = 1; // 1 case - pick

        // Fill the prev array using dynamic programming
        for (int ind = 1; ind < n; ind++) {
            int cur[] = new int[tar + 1];
            for (int target = 0; target <= tar; target++) {
                int notTaken = prev[target];

                int taken = 0;
                if (num[ind] <= target)
                    taken = prev[target - num[ind]];

                cur[target] = (notTaken + taken) % mod;
            }
            prev = cur;
        }

        return prev[tar];
    }

    // Function to calculate the number of ways to achieve the target sum
    static int targetSumOP(int n, int target, int[] arr) {
        int totSum = 0;

        // Calculate the total sum of elements in the array
        for (int i = 0; i < n; i++) {
            totSum += arr[i];
        }

        // Checking for edge cases
        if (totSum - target < 0 || (totSum - target) % 2 == 1)
            return 0;

        return findWaysOP(arr, (totSum - target) / 2);
    }


    public static void main(String[] args) {
        int arr[] = { 1, 1, 1, 1, 1 };
        int n = arr.length;
        int target = 3;
        System.out.println(targetSum(n, target, arr)); // 5
        // Time Complexity: O(N*K)

        // Reason: There are N*K states therefore at max ‘N*K’ new problems will be solved.

        // Space Complexity: O(N*K) + O(N)

        // Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*K)).
        System.out.println(targetSumDP(n, target, arr)); // 5
        // Time Complexity: O(N*K)

        // Reason: There are two nested loops

        // Space Complexity: O(N*K)

        // Reason: We are using an external array of size ‘N*K’. Stack Space is eliminated.
        System.out.println(targetSumOP(n, target, arr)); // 5
        // Time Complexity: O(N*K)

        // Reason: There are three nested loops

        // Space Complexity: O(K)
    }

}
