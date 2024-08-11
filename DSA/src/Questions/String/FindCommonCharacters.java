package Questions.String;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
https://leetcode.com/problems/find-common-characters/description/
 Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.

Explanation
Initialization:

We initialize an array minFreq of size 26 (for each letter in the alphabet) to store the minimum frequency of each character across all words. Initially, we fill it with Integer.MAX_VALUE to ensure any actual frequency will be smaller.
Frequency Calculation:

For each word in the words array, we calculate the frequency of each character and update the minFreq array by taking the minimum value between the current frequency and the existing value in minFreq.
Result Construction:

After processing all words, the minFreq array contains the minimum frequency of each character that is common across all words. We then create a result list by adding each character the number of times it appears (based on minFreq).
Complexity Analysis
Time Complexity: O(n×m),
 where n is the number of words and m is the average length of the words. Each word is processed to calculate the frequency of characters.

Space Complexity:O(1),
 since the minFreq array size is constant (26 for the lowercase English letters), and only a fixed amount of additional space is used.
 */
public class FindCommonCharacters {
    public List<String> commonChars(String[] words) {
        // Array to store the minimum frequency of each character
        int[] minFreq = new int[26];
        Arrays.fill(minFreq, Integer.MAX_VALUE); // Fill with maximum possible values

        // Calculate the frequency of characters in each word
        for (String word : words) {
            int[] freq = new int[26]; // Frequency of characters in the current word
            for (char c : word.toCharArray()) {
                freq[c - 'a']++;
            }
            // Update the minimum frequency for each character
            for (int i = 0; i < 26; i++) {
                minFreq[i] = Math.min(minFreq[i], freq[i]);
            }
        }

        // Construct the result list based on minimum frequencies
        List<String> result = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            while (minFreq[i] > 0) {
                result.add(String.valueOf((char) (i + 'a')));
                minFreq[i]--;
            }
        }

        return result;

    }
    public static void main(String[] args) {
        FindCommonCharacters findCommonCharacters = new FindCommonCharacters();
        String[] words = {"bella", "label", "roller"};
        System.out.println(findCommonCharacters.commonChars(words)); // Output: ["e","l","l"]
    }
}
