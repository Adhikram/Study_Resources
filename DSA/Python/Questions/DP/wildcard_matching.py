"""
# Question: Wildcard Pattern Matching
# Link: https://leetcode.com/problems/wildcard-matching/

# Problem Statement:
# Given two strings 'str' and 'pattern', determine if 'str' matches with 'pattern'.
# The pattern can include two special characters:
# '?' - Matches any single character
# '*' - Matches any sequence of characters (including empty sequence)

# Example:
# Input: str = "x?y*z", pattern = "xaylmz"
# Output: True
# Explanation: x matches x, ? matches a, y matches y, * matches lm, z matches z
"""


def is_all_stars(pattern: str, i: int) -> bool:
    """Check if all characters from 0 to i are '*'"""
    for j in range(i + 1):
        if pattern[j] != "*":
            return False
    return True


# 1. Recursive Solution with Memoization
"""
Algorithm:
1. Compare characters from both strings
2. Handle special characters '?' and '*'
3. Use memoization to store intermediate results
4. Handle base cases for empty strings

Time Complexity: O(N*M)
Space Complexity: O(N*M) + O(N+M) for recursion stack
"""


def wildcard_matching_recursive(pattern: str, string: str) -> bool:
    n, m = len(pattern), len(string)
    dp = [[-1] * m for _ in range(n)]

    def solve(i: int, j: int) -> bool:
        # Base cases
        if i < 0 and j < 0:
            return True
        if i < 0:
            return False
        if j < 0:
            return is_all_stars(pattern, i)

        if dp[i][j] != -1:
            return dp[i][j] == 1

        if pattern[i] == string[j] or pattern[i] == "?":
            dp[i][j] = 1 if solve(i - 1, j - 1) else 0
            return dp[i][j] == 1

        if pattern[i] == "*":
            dp[i][j] = 1 if (solve(i - 1, j) or solve(i, j - 1)) else 0
            return dp[i][j] == 1

        dp[i][j] = 0
        return False

    return solve(n - 1, m - 1)


# 2. Tabulation Solution
"""
Algorithm:
1. Create dp table and initialize base cases
2. Process strings from left to right
3. Handle each character type separately
4. Fill dp table based on pattern matching rules

Time Complexity: O(N*M)
Space Complexity: O(N*M)
"""


def wildcard_matching_tabulation(pattern: str, string: str) -> bool:
    n, m = len(pattern), len(string)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Base cases
    dp[0][0] = True
    for i in range(1, n + 1):
        dp[i][0] = is_all_stars(pattern, i - 1)

    # Fill dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[i - 1] == string[j - 1] or pattern[i - 1] == "?":
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[i - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[n][m]


# 3. Space Optimized Solution
"""
Algorithm:
1. Use two arrays instead of full dp table
2. Alternate between current and previous row
3. Process pattern character by character
4. Optimize space usage to O(M)

Time Complexity: O(N*M)
Space Complexity: O(M)
"""


def wildcard_matching_optimized(pattern: str, string: str) -> bool:
    n, m = len(pattern), len(string)
    prev = [False] * (m + 1)
    prev[0] = True

    for i in range(1, n + 1):
        curr = [False] * (m + 1)
        curr[0] = is_all_stars(pattern, i - 1)

        for j in range(1, m + 1):
            if pattern[i - 1] == string[j - 1] or pattern[i - 1] == "?":
                curr[j] = prev[j - 1]
            elif pattern[i - 1] == "*":
                curr[j] = prev[j] or curr[j - 1]

        prev = curr[:]

    return prev[m]


def main():
    test_cases = [
        ("x?y*z", "xaylmz"),
        ("ab*cd", "abefcd"),
        ("a*", "aa"),
        ("*", "abc"),
        ("a", "a"),
    ]

    for i, (pattern, string) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Pattern: {pattern}")
        print(f"String: {string}")
        print(f"Recursive Solution: {wildcard_matching_recursive(pattern, string)}")
        print(f"Tabulation Solution: {wildcard_matching_tabulation(pattern, string)}")
        print(f"Optimized Solution: {wildcard_matching_optimized(pattern, string)}")


if __name__ == "__main__":
    main()
