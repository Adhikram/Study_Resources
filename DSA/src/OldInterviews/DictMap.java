package OldInterviews;

import java.util.HashMap;

public class DictMap {
     public static HashMap<String, String> createAlphabetMap() {
        HashMap<String, String> map = new HashMap<>();

        for (int i = 1; i <= 26; i++) {
            char letter = (char) ('A' + i - 1); // Convert number to uppercase letter
            map.put(String.valueOf(i), String.valueOf(letter));
        }

        return map;
    }

    public static int decode(String str, HashMap<String, String> store) {
        // Base case: if the string is empty, there's no valid decoding
        if (str.isEmpty()) {
            return 0;
        }

        // Memoization map to store already calculated results
        HashMap<String, Integer> memo = new HashMap<>();

        // Helper function to use memoization
        return decodeHelper(str, store, memo);
    }

    private static int decodeHelper(String str, HashMap<String, String> store, HashMap<String, Integer> memo) {
        // If we've already calculated the result for this substring, return it
        if (memo.containsKey(str)) {
            return memo.get(str);
        }

        // If the string is empty, there's one valid decoding (an empty string)
        if (str.isEmpty()) {
            return 1;
        }

        int result = 0;

        // Check the first one or two characters to see if they form a valid letter
        for (int len = 1; len <= 2 && len <= str.length(); len++) {
            String part = str.substring(0, len);
            if (store.containsKey(part)) {
                result += decodeHelper(str.substring(len), store, memo);
            }
        }

        // Store the result in memo before returning
        memo.put(str, result);
        return result;
    }

    public static void main(String[] args) {
        // Example strings and expected outputs
        // "121" -> "ABA", "AU", "LA" -> 3
        // "1234" -> "ABCD", "LCD", "AWD" -> 3
        // "96" -> "IF" -> 1
        // "90" -> 0

        HashMap<String, String> store = createAlphabetMap();

        System.out.println(decode("121", store));  // Expected output: 3
        System.out.println(decode("1234", store)); // Expected output: 3
        System.out.println(decode("96", store));   // Expected output: 1
        System.out.println(decode("90", store));   // Expected output: 0
    }
}
