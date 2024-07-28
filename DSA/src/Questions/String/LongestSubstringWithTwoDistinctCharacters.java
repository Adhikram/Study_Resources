package Questions.String;

/*
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/
 Given a string s, return the length of the longest 
substring
 that contains at most two distinct characters.

 

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
 

Constraints:

1 <= s.length <= 105
s consists of English letters.
Time Complexity: O(n)
Space Complexity: O(1)
 */
public class LongestSubstringWithTwoDistinctCharacters {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int max = 0;
        int uni = 0;
        int[] rec = new int[256];
        char[] chars = s.toCharArray();
        int start = 0;
        for (int i = 0; i < s.length(); i++) {
            int n = ++rec[chars[i]];
            if (n == 1)
                uni++;
            while (uni == 3) {
                n = --rec[chars[start++]];
                if (n == 0)
                    uni--;
            }
            max = Math.max(max, i - start + 1);
        }
        return max;
    }
    public static void main(String[] args) {
        LongestSubstringWithTwoDistinctCharacters l = new LongestSubstringWithTwoDistinctCharacters();
        String s = "eceba";
        System.out.println(l.lengthOfLongestSubstringTwoDistinct(s));
    }

}
