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
    bool canConstruct(string s, int k) {

        int a[26];  // to store the count of charachters
        memset(a,0,sizeof(a));
        int n=s.length();
        if(k>n)return 0;
        for(int i=0;i<n;i++)
        {
            a[s[i]-'a']++;
        }
        int res=0;
        for(int i=0;i<26;i++)
        {
            // if count is odd, then increment the resultant
            if(a[i]%2)res++;
        }
        return res<=k;
    }
}
