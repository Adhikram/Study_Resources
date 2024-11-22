"""
# Question: Floor Square Root
# Problem Statement:
# Find the floor of square root of a given non-negative integer using different approaches.

# Example:
# Input: x = 8
# Output: 2
# Explanation: Square root of 8 is 2.828, floor value is 2
"""


class FloorSqrt:
    def floor_sqrt_binary(self, x: int) -> int:
        """
        Binary search approach
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if x == 0:
            return 0

        left, right = 1, x
        result = 0

        while left <= right:
            mid = (left + right) >> 1
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result

    def floor_sqrt_newton(self, x: int) -> int:
        """
        Newton's method approach
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if x == 0:
            return 0

        r = x
        while r * r > x:
            r = (r + x // r) >> 1

        return r

    def floor_sqrt_linear(self, x: int) -> int:
        """
        Linear search approach
        Time Complexity: O(√n)
        Space Complexity: O(1)
        """
        if x == 0:
            return 0

        i = 1
        while i * i <= x:
            i += 1

        return i - 1


def main():
    test_cases = [
        {"x": 8, "expected": 2},
        {"x": 16, "expected": 4},
        {"x": 0, "expected": 0},
        {"x": 1, "expected": 1},
        {"x": 100, "expected": 10},
    ]

    solution = FloorSqrt()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Input: {test['x']}")

        result_binary = solution.floor_sqrt_binary(test["x"])
        result_newton = solution.floor_sqrt_newton(test["x"])
        result_linear = solution.floor_sqrt_linear(test["x"])

        print(f"Binary Search Result: {result_binary}")
        print(f"Newton Method Result: {result_newton}")
        print(f"Linear Search Result: {result_linear}")
        print(f"Expected: {test['expected']}")

        assert result_binary == result_newton == result_linear == test["expected"]


if __name__ == "__main__":
    main()
