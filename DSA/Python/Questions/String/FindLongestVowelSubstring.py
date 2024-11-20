"""
# Question: Find Longest Substring Containing Vowels in Even Counts
# Link: https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Use bit masking for vowel count tracking
# 2. Track first occurrence of each mask
# 3. Update maximum length when same mask found
# 4. Return longest valid substring length

# Key Components:
# - find_the_longest_substring(): Main implementation
# - Bit mask for vowel tracking
# - First occurrence array
"""

class FindLongestVowelSubstring:
    def __init__(self):
        # Initialize vowel mask mapping
        self.VOWEL_MASK = [0] * 128
        self.VOWEL_MASK[ord('a')] = 1
        self.VOWEL_MASK[ord('e')] = 2
        self.VOWEL_MASK[ord('i')] = 4
        self.VOWEL_MASK[ord('o')] = 8
        self.VOWEL_MASK[ord('u')] = 16

    def find_the_longest_substring(self, s: str) -> int:
        first_occurrence = [-1] * 32
        first_occurrence[0] = 0
        max_length = 0
        mask = 0

        for i in range(len(s)):
            if s[i] in 'aeiou':
                mask ^= self.VOWEL_MASK[ord(s[i])]

            if first_occurrence[mask] != -1:
                max_length = max(max_length, i + 1 - first_occurrence[mask])
            else:
                first_occurrence[mask] = i + 1

        return max_length

def main():
    solution = FindLongestVowelSubstring()
    s = "eleetminicoworoep"
    print(solution.find_the_longest_substring(s))  # Expected: 13

if __name__ == "__main__":
    main()
