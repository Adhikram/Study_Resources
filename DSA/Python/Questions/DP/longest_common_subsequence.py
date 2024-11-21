"""
# Question: Longest Common Subsequence
# Link: https://leetcode.com/problems/longest-common-subsequence/

# Problem Statement:
# Given two strings text1 and text2, return the length of their longest common subsequence.
# A subsequence is a sequence that can be derived from another sequence by deleting some or
# no elements without changing the order of the remaining elements.

# Example:
# Input: text1 = "AGGTAB", text2 = "GXTXAYB"
# Output: 4
# Explanation: The longest common subsequence is "GTAB"
"""

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. Compare characters from both strings:
   - If match, include character and move both pointers
   - If not match, try excluding character from either string
2. Use memoization to store results of subproblems

Time Complexity: O(n*m)
Space Complexity: O(n*m) + O(n+m) recursion stack
"""


def lcs_recursive(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    # Initialize dp array for memoization
    dp = [[-1] * m for _ in range(n)]

    def solve(i: int, j: int) -> int:
        # Base case: if either string is exhausted
        if i < 0 or j < 0:
            return 0

        # Return memoized result if available
        if dp[i][j] != -1:
            return dp[i][j]

        # If characters match
        if s1[i] == s2[j]:
            dp[i][j] = 1 + solve(i - 1, j - 1)
        else:
            # Try excluding character from either string
            dp[i][j] = max(solve(i - 1, j), solve(i, j - 1))

        return dp[i][j]

    return solve(n - 1, m - 1)


# 2. Tabulation Solution
"""
Algorithm:
1. Create 2D dp array of size (n+1)*(m+1)
2. Fill dp table bottom-up:
   - If characters match, add 1 to diagonal value
   - If not match, take max of left and top values

Time Complexity: O(n*m)
Space Complexity: O(n*m)
"""


def lcs_tabulation(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    # Create dp array with base cases
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


# 3. Space Optimized Solution
"""
Algorithm:
1. Use two arrays instead of 2D array
2. Previous row and current row sufficient
3. Update arrays in alternating fashion

Time Complexity: O(n*m)
Space Complexity: O(m)
"""


def lcs_optimized(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    # Initialize previous row
    prev = [0] * (m + 1)

    # Process each character of s1
    for i in range(1, n + 1):
        # Current row array
        curr = [0] * (m + 1)

        # Fill current row
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])

        # Update previous row
        prev = curr[:]

    return prev[m]


def main():
    # Test cases
    test_cases = [
        ("AGGTAB", "GXTXAYB"),  # Regular case
        ("ABCDGH", "AEDFHR"),  # Multiple common subsequences
        ("ABC", "DEF"),  # No common subsequence
        ("AAA", "AAA"),  # Same strings
        ("", "ABC"),  # Empty string
    ]

    for i, (s1, s2) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: s1 = '{s1}', s2 = '{s2}'")
        print(f"Recursive Solution: {lcs_recursive(s1, s2)}")
        print(f"Tabulation Solution: {lcs_tabulation(s1, s2)}")
        print(f"Optimized Solution: {lcs_optimized(s1, s2)}")


if __name__ == "__main__":
    main()
