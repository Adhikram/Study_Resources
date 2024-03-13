package Questions.String;

import java.util.HashMap;

public class MakeStringEmpty {
    public String lastNonEmptyString(String s) {
        HashMap<Character, Integer> charFrequency = new HashMap<>();
        HashMap<Character, Integer> charLastIndex = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            charLastIndex.put(s.charAt(i), i);
            charFrequency.put(s.charAt(i), charFrequency.getOrDefault(s.charAt(i), 0) + 1);
        }

        int maxFrequency = 0;
        for (int frequency : charFrequency.values()) {
            maxFrequency = Math.max(maxFrequency, frequency);
        }

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            if (charFrequency.get(currentChar) == maxFrequency && charLastIndex.get(currentChar) == i) {
                result.append(currentChar);
            }
        }
        return result.toString();

    }
    public static void main(String[] args) {
        MakeStringEmpty makeStringEmpty = new MakeStringEmpty();
        System.out.println(makeStringEmpty.lastNonEmptyString("ababab"));
        System.out.println(makeStringEmpty.lastNonEmptyString("abc"));
        System.out.println(makeStringEmpty.lastNonEmptyString("abababab"));
    }
}
