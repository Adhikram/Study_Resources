"""
# Question: Basic Calculator II
# Link: https://leetcode.com/problems/basic-calculator-ii/

# Evaluate mathematical expressions with basic operators

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Process each character in expression
# 2. Handle numbers and operators (+, -, *, /)
# 3. Perform immediate multiplication and division
# 4. Track last number for operations

# Key Components:
# - calculate(): Main expression evaluator
# - is_digit(): Helper for digit validation
# - Operation precedence handling
"""


class BasicCalculatorII:
    def is_digit(self, char: str) -> bool:
        return "0" <= char <= "9"

    def calculate(self, s: str) -> int:
        result = 0
        current_number = 0
        last_number = 0
        operation = "+"

        for i, char in enumerate(s):
            if self.is_digit(char):
                current_number = current_number * 10 + int(char)

            if (not self.is_digit(char) and char != " ") or i == len(s) - 1:
                if operation in "+-":
                    result += last_number
                    last_number = (
                        current_number if operation == "+" else -current_number
                    )
                elif operation == "*":
                    last_number = last_number * current_number
                elif operation == "/":
                    # Handle division considering sign
                    last_number = int(last_number / current_number)

                operation = char
                current_number = 0

        result += last_number
        return result


def main():
    calculator = BasicCalculatorII()
    print(calculator.calculate("3+2*2"))  # Output: 7
    print(calculator.calculate(" 3/2 "))  # Output: 1
    print(calculator.calculate(" 3+5 / 2 "))  # Output: 5


if __name__ == "__main__":
    main()
