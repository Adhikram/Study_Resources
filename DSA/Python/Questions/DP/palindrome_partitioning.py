"""
# Question: Palindrome Partitioning
# Link: https://leetcode.com/problems/palindrome-partitioning-ii/

# Problem Statement:
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.

# Example:
# Input: s = "aabaa"
# Output: 0
# Explanation: String is already a palindrome, no cuts needed.
"""

from typing import List

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. Start from beginning of string
2. For each position, try all possible cuts
3. Check if substring is palindrome
4. If palindrome, recursively solve for remaining string
5. Return minimum cuts needed

Time Complexity: O(N*N) - each state computed once
Space Complexity: O(N) + O(N) for dp array and recursion
"""


def palindrome_partitioning_recursive(s: str) -> int:
    n = len(s)
    dp = [-1] * n

    def is_palindrome(i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def solve(i: int) -> int:
        # Base case: reached end of string
        if i == n:
            return 0

        if dp[i] != -1:
            return dp[i]

        min_cost = float("inf")
        # Try all possible cuts
        for j in range(i, n):
            if is_palindrome(i, j):
                cost = 1 + solve(j + 1)
                min_cost = min(min_cost, cost)

        dp[i] = min_cost
        return min_cost

    return solve(0) - 1


# 2. Tabulation Solution
"""
Algorithm:
1. Create dp array of size n+1
2. Process string from right to left
3. For each position, try all possible cuts
4. Store minimum cuts needed at each position
5. Return minimum cuts for entire string

Time Complexity: O(N*N)
Space Complexity: O(N)
"""


def palindrome_partitioning_tabulation(s: str) -> int:
    n = len(s)
    dp = [0] * (n + 1)

    def is_palindrome(i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    for i in range(n - 1, -1, -1):
        min_cost = float("inf")
        for j in range(i, n):
            if is_palindrome(i, j):
                cost = 1 + dp[j + 1]
                min_cost = min(min_cost, cost)
        dp[i] = min_cost

    return dp[0] - 1


def main():
    # Test cases
    test_cases = [
        "aabaa",  # Already palindrome
        "aab",  # Single cut needed
        "abcde",  # Multiple cuts needed
        "aaaa",  # All same characters
        "abcba",  # Palindrome with odd length
    ]

    for i, s in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {s}")
        print(f"Recursive Solution: {palindrome_partitioning_recursive(s)}")
        print(f"Tabulation Solution: {palindrome_partitioning_tabulation(s)}")


if __name__ == "__main__":
    main()
