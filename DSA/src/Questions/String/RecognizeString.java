package Questions.String;

/*
https://leetcode.com/problems/reorganize-string/description/
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
Time Complexity: O(n)
Space Complexity: O(1)
 */
public class RecognizeString {
    public String reorganizeString(String s) {
        int[] freq = new int[26]; // to Store Frequency of each alphabet
        char[] arr = s.toCharArray();

        for (int i = 0; i < arr.length; i++) { // store the frequency
            freq[arr[i] - 'a']++;
        }

        int max = 0, letter = 0;

        for (int i = 0; i < 26; i++) { // find the max frequency
            if (freq[i] > max) {
                max = freq[i];
                letter = i;
            }
        }

        if (max > (s.length() + 1) / 2)
            return ""; // if max is more than half then not possible

        int idx = 0;
        char[] res = new char[s.length()];

        while (freq[letter] > 0) { // distribute the max freq char into even indices
            res[idx] = (char) (letter + 'a');
            idx += 2;
            freq[letter]--;
        }

        for (int i = 0; i < 26; i++) {
            while (freq[i] > 0) {
                if (idx >= s.length())
                    idx = 1; // all even indices filled, so switch to odd indices
                res[idx] = (char) (i + 'a');
                idx += 2;
                freq[i]--;
            }

        }

        return String.valueOf(res);
    }

    public static void main(String[] args) {
        RecognizeString recognizeString = new RecognizeString();
        System.out.println(recognizeString.reorganizeString("aab")); // Output: "aba"
        System.out.println(recognizeString.reorganizeString("aaab")); // Output: ""
    }
}
