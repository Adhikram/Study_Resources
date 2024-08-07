package Questions.String;
/* 
 You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
 */
public class MergeAlternatively {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder merged = new StringBuilder();
        int i = 0, j = 0;
        while (i < word1.length() && j < word2.length()) {
            merged.append(word1.charAt(i++));
            merged.append(word2.charAt(j++));
        }
        while (i < word1.length()) {
            merged.append(word1.charAt(i++));
        }
        while (j < word2.length()) {
            merged.append(word2.charAt(j++));
        }
        return merged.toString();
    }
    // Optimize the code by using StringBuilder instead of String
    // Time complexity: O(n)
    // Space complexity: O(n)

    public static void main(String[] args) {
        MergeAlternatively obj = new MergeAlternatively();
        String word1 = "abc";
        String word2 = "pqr";
        System.out.println(obj.mergeAlternately(word1, word2));
    }
}
