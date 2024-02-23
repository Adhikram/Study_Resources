package Questions.DP;

import java.util.Arrays;

public class EditDistance {
    // We are given two strings ‘S1’ and ‘S2’. We need to convert S1 to S2. The
    // following three operations are allowed:

    // Deletion of a character.
    // Replacement of a character with another one.
    // Insertion of a character.
    // We have to return the minimum number of operations required to convert S1 to
    // S2 as our answer.

    // Function to calculate the minimum edit distance between two strings
    static int editDistanceUtil(String S1, String S2, int i, int j, int[][] dp) {
        // Base cases
        if (i < 0)
            return j + 1;
        if (j < 0)
            return i + 1;

        // If the result is already computed, return it
        if (dp[i][j] != -1)
            return dp[i][j];

        // If the characters at the current positions match, no edit is needed
        if (S1.charAt(i) == S2.charAt(j))
            return dp[i][j] = editDistanceUtil(S1, S2, i - 1, j - 1, dp);

        // Minimum of three choices:
        // 1. Replace the character in S1 with the character in S2.
        // 2. Delete the character in S1.
        // 3. Insert the character from S2 into S1.
        else
            return dp[i][j] = 1 + Math.min(editDistanceUtil(S1, S2, i - 1, j - 1, dp),
                    Math.min(editDistanceUtil(S1, S2, i - 1, j, dp), editDistanceUtil(S1, S2, i, j - 1, dp)));
    }

    static int editDistanceRecursive(String S1, String S2) {
        int n = S1.length();
        int m = S2.length();

        int[][] dp = new int[n][m];
        for (int row[] : dp)
            Arrays.fill(row, -1);

        // Call the recursive helper function
        return editDistanceUtil(S1, S2, n - 1, m - 1, dp);
    }

    // Time Complexity: O(N*M)

    // Reason: There are N*M states therefore at max ‘N*M’ new problems will be
    // solved.

    // Space Complexity: O(N*M) + O(N+M)

    // Reason: We are using a recursion stack space(O(N+M)) and a 2D array (
    // O(N*M)).

    // Function to calculate the minimum edit distance between two strings
    static int editDistanceTabulation(String S1, String S2) {
        int n = S1.length();
        int m = S2.length();

        // Create a 2D array to store the minimum edit distances
        // Each cell (i, j) in the array represents the minimum edit distance between
        // the
        // S1[0..i-1] and S2[0..j-1]
        int[][] dp = new int[n + 1][m + 1];

        // If one of the strings is empty, the minimum edit distance is the length of
        // the other string
        for (int i = 0; i <= n; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= m; j++) {
            dp[0][j] = j;
        }

        // Fill the dp array using a bottom-up approach
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (S1.charAt(i - 1) == S2.charAt(j - 1)) {
                    // If the characters match, no edit is needed, so take the value from the
                    // diagonal.
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    // If the characters don't match, take the minimum of three possibilities:
                    // 1. Replace the character in S1 with the character in S2 (diagonal).
                    // 2. Delete the character in S1 (left).
                    // 3. Insert the character from S2 into S1 (up).
                    dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1]));
                }
            }
        }

        return dp[n][m];
    }
    // Time Complexity: O(N*M)

    // Reason: There are two nested loops

    // Space Complexity: O(N*M)

    // Reason: We are using an external array of size ‘N*M’. Stack Space is
    // eliminated.

    // Function to calculate the minimum edit distance between two strings
    static int editDistance(String S1, String S2) {
        int n = S1.length();
        int m = S2.length();

        // Create two arrays to store the previous and current rows of minimum edit
        // distances
        int[] prev = new int[m + 1];
        int[] cur = new int[m + 1];

        // Initialize the first row with their respective indices
        for (int j = 0; j <= m; j++) {
            prev[j] = j;
        }

        // Fill the cur array using a bottom-up approach
        for (int i = 1; i <= n; i++) {
            cur[0] = i;
            for (int j = 1; j <= m; j++) {
                if (S1.charAt(i - 1) == S2.charAt(j - 1)) {
                    // If the characters match, no edit is needed, so take the value from the
                    // diagonal.
                    cur[j] = prev[j - 1];
                } else {
                    // If the characters don't match, take the minimum of three possibilities:
                    // 1. Replace the character in S1 with the character in S2 (diagonal).
                    // 2. Delete the character in S1 (left).
                    // 3. Insert the character from S2 into S1 (up).
                    cur[j] = 1 + Math.min(prev[j - 1], Math.min(prev[j], cur[j - 1]));
                }
            }
            // Update prev array to store the current values
            prev = cur.clone();
        }

        return cur[m];
    }

    public static void main(String[] args) {
        String S1 = "sunday";
        String S2 = "saturday";
        System.out.println(editDistanceRecursive(S1, S2)); // 3
        System.out.println(editDistanceTabulation(S1, S2)); // 3
        System.out.println(editDistance(S1, S2)); // 3
    }
    // Time Complexity: O(N*M)

    // Reason: There are two nested loops.

    // Space Complexity: O(M)

    // Reason: We are using an external array of size ‘M+1’ to store two rows.
}
