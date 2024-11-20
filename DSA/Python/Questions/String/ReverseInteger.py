"""
# Question: Reverse Integer
# Link: https://leetcode.com/problems/reverse-integer/

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Algorithm:
# 1. Extract digits one by one
# 2. Build reversed number
# 3. Handle overflow cases
# 4. Return reversed result

# Key Components:
# - reverse(): Main implementation
# - Overflow checking
# - Integer bounds handling
"""


class ReverseInteger:
    def reverse(self, x: int) -> int:
        result = 0

        while x != 0:
            # Extract last digit
            digit = x % 10
            x //= 10

            # Check for overflow before updating result
            if result > 2**31 // 10 or (result == 2**31 // 10 and digit > 7):
                return 0
            if result < -(2**31) // 10 or (result == -(2**31) // 10 and digit < -8):
                return 0

            # Build reversed number
            result = result * 10 + digit

        return result


def main():
    solution = ReverseInteger()
    print(solution.reverse(123))  # Expected: 321
    print(solution.reverse(-123))  # Expected: -321
    print(solution.reverse(120))  # Expected: 21
    print(solution.reverse(1534236469))  # Expected: 0 (overflow)


if __name__ == "__main__":
    main()
