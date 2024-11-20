"""
# Question: Find Nth Root
# Find the nth root of a given number using binary search

# Time Complexity: O(log(m * 10^d)) where d is decimal precision
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search between 0 and m
# 2. Calculate mid^n and compare
# 3. Return nth root with precision
"""


class FindNthRoot:
    def nth_root(self, m: float, n: int) -> float:
        if m == 0:
            return 0

        left, right = 0, max(1, m)
        eps = 1e-7  # precision

        while right - left > eps:
            mid = (left + right) / 2
            if mid**n <= m:
                left = mid
            else:
                right = mid

        return left


def main():
    solution = FindNthRoot()
    print(solution.nth_root(27, 3))  # Expected: 3.0
    print(solution.nth_root(7, 3))  # Expected: ~1.913


if __name__ == "__main__":
    main()
