"""
# Question: Basic Calculator III
# Link: https://leetcode.com/problems/basic-calculator-iii/

# Evaluate complex mathematical expressions with parentheses and operators

# Time Complexity: O(n)
# Space Complexity: O(n)

# Algorithm:
# 1. Process each character in expression
# 2. Handle numbers, operators (+, -, *, /), and parentheses
# 3. Use stack for operation tracking
# 4. Handle nested expressions recursively

# Key Components:
# - calculate(): Main expression evaluator
# - is_digit(): Helper for digit validation
# - Stack-based operation processing
"""


class BasicCalculatorIII:
    def is_digit(self, char: str) -> bool:
        return "0" <= char <= "9"

    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        operation = "+"

        i = 0
        while i < len(s):
            char = s[i]

            if self.is_digit(char):
                current_number = current_number * 10 + int(char)

            if char == "(":
                # Find matching closing parenthesis
                count = 1
                j = i + 1
                while count != 0:
                    if s[j] == "(":
                        count += 1
                    if s[j] == ")":
                        count -= 1
                    j += 1
                current_number = self.calculate(s[i + 1 : j - 1])
                i = j - 1

            if (not self.is_digit(char) and char != " ") or i == len(s) - 1:
                if operation == "+":
                    stack.append(current_number)
                elif operation == "-":
                    stack.append(-current_number)
                elif operation == "*":
                    stack.append(stack.pop() * current_number)
                elif operation == "/":
                    stack.append(int(stack.pop() / current_number))

                operation = char
                current_number = 0

            i += 1

        return sum(stack)


def main():
    calculator = BasicCalculatorIII()
    print(calculator.calculate("1+1"))  # Output: 2
    print(calculator.calculate("6-4/2"))  # Output: 4
    print(calculator.calculate("2*(5+5*2)/3+(6/2+8)"))  # Output: 21


if __name__ == "__main__":
    main()
