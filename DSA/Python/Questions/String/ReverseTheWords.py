"""
# Question: Reverse Words in a String
# Link: https://leetcode.com/problems/reverse-words-in-a-string/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Algorithm:
# 1. Process string from right to left
# 2. Skip trailing spaces
# 3. Extract and reverse words
# 4. Handle multiple spaces

# Key Components:
# - reverse_words(): Main implementation
# - reverse_words_optimized(): In-place version
# - reverse(): Helper for character reversal
"""


class ReverseTheWords:
    def reverse_words(self, s: str) -> str:
        result = []
        end = len(s) - 1

        while end >= 0:
            # Skip trailing spaces
            while end >= 0 and s[end] == " ":
                end -= 1
            if end < 0:
                break

            # Find word boundaries
            start = end
            while start >= 0 and s[start] != " ":
                start -= 1

            # Add word to result
            if result:
                result.append(" ")
            result.append(s[start + 1 : end + 1])

            end = start - 1

        return "".join(result)

    def reverse_words_optimized(self, s: list[str]) -> None:
        # Reverse entire string
        self.reverse(s, 0, len(s) - 1)

        # Reverse each word
        start = 0
        for end in range(len(s)):
            if s[end] == " ":
                self.reverse(s, start, end - 1)
                start = end + 1
        # Reverse last word
        self.reverse(s, start, len(s) - 1)

    def reverse(self, s: list[str], left: int, right: int) -> None:
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


def main():
    solution = ReverseTheWords()
    print(solution.reverse_words("the sky is blue"))  # Expected: "blue is sky the"
    print(solution.reverse_words("  hello world  "))  # Expected: "world hello"


if __name__ == "__main__":
    main()
