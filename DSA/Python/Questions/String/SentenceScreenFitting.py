"""
# Question: Sentence Screen Fitting
# Link: https://leetcode.com/problems/sentence-screen-fitting/

# Calculate how many times a sentence fits on screen

# Time Complexity: O(rows * cols)
# Space Complexity: O(n)

# Algorithm:
# 1. Join sentence with spaces
# 2. Track start position
# 3. Handle word wrapping
# 4. Calculate total fits

# Key Components:
# - words_typing(): Main implementation
# - String concatenation optimization
# - Position tracking
"""


class SentenceScreenFitting:
    def words_typing(self, sentence: list[str], rows: int, cols: int) -> int:
        # Join sentence with spaces and add trailing space
        s = " ".join(sentence) + " "
        s_len = len(s)
        start = 0

        # Process each row
        for i in range(rows):
            start += cols

            # If we land on a space, move to next character
            if s[start % s_len] == " ":
                start += 1
            else:
                # Backtrack to previous space
                while start > 0 and s[(start - 1) % s_len] != " ":
                    start -= 1

        return start // s_len


def main():
    solution = SentenceScreenFitting()
    sentence = ["i", "had", "apple", "pie"]
    rows = 4
    cols = 5
    print(solution.words_typing(sentence, rows, cols))  # Expected: 1


if __name__ == "__main__":
    main()
