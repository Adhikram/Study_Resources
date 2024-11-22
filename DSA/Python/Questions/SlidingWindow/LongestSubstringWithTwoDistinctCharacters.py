"""
# Question: Longest Substring with At Most Two Distinct Characters
# Link: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

# Problem Statement:
# Given a string s, find the length of the longest substring that contains at most two distinct characters.

# Example 1:
# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" with length 3.

# Example 2:
# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" with length 5.
"""

from typing import Dict
from collections import defaultdict


class LongestSubstringTwoDistinct:
    def length_of_longest_substring_sliding_window(self, s: str) -> int:
        """
        Find longest substring using sliding window technique
        Time Complexity: O(n)
        Space Complexity: O(1) since we store at most 3 characters
        """
        if not s:
            return 0

        char_count = defaultdict(int)
        max_length = 0
        window_start = 0

        for window_end, char in enumerate(s):
            char_count[char] += 1

            while len(char_count) > 2:
                left_char = s[window_start]
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
                window_start += 1

            current_length = window_end - window_start + 1
            max_length = max(max_length, current_length)

        return max_length

    def length_of_longest_substring_optimized(self, s: str) -> int:
        """
        Optimized solution using last occurrence tracking
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not s:
            return 0

        last_seen = {}
        max_length = 0
        window_start = 0

        for window_end, char in enumerate(s):
            if len(last_seen) == 2 and char not in last_seen:
                oldest_char = min(last_seen.items(), key=lambda x: x[1])[0]
                window_start = last_seen[oldest_char] + 1
                del last_seen[oldest_char]

            last_seen[char] = window_end
            current_length = window_end - window_start + 1
            max_length = max(max_length, current_length)

        return max_length


def main():
    test_cases = [
        {"input": "eceba", "expected": 3},
        {"input": "ccaabbb", "expected": 5},
        {"input": "a", "expected": 1},
        {"input": "", "expected": 0},
        {"input": "aabbaaccbbaa", "expected": 6},
    ]

    solution = LongestSubstringTwoDistinct()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Input: {test['input']}")
        sliding_window_result = solution.length_of_longest_substring_sliding_window(
            test["input"]
        )
        optimized_result = solution.length_of_longest_substring_optimized(test["input"])
        print(f"Sliding Window Result: {sliding_window_result}")
        print(f"Optimized Result: {optimized_result}")
        print(f"Expected: {test['expected']}")
        assert (
            sliding_window_result == optimized_result == test["expected"]
        ), f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
