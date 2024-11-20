"""
# Question: Letter Combinations of a Phone Number
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Generate all possible letter combinations from phone keypad digits

# Time Complexity: O(4^n) where n is length of input digits
# Space Complexity: O(n) for recursion stack

# Algorithm:
# 1. Map digits to letters using phone keypad
# 2. Recursively build combinations
# 3. Track current combination
# 4. Return all valid combinations

# Key Components:
# - letter_combinations(): Main combination generator
# - backtrack(): Recursive helper for building combinations
# - Phone keypad mapping
"""


class Keypad:
    def letter_combinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        output = []

        def backtrack(combination: str, next_digits: str):
            if not next_digits:
                output.append(combination)
            else:
                letters = phone_map[int(next_digits[0]) - 2]
                for letter in letters:
                    backtrack(combination + letter, next_digits[1:])

        backtrack("", digits)
        return output


def main():
    solution = Keypad()
    print(solution.letter_combinations("223"))
    # Expected output: ['aad', 'aae', 'aaf', 'abd', 'abe', 'abf', 'acd', 'ace', 'acf',
    #                  'bad', 'bae', 'baf', 'bbd', 'bbe', 'bbf', 'bcd', 'bce', 'bcf',
    #                  'cad', 'cae', 'caf', 'cbd', 'cbe', 'cbf', 'ccd', 'cce', 'ccf']


if __name__ == "__main__":
    main()
