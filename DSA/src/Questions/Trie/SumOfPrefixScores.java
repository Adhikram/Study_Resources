package Questions.Trie;

/*
https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/
You are given an array words of size n consisting of non-empty strings.

We define the score of a string word as the number of strings words[i] such that word is a prefix of words[i].

For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].

Note that a string is considered as a prefix of itself.

Example 1:

Input: words = ["abc","ab","bc","b"]
Output: [5,4,3,2]
Explanation: The answer for each string is the following:
- "abc" has 3 prefixes: "a", "ab", and "abc".
- There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
The total is answer[0] = 2 + 2 + 1 = 5.
- "ab" has 2 prefixes: "a" and "ab".
- There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
The total is answer[1] = 2 + 2 = 4.
- "bc" has 2 prefixes: "b" and "bc".
- There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
The total is answer[2] = 2 + 1 = 3.
- "b" has 1 prefix: "b".
- There are 2 strings with the prefix "b".
The total is answer[3] = 2.
Example 2:

Input: words = ["abcd"]
Output: [4]
Explanation:
"abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 = 4.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists of lowercase English letters.
Time complexity: O(n * m), where n is the number of words and m is the maximum length of a word.
Space complexity: O(n * m).
 */
public class SumOfPrefixScores {
    class TrieNode {
        public int freq = 0;
        TrieNode[] childs = null;

        public TrieNode() {
            childs = new TrieNode[26];
        }
    }

    public int[] sumPrefixScores(String[] words) {
        TrieNode root = new TrieNode();
        for (String w : words) {
            addInTrie(w, root);
        }
        int output[] = new int[words.length];
        for (int i = 0; i < words.length; i++) {
            int sum = 0;
            TrieNode node = root;
            for (char c : words[i].toCharArray()) {
                node = node.childs[c - 'a'];
                sum = sum + node.freq;
            }
            output[i] = sum;
        }
        return output;
    }

    private void addInTrie(String w, TrieNode root) {
        char[] arr = w.toCharArray();
        TrieNode node = root;
        for (char c : arr) {
            if (node.childs[c - 'a'] == null) {
                node.childs[c - 'a'] = new TrieNode();
            }
            node.childs[c - 'a'].freq++;
            node = node.childs[c - 'a'];
        }
    }

    public static void main(String[] args) {
        SumOfPrefixScores sumOfPrefixScores = new SumOfPrefixScores();
        String[] words = { "abc", "ab", "bc", "b" };
        int[] output = sumOfPrefixScores.sumPrefixScores(words);
        for (int i : output) {
            System.out.print(i + " ");
        }
    }

}
