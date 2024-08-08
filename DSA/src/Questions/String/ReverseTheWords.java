package Questions.String;
/*
https://leetcode.com/problems/reverse-words-in-a-string/description/
 Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

Time Complexity: O(N)
Space Complexity: O(N)
 */
public class ReverseTheWords {
    public static String reverseWords(String s) {
        StringBuilder result = new StringBuilder();
        int end = s.length() - 1;

        while (end >= 0) {
            // Skip trailing spaces
            while (end >= 0 && s.charAt(end) == ' ')
                end--;
            if (end < 0)
                break;

            int start = end;
            // Find the start of the word
            while (start >= 0 && s.charAt(start) != ' ')
                start--;

            // Append the word to the result
            if (result.length() > 0) {
                result.append(' ');
            }
            result.append(s.substring(start + 1, end + 1));

            // Move to the next word
            end = start - 1;
        }

        return result.toString();
    }

    public static void reverseWordsOP(char[] s) {
        int n = s.length;

        // Step 1: Reverse the entire string
        reverse(s, 0, n - 1);

        // Step 2: Reverse each word in the reversed string
        int start = 0;
        for (int end = 0; end < n; end++) {
            if (s[end] == ' ') {
                reverse(s, start, end - 1);
                start = end + 1;
            }
        }
        // Reverse the last word
        reverse(s, start, n - 1);
    }

    private static void reverse(char[] s, int left, int right) {
        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }

    public static void main(String[] args) {
        String s1 = "the sky is blue";
        reverseWords(s1);
        System.out.println(new String(s1)); // Output: "blue is sky the"

        String s2 = "  hello world  ";
        reverseWords(s2);
        System.out.println(new String(s2)); // Output: "world hello"

        String s3 = "a good   example";
        reverseWords(s3);
        System.out.println(new String(s3)); // Output: "example good a"
    }

}
