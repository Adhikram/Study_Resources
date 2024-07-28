package Questions.String;

import java.util.HashMap;
import java.util.Map;

/*
https://leetcode.com/problems/minimum-window-substring/description/
 Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
Time Complexity: O(n + m)
Space Complexity: O(n + m)
 */
public class MinimumWindowSubstring {
    public String minWindow(String s, String t) {
        // Edge case: if s or t is null or the length of s is less than the length of t,
        // return an empty string
        if (s == null || t == null || s.length() < t.length()) {
            return "";
        }

        // Create a frequency map for characters in t
        Map<Character, Integer> targetFreq = new HashMap<>();
        for (char c : t.toCharArray()) {
            targetFreq.put(c, targetFreq.getOrDefault(c, 0) + 1);
        }

        // Array to keep track of characters' frequencies in the current window of s
        int[] windowFreq = new int[256];
        int required = targetFreq.size(); // Number of unique characters in t
        int formed = 0; // Number of unique characters in the current window that match the target
                        // frequency

        // Sliding window pointers
        int left = 0, right = 0;
        int minLength = Integer.MAX_VALUE; // Length of the minimum window found
        int minLeft = 0, minRight = 0; // Boundaries of the minimum window

        // Expand the window by moving the right pointer
        while (right < s.length()) {
            char rightChar = s.charAt(right);
            windowFreq[rightChar]++;

            // If the current character in the window matches the target frequency,
            // increment formed
            if (targetFreq.containsKey(rightChar) && windowFreq[rightChar] == targetFreq.get(rightChar)) {
                formed++;
            }

            // Contract the window by moving the left pointer until the window is invalid
            while (formed == required) {
                // Update the minimum window if a smaller valid window is found
                if (right - left + 1 < minLength) {
                    minLength = right - left + 1;
                    minLeft = left;
                    minRight = right;
                }

                char leftChar = s.charAt(left);
                windowFreq[leftChar]--;

                // If the current character's frequency in the window is less than the target
                // frequency, decrement formed
                if (targetFreq.containsKey(leftChar) && windowFreq[leftChar] < targetFreq.get(leftChar)) {
                    formed--;
                }

                left++;
            }

            right++;
        }

        // Return the minimum window substring if found, otherwise return an empty
        // string
        return minLength == Integer.MAX_VALUE ? "" : s.substring(minLeft, minRight + 1);
    }
    public static void main(String[] args) {
        MinimumWindowSubstring m = new MinimumWindowSubstring();
        String s = "ADOBECODEBANC";
        String t = "ABC";
        System.out.println(m.minWindow(s, t));
    }
}