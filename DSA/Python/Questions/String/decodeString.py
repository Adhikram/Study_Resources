"""
# Question: Decode String
# Link: https://leetcode.com/problems/decode-string/

# Problem Statement:
# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
# is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# Example:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
"""


class StringDecoder:
    def decode_string(self, s: str) -> str:
        """
        Decode string using stack approach
        Time Complexity: O(n), where n is the length of the decoded string
        Space Complexity: O(m), where m is the length of the input string
        """
        stack = []
        current_string = ""
        current_number = 0

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == "[":
                stack.append((current_string, current_number))
                current_string = ""
                current_number = 0
            elif char == "]":
                prev_string, num = stack.pop()
                current_string = prev_string + num * current_string
            else:
                current_string += char

        return current_string

    def decode_string_recursive(self, s: str) -> str:
        """
        Recursive approach for string decoding
        Time Complexity: O(n)
        Space Complexity: O(n) for recursion stack
        """

        def decode(index: int) -> tuple:
            result = ""
            number = 0

            while index < len(s):
                char = s[index]
                if char.isdigit():
                    number = number * 10 + int(char)
                elif char == "[":
                    substring, next_index = decode(index + 1)
                    result += number * substring
                    number = 0
                    index = next_index
                elif char == "]":
                    return result, index
                else:
                    result += char
                index += 1

            return result, index

        return decode(0)[0]


def main():
    test_cases = [
        {"input": "3[a]2[bc]", "expected": "aaabcbc"},
        {"input": "2[abc]3[cd]ef", "expected": "abcabccdcdcdef"},
        {"input": "100[leetcode]", "expected": "leetcode" * 100},
        {"input": "3[a2[c]]", "expected": "accaccacc"},
    ]

    decoder = StringDecoder()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Input: {test['input']}")
        stack_result = decoder.decode_string(test["input"])
        recursive_result = decoder.decode_string_recursive(test["input"])
        print(f"Stack Result: {stack_result}")
        print(f"Recursive Result: {recursive_result}")
        print(f"Expected: {test['expected']}")
        assert (
            stack_result == recursive_result == test["expected"]
        ), f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
