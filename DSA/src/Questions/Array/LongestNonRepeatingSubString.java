package Questions.Array;

import java.util.HashMap;

public class LongestNonRepeatingSubString {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> hash = new HashMap<>();
        int result = 0;
        // Valid substring start index for the current character
        int start = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (hash.containsKey(ch)) {
                // If the character is already present in the hash, then we update the start
                // index to the next index of the character
                start = Math.max(start, hash.get(ch));
            }
            hash.put(ch, i);
            result = Math.max(result, i - start);
        }

        return result;
    }
    /*
     * Time complexity: O(n) where n is the length of the string
     */

    public static void main(String[] args) {
        LongestNonRepeatingSubString longestNonRepeatingSubString = new LongestNonRepeatingSubString();
        System.out.println(longestNonRepeatingSubString.lengthOfLongestSubstring("abcabcdb"));
    }
}
