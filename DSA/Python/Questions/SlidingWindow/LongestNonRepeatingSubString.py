"""
# Question: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Problem Statement:
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The longest substring is "abc", with length 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The longest substring is "b", with length 1.
"""


class LongestNonRepeatingSubString:
    def length_of_longest_substring_sliding_window(self, s: str) -> int:
        """
        Find longest substring using sliding window technique
        Time Complexity: O(n)
        Space Complexity: O(min(m,n)) where m is size of character set
        """
        char_map = {}
        max_length = 0
        window_start = 0

        for window_end, char in enumerate(s):
            # If character is already in window, update window start
            if char in char_map and char_map[char] >= window_start:
                window_start = char_map[char] + 1

            # Update character position and max length
            char_map[char] = window_end
            current_length = window_end - window_start + 1
            max_length = max(max_length, current_length)

        return max_length

    def length_of_longest_substring_set(self, s: str) -> int:
        """
        Find longest substring using set approach
        Time Complexity: O(n)
        Space Complexity: O(min(m,n))
        """
        char_set = set()
        max_length = 0
        left = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


def main():
    test_cases = [
        {"input": "abcabcbb", "expected": 3},
        {"input": "bbbbb", "expected": 1},
        {"input": "pwwkew", "expected": 3},
        {"input": "", "expected": 0},
        {"input": "aab", "expected": 2},
    ]

    solution = LongestNonRepeatingSubString()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Input: {test['input']}")
        sliding_window_result = solution.length_of_longest_substring_sliding_window(
            test["input"]
        )
        set_result = solution.length_of_longest_substring_set(test["input"])
        print(f"Sliding Window Result: {sliding_window_result}")
        print(f"Set Approach Result: {set_result}")
        print(f"Expected: {test['expected']}")
        assert (
            sliding_window_result == set_result == test["expected"]
        ), f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
