"""
# Question: Basic Calculator
# Link: https://leetcode.com/problems/basic-calculator/

# Evaluate mathematical expressions with parentheses

# Time Complexity: O(n)
# Space Complexity: O(n)

# Algorithm:
# 1. Process each character in expression
# 2. Handle numbers, operators, and parentheses
# 3. Use stack for nested expressions
# 4. Return final evaluation result

# Key Components:
# - calculate(): Main expression evaluator
# - Stack for tracking nested calculations
# - Sign handling for negative numbers
"""


class BasicCalculator:
    def is_digit(self, char: str) -> bool:
        return "0" <= char <= "9"

    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        sign = 1
        i = 0

        while i < len(s):
            char = s[i]

            if self.is_digit(char):
                num = 0
                while i < len(s) and self.is_digit(s[i]):
                    num = num * 10 + int(s[i])
                    i += 1
                result += sign * num
                i -= 1
            elif char == "+":
                sign = 1
            elif char == "-":
                sign = -1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                result = stack.pop() * result + stack.pop()
            i += 1

        return result

    def calculate_recursive(self, s: str) -> int:
        self.i = 0
        return self.calc(s)

    def calc(self, s: str) -> int:
        num = 0
        ans = 0
        sign = 1

        while self.i < len(s):
            char = s[self.i]
            self.i += 1

            if self.is_digit(char):
                num = num * 10 + int(char)
            elif char == "(":
                num = self.calc(s)
            elif char == ")":
                return ans + num * sign
            elif char in "+-":
                ans += num * sign
                num = 0
                sign = 1 if char == "+" else -1

        ans += num * sign
        return ans


def main():
    calculator = BasicCalculator()
    print(calculator.calculate("1 + 1"))  # Output: 2
    print(calculator.calculate(" 2-1 + 2 "))  # Output: 3
    print(calculator.calculate("(1+(4+5+2)-3)+(6+8)"))  # Output: 23


if __name__ == "__main__":
    main()
