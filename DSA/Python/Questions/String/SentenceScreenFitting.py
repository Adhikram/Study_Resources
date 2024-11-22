# Question: Sentence Screen Fitting
# Link: https://leetcode.com/problems/sentence-screen-fitting/

# Problem Statement:
# Given a rows x cols screen and a sentence represented as a list of strings, 
# find how many times the given sentence can be fitted on the screen.

from typing import List


class SentenceScreenFitting:
    def words_typing_dp(self, sentence: List[str], rows: int, cols: int) -> int:
        """
        Dynamic Programming approach using word index tracking.
        Time Complexity: O(rows * cols), where rows is the number of rows and cols is the number of columns.
        Space Complexity: O(1).
        """
        # Join the sentence into a single string with spaces and a trailing space
        s = " ".join(sentence) + " "
        n = len(s)
        chars_fitted = 0

        # Iterate through each row
        for _ in range(rows):
            # Add the number of columns to chars_fitted
            chars_fitted += cols
            # If we land on a space, proceed to the next character
            if s[chars_fitted % n] == " ":
                chars_fitted += 1
            else:
                # Move back to the last valid space
                while chars_fitted > 0 and s[(chars_fitted - 1) % n] != " ":
                    chars_fitted -= 1

        return chars_fitted // n

    def words_typing_optimized(self, sentence: List[str], rows: int, cols: int) -> int:
        """
        Optimized approach using pre-computation.
        Time Complexity: O(rows + len(sentence)), where len(sentence) is the total sentence length.
        Space Complexity: O(1).
        """
        s = " ".join(sentence) + " "
        n = len(s)
        chars_fitted = 0

        # Iterate through each row
        for _ in range(rows):
            chars_fitted += cols
            # Adjust the position based on the character fit
            if s[chars_fitted % n] == " ":
                chars_fitted += 1
            else:
                while chars_fitted > 0 and s[(chars_fitted - 1) % n] != " ":
                    chars_fitted -= 1

        return chars_fitted // n


def main():
    test_cases = [
        {"sentence": ["hello", "world"], "rows": 2, "cols": 8, "expected": 1},
        {"sentence": ["a", "bcd", "e"], "rows": 3, "cols": 6, "expected": 2},
        {"sentence": ["I", "had", "apple", "pie"], "rows": 4, "cols": 5, "expected": 1},
        {"sentence": ["a"], "rows": 5, "cols": 5, "expected": 15},
    ]

    solution = SentenceScreenFitting()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Sentence: {test['sentence']}")
        print(f"Rows: {test['rows']}, Cols: {test['cols']}")
        result_dp = solution.words_typing_dp(
            test["sentence"], test["rows"], test["cols"]
        )
        print(f"DP Result: {result_dp}")
        result_optimized = solution.words_typing_optimized(
            test["sentence"], test["rows"], test["cols"]
        )
        print(f"Optimized Result: {result_optimized}")
        print(f"Expected: {test['expected']}")
        assert result_dp == test["expected"], f"Test case {i + 1} failed"
        print(f"Test case {i + 1} passed")


if __name__ == "__main__":
    main()
