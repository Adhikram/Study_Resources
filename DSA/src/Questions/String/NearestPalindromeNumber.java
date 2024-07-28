package Questions.String;

import java.util.ArrayList;
import java.util.List;

/*
https://leetcode.com/problems/find-the-closest-palindrome/description/
 Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 

Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].
Time Complexity: O(N)
Space Complexity: O(N)
 */
public class NearestPalindromeNumber {
    public String nearestPalindromic(String n) {
        // edge cases, no

        int len = n.length();
        int i = len % 2 == 0 ? len / 2 - 1 : len / 2;
        long left = Long.parseLong(n.substring(0, i + 1));

        // input: n 12345
        List<Long> candidate = new ArrayList<>();
        candidate.add(getPalindrome(left, len % 2 == 0)); // 12321
        candidate.add(getPalindrome(left + 1, len % 2 == 0)); // 12421
        candidate.add(getPalindrome(left - 1, len % 2 == 0)); // 12221
        candidate.add((long) Math.pow(10, len - 1) - 1); // 9999
        candidate.add((long) Math.pow(10, len) + 1); // 100001

        long diff = Long.MAX_VALUE, res = 0, nl = Long.parseLong(n);
        for (long cand : candidate) {
            if (cand == nl)
                continue;
            if (Math.abs(cand - nl) < diff) {
                diff = Math.abs(cand - nl);
                res = cand;
            } else if (Math.abs(cand - nl) == diff) {
                res = Math.min(res, cand);
            }
        }

        return String.valueOf(res);
    }

    private long getPalindrome(long left, boolean even) {
        long res = left;
        if (!even)
            left = left / 10;
        while (left > 0) {
            res = res * 10 + left % 10;
            left /= 10;
        }
        return res;
    }

    public static void main(String[] args) {
        NearestPalindromeNumber obj = new NearestPalindromeNumber();
        System.out.println(obj.nearestPalindromic("123"));
        System.out.println(obj.nearestPalindromic("100"));
    }
}