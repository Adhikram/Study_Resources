package Questions.BackTracking;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/*
https://leetcode.com/problems/word-break-ii/description/
 Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.

 */
public class WordBreakII {
    List<String> results;
    HashSet<String> dict;

    public List<String> wordBreakBackTrack(String s, List<String> wordDict) {
        results = new ArrayList<>();
        dict = new HashSet<String>();
        for (String word : wordDict)
            dict.add(word);
        backTrack(s, 0, new StringBuilder());
        return results;

    }

    public void backTrack(String s, int start, StringBuilder currentSentence) {
        if (start == s.length())
            results.add(currentSentence.toString().trim());
        for (int i = start; i < s.length(); i++) {
            if (dict.contains(s.substring(start, i + 1))) {
                int len = currentSentence.length();
                currentSentence.append(s.substring(start, i + 1));
                currentSentence.append(" ");
                backTrack(s, i + 1, currentSentence);
                currentSentence.setLength(len);
            }
        }
    }

    public List<String> wordBreakDP(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        Map<Integer, List<String>> dp = new HashMap<>();
        dp.put(0, Arrays.asList("")); // Initialize with an empty string to handle the base case.

        for (int i = 1; i <= s.length(); i++) {
            List<String> list = new ArrayList<>();
            for (int j = 0; j < i; j++) {
                String word = s.substring(j, i);
                if (wordSet.contains(word) && dp.containsKey(j)) {
                    for (String sentence : dp.get(j)) {
                        list.add(sentence.isEmpty() ? word : sentence + " " + word);
                    }
                }
            }
            if (!list.isEmpty()) {
                dp.put(i, list);
            }
        }
        return dp.getOrDefault(s.length(), new ArrayList<>());
    }

    // Time Complexity: O(n^2 * k) where n is the length of the string and k is the
    // average length of the words.
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        Map<String, List<String>> memo = new HashMap<>();
        return wordBreakHelper(s, wordSet, memo);
    }

    private List<String> wordBreakHelper(String s, Set<String> wordSet, Map<String, List<String>> memo) {
        if (memo.containsKey(s)) {
            return memo.get(s);
        }

        List<String> result = new ArrayList<>();

        if (wordSet.contains(s)) {
            result.add(s); // If the whole string is a word, add it as a possible sentence.
        }

        // Try breaking the string into two parts and solve for the second part
        // recursively.
        for (int i = 1; i < s.length(); i++) {
            String prefix = s.substring(0, i);
            if (wordSet.contains(prefix)) {
                String suffix = s.substring(i);
                List<String> suffixWays = wordBreakHelper(suffix, wordSet, memo);
                for (String way : suffixWays) {
                    result.add(prefix + " " + way);
                }
            }
        }

        memo.put(s, result);
        return result;
    }

    public static void main(String[] args) {
        WordBreakII wordBreakII = new WordBreakII();
        List<String> wordDict = new ArrayList<>(Arrays.asList("cat", "cats", "and", "sand", "dog"));
        System.out.println(wordBreakII.wordBreakDP("catsanddog", wordDict)); // Output: ["cats and dog","cat sand dog"]
        wordDict = new ArrayList<>(Arrays.asList("apple", "pen", "applepen", "pine", "pineapple"));
        System.out.println(wordBreakII.wordBreakDP("pineapplepenapple", wordDict)); // Output: ["pine apple pen
                                                                                    // apple","pineapple pen
                                                                                    // apple","pine applepen apple"]
        wordDict = new ArrayList<>(Arrays.asList("cats", "dog", "sand", "and", "cat"));
        System.out.println(wordBreakII.wordBreakDP("catsandog", wordDict)); // Output: []
    }
}
