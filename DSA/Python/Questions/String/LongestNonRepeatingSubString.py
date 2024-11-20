"""
# Question: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Time Complexity: O(n)
# Space Complexity: O(min(m,n)) where m is size of charset

# Algorithm:
# 1. Use sliding window approach
# 2. Track character positions in hashmap
# 3. Update window start based on repeating characters
# 4. Track maximum length

# Key Components:
# - length_of_longest_substring(): Main implementation
# - Character position tracking
# - Window size calculation
"""


class LongestNonRepeatingSubString:
    def length_of_longest_substring(self, s: str) -> int:
        char_map = {}
        result = 0
        start = -1

        for i, char in enumerate(s):
            if char in char_map:
                start = max(start, char_map[char])
            char_map[char] = i
            result = max(result, i - start)

        return result


def main():
    solution = LongestNonRepeatingSubString()
    print(solution.length_of_longest_substring("abcabcdb"))  # Expected: 4
    print(solution.length_of_longest_substring("b"))  # Expected: 1
    print(solution.length_of_longest_substring("pwwkew"))  # Expected: 3
    print(solution.length_of_longest_substring("aaaaaa"))  # Expected: 1


if __name__ == "__main__":
    main()
