"""
# Question: Implement pow(x, n)
# Link: https://leetcode.com/problems/powx-n/

# Calculate x raised to power n efficiently using recursion

# Time Complexity: O(log n) using divide and conquer
# Space Complexity: O(log n) due to recursive stack

# Algorithm:
# 1. Handle base cases (n = 0, x = 1, n = 1)
# 2. Handle special case for x = -1
# 3. Handle negative powers using reciprocal
# 4. Use divide and conquer for even/odd powers

# Key Components:
# - my_pow(): Main recursive function
# - Special case handling
# - Efficient power calculation
"""


class MyPow:
    def my_pow(self, x: float, n: int) -> float:
        # Base cases
        if n == 0 or x == 1:
            return 1
        if n == 1:
            return x

        # Special case for x = -1
        if x == -1:
            return 1 if n % 2 == 0 else -1

        # Handle negative powers
        if n < 0:
            return 1 / (x * self.my_pow(x, -(n + 1)))

        # Divide and conquer
        if n % 2 == 0:
            return self.my_pow(x * x, n // 2)

        return x * self.my_pow(x * x, n // 2)


def main():
    solution = MyPow()
    result = solution.my_pow(2.00000, -2)
    print(result)  # Expected output: 0.25000


if __name__ == "__main__":
    main()
