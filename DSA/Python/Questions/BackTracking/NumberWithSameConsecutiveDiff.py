"""
# Question: Numbers With Same Consecutive Differences
# Link: https://leetcode.com/problems/numbers-with-same-consecutive-differences/

# Find all numbers of length n where consecutive digits differ by k

# Time Complexity: O(2^n)
# Space Complexity: O(2^n)

# Algorithm:
# 1. Start with single digits (1-9)
# 2. Build numbers recursively
# 3. Check consecutive digit differences
# 4. Return all valid numbers

# Key Components:
# - nums_same_consec_diff(): Main implementation
# - backtrack(): Recursive helper for number building
# - Difference validation logic
"""


class NumberWithSameConsecutiveDiff:
    def backtrack(self, val: int, length: int, k: int, result: list) -> None:
        if length == 0:
            result.append(val)
            return

        last_digit = val % 10
        if k + last_digit < 10:
            self.backtrack((val * 10) + (k + last_digit), length - 1, k, result)
        if last_digit - k > -1 and k != 0:
            self.backtrack((val * 10) + (last_digit - k), length - 1, k, result)

    def nums_same_consec_diff(self, n: int, k: int) -> list[int]:
        result = []

        for i in range(1, 10):
            self.backtrack(i, n - 1, k, result)

        return result


def main():
    solution = NumberWithSameConsecutiveDiff()
    print(solution.nums_same_consec_diff(3, 7))  # Expected: [181, 292, 707, 818, 929]


if __name__ == "__main__":
    main()
