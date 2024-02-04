package Questions.Array;

import java.util.HashMap;

public class LongestNonRepeatingSubString {
        public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> hash = new HashMap<>();
        int result = -1;

        for(Char ch: s.toCharArray()){
            if(hash.containsKey(ch)){
                result = Math.max(result, hash.size());
                hash.clear();
            }
            hash.put(ch, 1);
        }

        if(result == -1){
            return s.length();
        }else{
            return result;
        }
    }
    public static void main(String[] args) {
        LongestNonRepeatingSubString longestNonRepeatingSubString = new LongestNonRepeatingSubString();
        System.out.println(longestNonRepeatingSubString.lengthOfLongestSubstring("abcabcbb"));
    }
}
