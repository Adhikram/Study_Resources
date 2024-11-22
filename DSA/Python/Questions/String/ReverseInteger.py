"""
# Question: Reverse Integer
# Link: https://leetcode.com/problems/reverse-integer/

# Problem Statement:
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Constraints:
# -2^31 <= x <= 2^31 - 1
"""


class ReverseInteger:
    def reverse(self, x: int) -> int:
        """
        Reverse digits of a 32-bit signed integer.
        Time Complexity: O(log10(n)), where n is the input number
        Space Complexity: O(1)
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow before updating result
            if result > (INT_MAX - digit) // 10:
                return 0

            result = result * 10 + digit

        return sign * result


def main():
    test_cases = [
        {"input": 123, "expected": 321},
        {"input": -123, "expected": -321},
        {"input": 120, "expected": 21},
        {"input": 0, "expected": 0},
        {"input": 1534236469, "expected": 0},  # Overflow case
    ]

    solution = ReverseInteger()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Input: {test['input']}")
        result = solution.reverse(test["input"])
        print(f"Result: {result}")
        print(f"Expected: {test['expected']}")
        assert result == test["expected"], f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
