package Questions.DP;

public class LongestCommonSubsequence {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text2.length();
        int n = text1.length();
        // 1. 2D Recursive
        // int[][] store = new int[m + 1][n + 1];

        // for (int i = 1; i <= m; i++) {
        // for (int j = 1; j <= n; j++) {
        // if (text2.charAt(i - 1) == text1.charAt(j - 1)) {
        // store[i][j] = store[i - 1][j - 1] + 1;
        // } else {
        // store[i][j] = Math.max(store[i][j - 1], store[i - 1][j]);
        // }
        // }
        // }
        // return store[m][n];

        // 2. 1D Recursive
        int[] store = new int[n + 1];

        for (int i = 1; i <= m; i++) {
            int prev = 0;
            for (int j = 1; j <= n; j++) {
                int temp = store[j];
                if (text2.charAt(i - 1) == text1.charAt(j - 1)) {
                    store[j] = prev + 1;
                } else {
                    store[j] = Math.max(store[j - 1], store[j]);
                }
                prev = temp;
            }
        }
        return store[n];

    }

    public static void main(String[] args) {
        LongestCommonSubsequence longestCommonSubsequence = new LongestCommonSubsequence();
        String text1 = "abcde";
        String text2 = "ace";
        int result = longestCommonSubsequence.longestCommonSubsequence(text1, text2);
        System.out.println("Longest Common Subsequence: " + result);
    }
}
