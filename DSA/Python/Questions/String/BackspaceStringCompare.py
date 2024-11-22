"""
# Question: Backspace String Compare
# Link: https://leetcode.com/problems/backspace-string-compare/

# Problem Statement:
# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

# Example:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both strings become "ac" after processing backspaces.
"""

from typing import List, Tuple


class BackspaceStringCompare:
    def backspace_compare_stack(self, s: str, t: str) -> bool:
        """
        Compare strings using stack approach
        Time Complexity: O(n + m) where n and m are lengths of input strings
        Space Complexity: O(n + m) for storing processed strings
        """

        def process_string(string: str) -> List[str]:
            stack = []
            for char in string:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack

        return process_string(s) == process_string(t)

    def backspace_compare_two_pointer(self, s: str, t: str) -> bool:
        """
        Compare strings using two-pointer approach
        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """

        def get_next_valid_char(string: str, index: int) -> Tuple[str, int]:
            skip = 0
            while index >= 0:
                if string[index] == "#":
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    return string[index], index - 1
                index -= 1
            return "", index

        # Compare characters from right to left
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            char_s, i = get_next_valid_char(s, i) if i >= 0 else ("", -1)
            char_t, j = get_next_valid_char(t, j) if j >= 0 else ("", -1)

            if char_s != char_t:
                return False

        return True


def main():
    test_cases = [
        {"s": "ab#c", "t": "ad#c", "expected": True},
        {"s": "ab##", "t": "c#d#", "expected": True},
        {"s": "a#c", "t": "b", "expected": False},
        {"s": "####", "t": "", "expected": True},
    ]

    solution = BackspaceStringCompare()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"String 1: {test['s']}")
        print(f"String 2: {test['t']}")
        stack_result = solution.backspace_compare_stack(test["s"], test["t"])
        pointer_result = solution.backspace_compare_two_pointer(test["s"], test["t"])
        print(f"Stack Result: {stack_result}")
        print(f"Two-Pointer Result: {pointer_result}")
        print(f"Expected: {test['expected']}")
        assert (
            stack_result == pointer_result == test["expected"]
        ), f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
