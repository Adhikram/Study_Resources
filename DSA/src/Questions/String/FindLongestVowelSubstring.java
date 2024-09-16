package Questions.String;
/*
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description

Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.


Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.

 */
public class FindLongestVowelSubstring {
    private static final int[] VOWEL_MASK = new int[128];
    static {
        VOWEL_MASK['a'] = 1; // 00001
        VOWEL_MASK['e'] = 2; // 00010
        VOWEL_MASK['i'] = 4; // 00100
        VOWEL_MASK['o'] = 8; // 01000
        VOWEL_MASK['u'] = 16; // 10000
    }

    public int findTheLongestSubstring(String s) {
        // To store the first occurrence of each bitmask (0 to 31)
        int[] firstOccurrence = new int[32];
        java.util.Arrays.fill(firstOccurrence, -1);
        firstOccurrence[0] = 0; // Bitmask 0 occurs at position -1 (before the string starts)

        int maxLength = 0;
        int mask = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            // Update mask if it's a vowel
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
                mask ^= VOWEL_MASK[ch];
            }

            // If the current mask was seen before, calculate the length of the substring
            if (firstOccurrence[mask] != -1) {
                maxLength = Math.max(maxLength, i + 1 - firstOccurrence[mask]);
            } else {
                // Store the first occurrence of this bitmask
                firstOccurrence[mask] = i + 1;
            }
        }

        return maxLength;
    }

    public static void main(String[] args) {
        FindLongestVowelSubstring findLongestVowelSubstring = new FindLongestVowelSubstring();
        String s = "eleetminicoworoep";
        System.out.println(findLongestVowelSubstring.findTheLongestSubstring(s));
    }
}
