package Questions.DP;

import java.util.Arrays;

public class LongestCommonSubsequence {
    static int lcsUtil(String s1, String s2, int ind1, int ind2, int[][] dp) {
        // Base case: If either of the strings reaches the end, return 0
        if (ind1 < 0 || ind2 < 0)
            return 0;

        // If the result for this subproblem has already been calculated, return it
        if (dp[ind1][ind2] != -1)
            return dp[ind1][ind2];

        // If the characters at the current indices are the same, increment the LCS
        // length
        if (s1.charAt(ind1) == s2.charAt(ind2))
            return dp[ind1][ind2] = 1 + lcsUtil(s1, s2, ind1 - 1, ind2 - 1, dp);

        // If the characters are different, choose the maximum LCS length by either
        // skipping a character in s1 or skipping a character in s2
        else
            return dp[ind1][ind2] = Math.max(lcsUtil(s1, s2, ind1, ind2 - 1, dp),
                    lcsUtil(s1, s2, ind1 - 1, ind2, dp));
    }

    // Function to find the length of the Longest Common Subsequence (LCS)
    static int lcsRecursive(String s1, String s2) {
        int n = s1.length();
        int m = s2.length();

        // Create a 2D array to store results of subproblems
        int[][] dp = new int[n][m];

        // Initialize the dp array with -1 to indicate that subproblems are not solved
        // yet
        for (int[] rows : dp)
            Arrays.fill(rows, -1);

        // Call the recursive function to find the LCS length
        return lcsUtil(s1, s2, n - 1, m - 1, dp);
    }

    // Time Complexity: O(N*M)

    // Reason: There are N*M states therefore at max ‘N*M’ new problems will be
    // solved.

    // Space Complexity: O(N*M) + O(N+M)

    // Reason: We are using an auxiliary recursion stack space(O(N+M)) (see the
    // recursive tree, in the worst case, we will go till N+M calls at a time) and a
    // 2D array ( O(N*M)).

    // Function to find the length of the Longest Common Subsequence (LCS)
    static int lcsTabulation(String s1, String s2) {
        int n = s1.length();
        int m = s2.length();

        // Each cell (i,j) in the dp array indicates the length of the LCS for s1[0:i-1]
        // and s2[0:j-1]
        int[][] dp = new int[n + 1][m + 1];

        // Initialize the dp array with -1 to indicate that subproblems are not solved
        // yet
        for (int[] row : dp)
            Arrays.fill(row, -1);

        // Initialize the first row and first column with zeros since LCS with an empty
        // string is zero
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 0;
        }
        for (int i = 0; i <= m; i++) {
            dp[0][i] = 0;
        }

        // Fill the dp array using dynamic programming
        for (int ind1 = 1; ind1 <= n; ind1++) {
            for (int ind2 = 1; ind2 <= m; ind2++) {
                // If the characters at the current indices are the same, increment the LCS
                // length
                if (s1.charAt(ind1 - 1) == s2.charAt(ind2 - 1))
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1];
                // If the characters are different, choose the maximum LCS length by either
                // excluding a character in s1 or excluding a character in s2
                else
                    dp[ind1][ind2] = Math.max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1]);
            }
        }

        return dp[n][m]; // Return the length of the Longest Common Subsequence (LCS)
    }
    // Time Complexity: O(N*M)

    // Reason: There are two nested loops

    // Space Complexity: O(N*M)

    // Reason: We are using an external array of size ‘N*M)’. Stack Space is
    // eliminated.

    // Function to find the length of the Longest Common Subsequence (LCS)
    static int lcsOptimized(String s1, String s2) {
        int n = s1.length();
        int m = s2.length();

        // Create arrays to store the LCS lengths
        int[] prev = new int[m + 1];
        int[] cur = new int[m + 1];

        // Iterate through the strings and calculate LCS lengths
        for (int ind1 = 1; ind1 <= n; ind1++) {
            for (int ind2 = 1; ind2 <= m; ind2++) {
                // If the characters at the current indices are the same, increment the LCS
                // length
                if (s1.charAt(ind1 - 1) == s2.charAt(ind2 - 1))
                    cur[ind2] = 1 + prev[ind2 - 1];
                // If the characters are different, choose the maximum LCS length by either
                // excluding a character in s1 or excluding a character in s2
                else
                    cur[ind2] = Math.max(prev[ind2], cur[ind2 - 1]);
            }
            // Update the 'prev' array to the values of 'cur' for the next iteration
            prev = (int[]) (cur.clone());
        }

        return prev[m]; // Return the length of the Longest Common Subsequence (LCS)
    }
    // Time Complexity: O(N*M)

    // Reason: There are two nested loops.

    // Space Complexity: O(M)

    // Reason: We are using an external array of size ‘M+1’ to store only two rows.

    public static void main(String[] args) {
        String s1 = "AGGTAB";
        String s2 = "GXTXAYB";

        System.out.println(lcsRecursive(s1, s2)); // Output: 4
        System.out.println(lcsTabulation(s1, s2)); // Output: 4
        System.out.println(lcsOptimized(s1, s2)); // Output: 4
    }

}
