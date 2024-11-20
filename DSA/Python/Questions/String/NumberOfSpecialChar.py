"""
# Question: Number of Special Characters
# Count special characters in string based on case matching

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Track character occurrences
# 2. Count matching upper/lowercase pairs
# 3. Handle character position constraints
# 4. Return special character count

# Key Components:
# - number_of_special_chars(): First implementation
# - number_of_special_chars2(): Alternative implementation
"""


class NumberOfSpecialChar:
    def number_of_special_chars(self, word: str) -> int:
        dist = ord("A") - ord("a")
        result = 0
        char_map = {}

        # Track character occurrences
        for ch in word:
            char_map[ord(ch) - ord("a")] = True

        # Count matching pairs
        for i in range(26):
            if i in char_map and (i + dist) in char_map:
                result += 1

        return result

    def number_of_special_chars2(self, word: str) -> int:
        dist = ord("a") - ord("A")
        result = 0
        char_map = {}

        # Track character positions
        for i, ch in enumerate(word):
            if ord(ch) - ord("A") in char_map and ord("A") <= ord(ch) <= ord("Z"):
                continue
            char_map[ord(ch) - ord("A")] = i

        # Count valid pairs
        for i in range(26):
            if (
                i in char_map
                and (i + dist) in char_map
                and char_map[i] > char_map[i + dist]
            ):
                result += 1

        return result


def main():
    solution = NumberOfSpecialChar()
    word = "abAc"
    print(solution.number_of_special_chars(word))
    print(solution.number_of_special_chars2(word))


if __name__ == "__main__":
    main()
