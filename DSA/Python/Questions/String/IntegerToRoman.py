"""
# Question: Integer to Roman
# Link: https://leetcode.com/problems/integer-to-roman/

# Time Complexity: O(1)
# Space Complexity: O(1)

# Algorithm:
# 1. Define Roman numeral symbols and values
# 2. Process number from largest to smallest value
# 3. Build Roman numeral string
# 4. Handle special cases (4, 9, 40, 90, 400, 900)

# Key Components:
# - int_to_roman(): Main implementation
# - Symbol-value mapping
# - String building
"""


class IntegerToRoman:
    def int_to_roman(self, num: int) -> str:
        # Define symbols and their corresponding values
        symbols = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        roman = []

        # Convert integer to Roman numeral
        for i in range(len(values)):
            while num >= values[i]:
                roman.append(symbols[i])
                num -= values[i]

        return "".join(roman)


def main():
    solution = IntegerToRoman()
    num = 3749
    print(solution.int_to_roman(num))  # Expected: "MMMDCCXLIX"


if __name__ == "__main__":
    main()
