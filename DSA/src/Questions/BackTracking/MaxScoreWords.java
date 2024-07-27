package Questions.BackTracking;

/*
https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/
 Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

 

Example 1:

Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.
Example 2:

Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explanation:
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.
Example 3:

Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
Output: 0
Explanation:
Letter "e" can only be used once.
 

Constraints:

1 <= words.length <= 14
1 <= words[i].length <= 15
1 <= letters.length <= 100
letters[i].length == 1
score.length == 26
0 <= score[i] <= 10
words[i], letters[i] contains only lower case English letters.
Time Complexity: O(2^N * M)
Space Complexity: O(N) due to the recursive call stack and a constant size for the letter count array.
 */
public class MaxScoreWords {
    public int maxScoreWords(String[] words, char[] letters, int[] score) {
        // Initialize a count array to keep track of the available letters
        int[] count = new int[26];

        // Count the occurrences of each letter in the letters array
        for (char ch : letters) {
            count[ch - 'a']++;
        }

        // Start backtracking to find the maximum score of valid words
        int res = backtrack(words, count, score, 0);
        return res; // Return the maximum score obtained
    }

    int backtrack(String[] words, int[] count, int[] score, int index) {
        int max = 0; // Variable to keep track of the maximum score at this stage

        // Iterate through each word starting from the given index
        for (int i = index; i < words.length; i++) {
            int res = 0; // Score for the current word
            boolean isValid = true; // Flag to check if the current word can be formed

            // Check if the current word can be formed with the available letters
            for (char ch : words[i].toCharArray()) {
                // Decrement the count for the current letter
                count[ch - 'a']--;
                // Add the score of the current letter to the total score
                res += score[ch - 'a'];

                // If the count for any letter becomes negative, the word cannot be formed
                if (count[ch - 'a'] < 0) {
                    isValid = false; // Mark the word as invalid
                }
            }

            // If the word is valid, proceed with recursion
            if (isValid) {
                // Add the score from the recursive call for the remaining words
                res += backtrack(words, count, score, i + 1);
                // Update the maximum score found so far
                max = Math.max(res, max);
            }

            // Backtrack: restore the count of letters after exploring the current word
            for (char ch : words[i].toCharArray()) {
                count[ch - 'a']++;
            }
        }
        return max; // Return the maximum score found for this path
    }
}
