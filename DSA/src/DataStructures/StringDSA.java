package DataStructures;

import java.util.HashMap;
import java.util.Map;

public class StringDSA {

    // Method to check if a string is a palindrome
    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    // Method to find the first non-repeating character in a string
    public char firstNonRepeatingChar(String s) {
        Map<Character, Integer> charCount = new HashMap<>();
        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
        for (char c : s.toCharArray()) {
            if (charCount.get(c) == 1) {
                return c;
            }
        }
        return '_'; // Return '_' if no non-repeating character is found
    }

    // Method to reverse a string
    public StringDSA reverseString(String s) {
        char[] charArray = s.toCharArray();
        int left = 0, right = charArray.length - 1;
        while (left < right) {
            char temp = charArray[left];
            charArray[left] = charArray[right];
            charArray[right] = temp;
            left++;
            right--;
        }
        return new java.lang.String(charArray);
    }

    // Method to check if two strings are anagrams
    public boolean areAnagrams(String s1, String s2) {
        if (s1.length() != s2.length()) {
            return false;
        }
        int[] charCount = new int[26];
        for (char c : s1.toCharArray()) {
            charCount[c - 'a']++;
        }
        for (char c : s2.toCharArray()) {
            if (--charCount[c - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }

    // Method to find the longest common prefix among an array of strings
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }
        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++) {
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) {
                    return "";
                }
            }
        }
        return prefix;
    }

    // Method to find the longest palindromic substring
    public String longestPalindromicSubstring(String s) {
        if (s == null || s.length() < 1) {
            return "";
        }
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            int len1 = expandAroundCenter(s, i, i);
            int len2 = expandAroundCenter(s, i, i + 1);
            int len = Math.max(len1, len2);
            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        return s.substring(start, end + 1);
    }

    private int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }

    // Method to perform basic string compression using the counts of repeated characters
    public String compressString(String s) {
        StringBuilder compressed = new StringBuilder();
        int countConsecutive = 0;
        for (int i = 0; i < s.length(); i++) {
            countConsecutive++;
            if (i + 1 >= s.length() || s.charAt(i) != s.charAt(i + 1)) {
                compressed.append(s.charAt(i));
                compressed.append(countConsecutive);
                countConsecutive = 0;
            }
        }
        return compressed.length() < s.length() ? compressed.toString() : s;
    }

    // Method to check if a string contains only digits
    public boolean isNumeric(String s) {
        for (char c : s.toCharArray()) {
            if (!Character.isDigit(c)) {
                return false;
            }
        }
        return true;
    }

    // Method to convert a string to an integer
    public int stringToInt(String s) {
        int result = 0;
        int sign = 1;
        int i = 0;
        if (s.charAt(0) == '-') {
            sign = -1;
            i++;
        }
        for (; i < s.length(); i++) {
            result = result * 10 + (s.charAt(i) - '0');
        }
        return result * sign;
    }

    public static void main(String[] args) {
        StringDSA string = new StringDSA();

        // Test isPalindrome
        System.out.println(string.isPalindrome("racecar")); // true
        System.out.println(string.isPalindrome("hello")); // false

        // Test firstNonRepeatingChar
        System.out.println(string.firstNonRepeatingChar("swiss")); // 'w'
        System.out.println(string.firstNonRepeatingChar("aabbcc")); // '_'

        // Test reverseString
        System.out.println(string.reverseString("hello")); // "olleh"

        // Test areAnagrams
        System.out.println(string.areAnagrams("listen", "silent")); // true
        System.out.println(string.areAnagrams("hello", "world")); // false

        // Test longestCommonPrefix
        String[] strs = {"flower", "flow", "flight"};
        System.out.println(string.longestCommonPrefix(strs)); // "fl"

        // Test longestPalindromicSubstring
        System.out.println(string.longestPalindromicSubstring("babad")); // "bab" or "aba"

        // Test compressString
        System.out.println(string.compressString("aabcccccaaa")); // "a2b1c5a3"

        // Test isNumeric
        System.out.println(string.isNumeric("12345")); // true
        System.out.println(string.isNumeric("123a5")); // false

        // Test stringToInt
        System.out.println(string.stringToInt("12345")); // 12345
        System.out.println(string.stringToInt("-12345")); // -12345
    }
}