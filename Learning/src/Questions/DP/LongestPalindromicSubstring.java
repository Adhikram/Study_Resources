package Questions.DP;

public class LongestPalindromicSubstring {
    public static String longestPalindrome(String s) {
        int start = 0;
        int length = 1;
        int n = s.length();
        boolean[] dp = new boolean[n];

        // Each Cell represents the max palindrome from this point to what ever index we
        // are at
        for (int index = 1; index < n; index++) {
            for (int i = 0; i < index; i++) {
                // If there is less then two letters
                if (index - i <= 2) {
                    dp[i] = s.charAt(i) == s.charAt(index);
                } else {
                    // i+1 represents the status of (index - 1)(i)
                    dp[i] = s.charAt(i) == s.charAt(index) && dp[i + 1];
                }
                System.out.print( "("+ i + "," + index + ") -> " + dp[i] + ",");
                // If the current palindrome is greater then the previous palindrome
                if (dp[i] && index - i + 1 > length) {
                    start = i;
                    length = index - i + 1;
                }
            }
            System.out.println();
        }
        return s.substring(start, start + length);
    }

    public static void main(String[] args) {
        String s = "babad";
        String s1 = "cbbdadbb";
        System.out.println(longestPalindrome(s));
        System.out.println(longestPalindrome(s1));
    }
}
