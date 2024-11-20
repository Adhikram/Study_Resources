"""
# Question: Find the Closest Palindrome
# Link: https://leetcode.com/problems/find-the-closest-palindrome/

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Algorithm:
# 1. Generate candidate palindromes
# 2. Handle edge cases
# 3. Find closest palindrome
# 4. Return result as string

# Key Components:
# - nearest_palindromic(): Main implementation
# - get_palindrome(): Helper for palindrome generation
# - Candidate generation logic
"""


class NearestPalindromeNumber:
    def nearest_palindromic(self, n: str) -> str:
        length = len(n)
        i = length // 2 if length % 2 == 1 else length // 2 - 1
        left = int(n[: i + 1])

        # Generate candidates
        candidates = []

        # Current palindrome
        candidates.append(self.get_palindrome(left, length % 2 == 0))
        # Next palindrome
        candidates.append(self.get_palindrome(left + 1, length % 2 == 0))
        # Previous palindrome
        candidates.append(self.get_palindrome(left - 1, length % 2 == 0))
        # Edge cases
        candidates.append(10 ** (length - 1) - 1)
        candidates.append(10**length + 1)

        # Find closest palindrome
        num = int(n)
        diff = float("inf")
        result = 0

        for candidate in candidates:
            if candidate == num:
                continue
            if abs(candidate - num) < diff:
                diff = abs(candidate - num)
                result = candidate
            elif abs(candidate - num) == diff:
                result = min(result, candidate)

        return str(result)

    def get_palindrome(self, left: int, even: bool) -> int:
        res = left
        if not even:
            left //= 10
        while left > 0:
            res = res * 10 + left % 10
            left //= 10
        return res


def main():
    solution = NearestPalindromeNumber()
    print(solution.nearest_palindromic("123"))  # Expected: "121"
    print(solution.nearest_palindromic("1000"))  # Expected: "999"


if __name__ == "__main__":
    main()
