"""
# Question: Reverse Words in a String
# Link: https://leetcode.com/problems/reverse-words-in-a-string/

# Problem Statement:
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"

# Constraints:
# - 1 <= s.length <= 10^4
# - s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# - There is at least one word in s.
"""


class ReverseTheWords:
    def reverse_words_builtin(self, s: str) -> str:
        """
        Reverse the words using built-in functions.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Split the string by spaces and filter out empty strings
        words = s.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join the reversed list into a single string with spaces
        return " ".join(reversed_words)

    def reverse_words_manual(self, s: str) -> str:
        """
        Reverse the words manually without using built-in reverse.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        words = []
        length = len(s)
        i = 0

        while i < length:
            if s[i] != " ":
                start = i
                while i < length and s[i] != " ":
                    i += 1
                words.append(s[start:i])
            i += 1

        # Manually reverse the words list
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words)

    def reverse_words_two_pointer(self, s: str) -> str:
        """
        Reverse the words using two-pointer technique.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        words = s.split()
        left, right = 0, len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words)


def main():
    test_cases = [
        {"input": "the sky is blue", "expected": "blue is sky the"},
        {"input": "  hello world  ", "expected": "world hello"},
        {"input": "a good   example", "expected": "example good a"},
        {"input": "  Bob    Loves  Alice   ", "expected": "Alice Loves Bob"},
    ]

    solution = ReverseTheWords()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Input: '{test['input']}'")
        result_builtin = solution.reverse_words_builtin(test["input"])
        result_manual = solution.reverse_words_manual(test["input"])
        result_two_pointer = solution.reverse_words_two_pointer(test["input"])
        print(f"Builtin Result: '{result_builtin}'")
        print(f"Manual Result: '{result_manual}'")
        print(f"Two-Pointer Result: '{result_two_pointer}'")
        print(f"Expected: '{test['expected']}'")
        assert (
            result_builtin == result_manual == result_two_pointer == test["expected"]
        ), f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
