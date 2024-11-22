"""
# Question: Find Nth Root
# Problem Statement:
# Given two numbers N and M, find the Nth root of M.
# Return the answer with precision up to 6 decimal places.

# Example:
# Input: N = 3, M = 27
# Output: 3.000000
# Explanation: Cube root of 27 is 3
"""


class FindNthRoot:
    def nth_root_binary_search(
        self, n: int, m: float, precision: float = 1e-6
    ) -> float:
        """
        Binary search approach for finding nth root
        Time Complexity: O(log(M * 10^d)) where d is decimal precision
        Space Complexity: O(1)
        """
        if m == 0:
            return 0

        left, right = 0, max(1, m)

        while right - left > precision:
            mid = (left + right) / 2
            if mid**n <= m:
                left = mid
            else:
                right = mid

        return left

    def nth_root_newton(self, n: int, m: float, precision: float = 1e-6) -> float:
        """
        Newton's method for finding nth root
        Time Complexity: O(log(M) * log(1/precision))
        Space Complexity: O(1)
        """
        if m == 0:
            return 0

        x = m  # Initial guess
        while True:
            next_x = ((n - 1) * x + m / (x ** (n - 1))) / n
            if abs(next_x - x) < precision:
                return x
            x = next_x

    def nth_root_exponential(self, n: int, m: float, precision: float = 1e-6) -> float:
        """
        Exponential approach using logarithms
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if m == 0:
            return 0

        import math

        result = math.exp(math.log(m) / n)
        return result


def main():
    test_cases = [
        {"n": 3, "m": 27, "expected": 3.0},
        {"n": 2, "m": 16, "expected": 4.0},
        {"n": 4, "m": 81, "expected": 3.0},
        {"n": 3, "m": 1000, "expected": 10.0},
    ]

    solution = FindNthRoot()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"N: {test['n']}, M: {test['m']}")

        result_binary = solution.nth_root_binary_search(test["n"], test["m"])
        result_newton = solution.nth_root_newton(test["n"], test["m"])
        result_exp = solution.nth_root_exponential(test["n"], test["m"])

        print(f"Binary Search Result: {result_binary:.6f}")
        print(f"Newton Method Result: {result_newton:.6f}")
        print(f"Exponential Result: {result_exp:.6f}")
        print(f"Expected: {test['expected']:.6f}")

        assert abs(result_binary - test["expected"]) < 1e-6
        assert abs(result_newton - test["expected"]) < 1e-6
        assert abs(result_exp - test["expected"]) < 1e-6


if __name__ == "__main__":
    main()
