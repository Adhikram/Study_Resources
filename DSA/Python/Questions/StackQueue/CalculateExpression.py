"""
# Question: Evaluate Reverse Polish Notation
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Calculate result of expression in Reverse Polish Notation

# Time Complexity: O(n)
# Space Complexity: O(n)

# Algorithm:
# 1. Process tokens one by one
# 2. Push numbers onto stack
# 3. Evaluate operators with top two numbers
# 4. Return final result

# Key Components:
# - eval_rpn(): Main expression evaluator
# - resolve(): Helper for operator evaluation
# - Stack-based calculation
"""


class CalculateExpression:
    def resolve(self, a: int, b: int, operator: str) -> int:
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        else:
            return int(a / b)  # Integer division

    def eval_rpn(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if len(token) == 1 and not token[0].isdigit() and token[0] != "-":
                num2 = stack.pop()
                num1 = stack.pop()
                result = self.resolve(num1, num2, token)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack.pop()


def main():
    calculator = CalculateExpression()
    tokens = ["2", "1", "+", "3", "*"]
    result = calculator.eval_rpn(tokens)
    print(f"Result: {result}")  # Expected: 9


if __name__ == "__main__":
    main()
