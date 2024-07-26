package Questions.String;
/*
https://leetcode.com/problems/sentence-screen-fitting/description/
 Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given sentence can be fitted on the screen.

The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.

 

Example 1:

Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.
Example 2:

Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
Output: 2
Explanation:
a-bcd- 
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.
Example 3:

Input: sentence = ["i","had","apple","pie"], rows = 4, cols = 5
Output: 1
Explanation:
i-had
apple
pie-i
had--
The character '-' signifies an empty space on the screen.
 

Constraints:

1 <= sentence.length <= 100
1 <= sentence[i].length <= 10
sentence[i] consists of lowercase English letters.
1 <= rows, cols <= 2 * 104
Time complexity: O(rows * cols)
Space complexity: O(n), where n is the length of the concatenated string formed by the sentence.
 */
public class SentenceScreenFitting {
    public int wordsTyping(String[] sentence, int rows, int cols) {
        // Concatenate all words in the sentence into a single string with spaces
        // between words
        // Adding an extra space at the end to handle edge cases where the last word
        // fits perfectly at the end of a row
        String s = String.join(" ", sentence) + " ";

        // Start keeps track of the current position in the concatenated string
        int start = 0;
        int len = s.length(); // Length of the concatenated string

        // Iterate over each row
        for (int i = 0; i < rows; i++) {
            start += cols; // Move the start pointer by the number of columns
            if (s.charAt(start % len) == ' ') {
                // If we land on a space, increment start to the next character
                start++;
            } else {
                // If we land in the middle of a word, backtrack to the previous space
                while (start > 0 && s.charAt((start - 1) % len) != ' ') {
                    start--;
                }
            }
        }

        // The number of times the sentence fits on the screen is given by start / len
        return start / len;
    }

    public static void main(String[] args) {
        SentenceScreenFitting sentenceScreenFitting = new SentenceScreenFitting();
        String[] sentence = { "i", "had", "apple", "pie" };
        int rows = 4;
        int cols = 5;
        System.out.println(sentenceScreenFitting.wordsTyping(sentence, rows, cols));
    }
}
