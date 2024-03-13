package Questions.Array;

import java.util.HashMap;

public class LongestNonRepeatingSubString {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> hash = new HashMap<>();
        int result = 0;
        int start = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (hash.containsKey(ch)) {
                start = Math.max(start, hash.get(ch) + 1);
            }
            hash.put(ch, i);
            result = Math.max(result, i - start + 1);
        }

        return result;
    }

    public static void main(String[] args) {
        LongestNonRepeatingSubString longestNonRepeatingSubString = new LongestNonRepeatingSubString();
        System.out.println(longestNonRepeatingSubString.lengthOfLongestSubstring("abcabcdb"));
    }
}
