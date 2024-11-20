"""
# Question: Additive Number
# Link: https://leetcode.com/problems/additive-number/

# Check if string can form additive sequence

# Time Complexity: O(n^3)
# Space Complexity: O(1)

# Algorithm:
# 1. Generate first two numbers
# 2. Recursively validate sequence
# 3. Handle leading zeros
# 4. Check if sequence is valid

# Key Components:
# - is_additive_number(): Main validation implementation
# - solve(): Recursive helper for sequence validation
# - Number generation and validation logic
"""


class AdditiveNumbers:
    def is_additive_number(self, num: str) -> bool:
        number1 = 0
        for i in range(len(num) - 1):
            number1 = number1 * 10 + int(num[i])
            number2 = 0
            for j in range(i + 1, len(num)):
                number2 = number2 * 10 + int(num[j])
                if self.solve(number1, number2, j + 1, num, 2):
                    return True
                if number2 == 0:
                    break
            if number1 == 0:
                break
        return False

    def solve(self, number1: int, number2: int, cur: int, num: str, count: int) -> bool:
        if cur >= len(num):
            return count >= 3

        if num[cur] == "0" and number1 + number2 != 0:
            return False

        number = 0
        target = number1 + number2

        for i in range(cur, len(num)):
            number = number * 10 + int(num[i])
            if number == target and self.solve(number2, target, i + 1, num, count + 1):
                return True
            elif number > target:
                break

        return False


def main():
    solution = AdditiveNumbers()
    print(solution.is_additive_number("112358"))  # True
    print(solution.is_additive_number("199100199"))  # True


if __name__ == "__main__":
    main()
