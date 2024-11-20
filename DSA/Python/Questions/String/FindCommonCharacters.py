"""
# Question: Find Common Characters
# Link: https://leetcode.com/problems/find-common-characters/

# Find characters that appear in all strings

# Time Complexity: O(n * m)
# Space Complexity: O(1)

# Algorithm:
# 1. Track minimum frequency of each character
# 2. Process each word character by character
# 3. Update minimum frequencies
# 4. Build result from frequencies

# Key Components:
# - common_chars(): Main implementation
# - Character frequency tracking
# - Result list construction
"""

from typing import List


class FindCommonCharacters:
    def common_chars(self, words: List[str]) -> List[str]:
        # Initialize minimum frequency array
        min_freq = [float("inf")] * 26

        # Calculate minimum frequencies
        for word in words:
            # Current word frequency
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord("a")] += 1

            # Update minimum frequencies
            for i in range(26):
                min_freq[i] = min(min_freq[i], freq[i])

        # Build result list
        result = []
        for i in range(26):
            while min_freq[i] > 0:
                result.append(chr(i + ord("a")))
                min_freq[i] -= 1

        return result


def main():
    solution = FindCommonCharacters()
    words = ["bella", "label", "roller"]
    print(solution.common_chars(words))  # Expected: ["e","l","l"]


if __name__ == "__main__":
    main()
