"""
# Question: Make String Empty
# Link: https://leetcode.com/problems/make-string-empty/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Algorithm:
# 1. Track character frequencies
# 2. Track last indices of characters
# 3. Find maximum frequency
# 4. Build result string

# Key Components:
# - last_non_empty_string(): Main implementation
# - Character frequency tracking
# - Last index tracking
"""

from collections import defaultdict


class MakeStringEmpty:
    def last_non_empty_string(self, s: str) -> str:
        char_frequency = defaultdict(int)
        char_last_index = {}

        # Track frequencies and last indices
        for i, char in enumerate(s):
            char_last_index[char] = i
            char_frequency[char] += 1

        # Find maximum frequency
        max_frequency = max(char_frequency.values())

        # Build result string
        result = []
        for i, char in enumerate(s):
            if char_frequency[char] == max_frequency and char_last_index[char] == i:
                result.append(char)

        return "".join(result)


def main():
    solution = MakeStringEmpty()
    print(solution.last_non_empty_string("ababab"))
    print(solution.last_non_empty_string("abc"))
    print(solution.last_non_empty_string("abababab"))


if __name__ == "__main__":
    main()
