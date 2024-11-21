"""
# Question: Longest Palindromic Subsequence
# Link: https://leetcode.com/problems/longest-palindromic-subsequence/

# Problem Statement:
# Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by 
# deleting some or no elements without changing the order of the remaining elements.

# Example:
# Input: s = "agbcba"
# Output: 5
# Explanation: The longest palindromic subsequence is "abcba"
"""


def lcs(s1: str, s2: str) -> int:
    """
    Helper function to find Longest Common Subsequence
    Uses dynamic programming with tabulation
    """
    n, m = len(s1), len(s2)
    # Create and initialize dp array
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


def longest_palindromic_subsequence(s: str) -> int:
    """
    Main function to find longest palindromic subsequence
    Uses LCS of string and its reverse

    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    # Create reversed string
    reversed_s = s[::-1]

    # LCS of string and its reverse gives longest palindromic subsequence
    return lcs(s, reversed_s)


def main():
    # Test cases
    test_cases = [
        "agbcba",  # Regular case
        "racecar",  # Perfect palindrome
        "aaa",  # Repeated characters
        "abc",  # No palindrome > 1
        "bbbb",  # All same characters
        "character",  # Multiple palindromic subsequences
    ]

    for i, s in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {s}")
        print(
            f"Length of Longest Palindromic Subsequence: {longest_palindromic_subsequence(s)}"
        )


if __name__ == "__main__":
    main()
