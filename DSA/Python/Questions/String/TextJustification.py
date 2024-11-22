"""
# Question: Text Justification
# Link: https://leetcode.com/problems/text-justification/

# Problem Statement:
# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters 
# and is fully (left and right) justified.

# Example:
# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output: [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
"""

from typing import List


class TextJustification:
    def justify_text_standard(self, words: List[str], max_width: int) -> List[str]:
        """
        Standard approach using line-by-line justification
        Time Complexity: O(n) where n is total characters in all words
        Space Complexity: O(n) for storing result
        """
        result = []
        current_line = []
        current_length = 0

        i = 0
        while i < len(words):
            # Check if word can be added to current line
            if current_length + len(words[i]) + len(current_line) <= max_width:
                current_line.append(words[i])
                current_length += len(words[i])
                i += 1
            else:
                # Justify current line
                result.append(
                    self.justify_line(current_line, current_length, max_width, False)
                )
                current_line = []
                current_length = 0

        # Handle last line (left-justified)
        if current_line:
            result.append(
                self.justify_line(current_line, current_length, max_width, True)
            )

        return result

    def justify_line(
        self, line: List[str], line_length: int, max_width: int, is_last_line: bool
    ) -> str:
        """Helper function to justify a single line"""
        if len(line) == 1 or is_last_line:
            return " ".join(line).ljust(max_width)

        total_spaces = max_width - line_length
        gaps = len(line) - 1
        spaces_per_gap = total_spaces // gaps
        extra_spaces = total_spaces % gaps

        result = []
        for i in range(len(line) - 1):
            result.append(line[i])
            spaces = spaces_per_gap + (1 if i < extra_spaces else 0)
            result.append(" " * spaces)
        result.append(line[-1])

        return "".join(result)

    def justify_text_optimized(self, words: List[str], max_width: int) -> List[str]:
        """
        Optimized approach with minimal string operations
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = []
        i = 0

        while i < len(words):
            # Calculate how many words fit on current line
            line_length = len(words[i])
            last_word = i

            while (
                last_word < len(words) - 1
                and line_length + len(words[last_word + 1]) + 1 <= max_width
            ):
                last_word += 1
                line_length += len(words[last_word]) + 1

            # Create the line with proper justification
            line = []
            word_count = last_word - i + 1

            if last_word == len(words) - 1 or word_count == 1:
                # Left justify last line or single word
                for j in range(i, last_word):
                    line.append(words[j])
                    line.append(" ")
                line.append(words[last_word])
                line.append(" " * (max_width - line_length))
            else:
                # Full justify middle lines
                spaces = max_width - (line_length - (word_count - 1))
                spaces_between = spaces // (word_count - 1)
                extra_spaces = spaces % (word_count - 1)

                for j in range(i, last_word):
                    line.append(words[j])
                    space_count = spaces_between + (1 if extra_spaces > 0 else 0)
                    line.append(" " * space_count)
                    extra_spaces -= 1
                line.append(words[last_word])

            result.append("".join(line))
            i = last_word + 1

        return result


def main():
    test_cases = [
        {
            "words": ["This", "is", "an", "example", "of", "text", "justification."],
            "max_width": 16,
            "expected": ["This    is    an", "example  of text", "justification.  "],
        },
        {
            "words": ["What", "must", "be", "acknowledgment", "shall", "be"],
            "max_width": 16,
            "expected": ["What   must   be", "acknowledgment  ", "shall be        "],
        },
    ]

    solution = TextJustification()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Words: {test['words']}")
        print(f"Max Width: {test['max_width']}")
        result_standard = solution.justify_text_standard(
            test["words"], test["max_width"]
        )
        result_optimized = solution.justify_text_optimized(
            test["words"], test["max_width"]
        )
        print("Standard Result:")
        for line in result_standard:
            print(f"'{line}'")
        print("Optimized Result:")
        for line in result_optimized:
            print(f"'{line}'")
        print("Expected:")
        for line in test["expected"]:
            print(f"'{line}'")
        assert (
            result_standard == result_optimized == test["expected"]
        ), f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
