"""
# Question: Longest Common Substring
# Link: https://leetcode.com/problems/longest-common-substring/

# Problem Statement:
# Given two strings str1 and str2, find the length of their longest common substring.
# A substring is a contiguous sequence of characters within a string.

# Example:
# Input: str1 = "abcdxyz", str2 = "xyzabcd"
# Output: 4
# Explanation: The longest common substring is "abcd" or "xyza"

# Key Insights:
# - Substrings must be contiguous
# - Reset count when characters don't match
# - Track maximum length throughout
"""

# 1. Tabulation Solution
"""
Algorithm:
1. Create 2D dp array of size (n+1)*(m+1)
2. For each matching character:
   - Extend substring by adding 1 to diagonal value
   - Reset count to 0 if characters don't match
3. Track maximum length found so far

Time Complexity: O(n*m)
Space Complexity: O(n*m)
"""


def lcs_tabulation(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    # Create dp array for storing lengths
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # Variable to track maximum substring length
    max_length = 0

    # Fill dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # When characters match
            if s1[i - 1] == s2[j - 1]:
                # Extend current substring
                dp[i][j] = 1 + dp[i - 1][j - 1]
                # Update maximum length if needed
                max_length = max(max_length, dp[i][j])

    return max_length


# 2. Space Optimized Solution
"""
Algorithm:
1. Use two arrays instead of 2D array
2. Previous row and current row sufficient
3. Track maximum length while updating rows

Time Complexity: O(n*m)
Space Complexity: O(m)
"""


def lcs_optimized(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    # Initialize previous row
    prev = [0] * (m + 1)
    # Track maximum substring length
    max_length = 0

    # Process each character of first string
    for i in range(1, n + 1):
        # Current row for dynamic programming
        curr = [0] * (m + 1)

        # Fill current row
        for j in range(1, m + 1):
            # When characters match
            if s1[i - 1] == s2[j - 1]:
                # Extend current substring
                curr[j] = 1 + prev[j - 1]
                # Update maximum length if needed
                max_length = max(max_length, curr[j])

        # Update previous row for next iteration
        prev = curr[:]

    return max_length


def main():
    # Comprehensive test cases
    test_cases = [
        ("abcdxyz", "xyzabcd"),  # Multiple common substrings
        ("zxabcdezy", "yzabcdezx"),  # Overlapping substrings
        ("ABCD", "EFGH"),  # No common substring
        ("AAAA", "AAAA"),  # Same strings
        ("", "ABC"),  # Empty string
        ("XY", "XY"),  # Short strings
    ]

    # Test both implementations
    for i, (s1, s2) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: s1 = '{s1}', s2 = '{s2}'")
        print(f"Tabulation Solution: {lcs_tabulation(s1, s2)}")
        print(f"Optimized Solution: {lcs_optimized(s1, s2)}")


if __name__ == "__main__":
    main()
