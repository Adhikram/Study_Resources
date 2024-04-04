package Questions.String;

public class KPalindrome {

    public static boolean isKPalindrome(String s, int k) {
        int n = s.length();
        int[][] dp = new int[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            dp[i][0] = i;
        }
        for (int i = 0; i <= n; i++) {
            dp[0][i] = i;
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = s.charAt(i - 1) == s.charAt(n - j) ? dp[i - 1][j - 1]
                        : 1 + Math.min(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[n][n] <= 2 * k;
    }

    public static boolean canConstruct(String s, int k) {
        int[] a = new int[26]; // to store the count of characters
        int n = s.length();
        if (k > n)
            return false;
        for (int i = 0; i < n; i++) {
            a[s.charAt(i) - 'a']++;
        }
        int res = 0;
        for (int i = 0; i < 26; i++) {
            // if count is odd, then increment the result
            if (a[i] % 2 != 0)
                res++;
        }
        return res <= k;
    }

    public static void main(String[] args) {
        String s = "abcdeca";
        int k = 2;
        System.out.println(isKPalindrome(s, k));
        System.out.println(canConstruct(s, k));
    }
}
