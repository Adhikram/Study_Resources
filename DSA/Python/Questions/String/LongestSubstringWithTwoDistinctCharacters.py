"""
# Question: Longest Substring with At Most Two Distinct Characters
# Link: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Use sliding window approach
# 2. Track character frequencies
# 3. Maintain distinct character count
# 4. Update maximum length

# Key Components:
# - length_of_longest_substring_two_distinct(): Main implementation
# - Character frequency tracking
# - Window size management
"""


class LongestSubstringWithTwoDistinctCharacters:
    def length_of_longest_substring_two_distinct(self, s: str) -> int:
        max_len = 0
        unique_count = 0
        freq = [0] * 256
        chars = list(s)
        start = 0

        for i in range(len(s)):
            # Increment frequency and unique count
            n = freq[ord(chars[i])]
            freq[ord(chars[i])] += 1
            if n == 0:
                unique_count += 1

            # Shrink window if more than 2 distinct characters
            while unique_count == 3:
                n = freq[ord(chars[start])] - 1
                freq[ord(chars[start])] -= 1
                if n == 0:
                    unique_count -= 1
                start += 1

            max_len = max(max_len, i - start + 1)

        return max_len


def main():
    solution = LongestSubstringWithTwoDistinctCharacters()
    s = "eceba"
    print(solution.length_of_longest_substring_two_distinct(s))  # Expected: 3


if __name__ == "__main__":
    main()
