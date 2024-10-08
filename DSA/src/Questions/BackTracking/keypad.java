package Questions.BackTracking;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
/*
 https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
 */
public class keypad {
    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty())
            return Collections.emptyList();

        String[] phone_map = { "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
        List<String> output = new ArrayList<>();
        backtrack("", digits, phone_map, output);
        return output;
    }

    private void backtrack(String combination, String next_digits, String[] phone_map, List<String> output) {
        if (next_digits.isEmpty()) {
            output.add(combination);
        } else {
            String letters = phone_map[next_digits.charAt(0) - '2'];
            for (char letter : letters.toCharArray()) {
                backtrack(combination + letter, next_digits.substring(1), phone_map, output);
            }
        }
    }
    /*
     * Time complexity: O(4^n) where n is the number of digits in the input string
     */

    public static void main(String[] args) {
        keypad k = new keypad();
        System.out.println(k.letterCombinations("223"));
    }
}
