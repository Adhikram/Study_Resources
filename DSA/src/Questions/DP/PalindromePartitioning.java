package Questions.DP;

import java.util.Arrays;

public class PalindromePartitioning {

    // Problem Statement: Given a string s, partition s such that every substring of
    // the partition is a palindrome. Return the minimum cuts needed for a
    // palindrome partitioning of s.
    static boolean isPalindrome(int i, int j, String s) {
        while (i < j) {
            if (s.charAt(i) != s.charAt(j))
                return false;
            i++;
            j--;
        }
        return true;
    }

    static int f(int i, int n, String str) {
        // Base case:
        if (i == n)
            return 0;

        int minCost = Integer.MAX_VALUE;
        // String[i...j]
        for (int j = i; j < n; j++) {
            if (isPalindrome(i, j, str)) {
                int cost = 1 + f(j + 1, n, str);
                minCost = Math.min(minCost, cost);
            }
        }
        return minCost;
    }

    static int palindromePartitioningRecursive(String str) {
        int n = str.length();
        return f(0, n, str) - 1;
    }
    // Time Complexity: Exponential
    // Reason: We are using a recursive approach and checking all the possible
    // partitions

    static int f(int i, int n, String str, int[] dp) {
        // Base case:
        if (i == n)
            return 0;

        if (dp[i] != -1)
            return dp[i];
        int minCost = Integer.MAX_VALUE;
        // String[i...j]
        for (int j = i; j < n; j++) {
            if (isPalindrome(i, j, str)) {
                int cost = 1 + f(j + 1, n, str, dp);
                minCost = Math.min(minCost, cost);
            }
        }
        return dp[i] = minCost;
    }

    static int palindromePartitioningMemoization(String str) {
        int n = str.length();
        int[] dp = new int[n];
        Arrays.fill(dp, -1);
        return f(0, n, str, dp) - 1;
    }
    // Time Complexity: O(N2)
    // Reason: There are a total of N states and inside each state, a loop of size
    // N(apparently) is running.

    // Space Complexity: O(N) + Auxiliary stack space O(N)
    // Reason: The first O(N) is for the dp array of size N.

    static int palindromePartitioningTabulation(String str) {
        int n = str.length();
        int[] dp = new int[n + 1];
        dp[n] = 0;
        for (int i = n - 1; i >= 0; i--) {
            int minCost = Integer.MAX_VALUE;
            // String[i...j]
            for (int j = i; j < n; j++) {
                if (isPalindrome(i, j, str)) {
                    int cost = 1 + dp[j + 1];
                    minCost = Math.min(minCost, cost);
                }
            }
            dp[i] = minCost;
        }
        return dp[0] - 1;
    }

    // Time Complexity: O(N2)
    // Reason: There are a total of N states and inside each state a loop of size
    // N(apparently) is running.

    // Space Complexity: O(N)
    // Reason: O(N) is for the dp array we have used.

    public static void main(String[] args) {
        String str = "aabaa";
        System.out.println(palindromePartitioningRecursive(str));
        System.out.println(palindromePartitioningMemoization(str));
        System.out.println(palindromePartitioningTabulation(str));
    }

}
