"""
# Question: Longest Palindromic Substring
# Link: https://leetcode.com/problems/longest-palindromic-substring/

# Problem Statement:
# Given a string s, return the longest palindromic substring in s.
# A substring is a contiguous sequence of characters within a string.

# Example:
# Input: s = "babad"
# Output: "bab" or "aba"
"""


def longest_palindrome(s: str) -> str:
    """
    Find the longest palindromic substring using dynamic programming

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    n = len(s)
    start = 0
    length = 1

    # Initialize dp array for current row
    dp = [False] * n

    # Process each ending position
    for index in range(1, n):
        # Check all possible starting positions
        for i in range(index):
            # For substrings of length 2 or less
            if index - i <= 2:
                dp[i] = s[i] == s[index]
            else:
                # For longer substrings, check if ends match and middle is palindrome
                dp[i] = (s[i] == s[index]) and dp[i + 1]

            # Update longest palindrome if current is longer
            if dp[i] and index - i + 1 > length:
                start = i
                length = index - i + 1

    return s[start : start + length]


def main():
    # Test cases
    test_cases = [
        "babad",  # Multiple palindromes of same length
        "cbbdadbb",  # Palindrome with even length
        "racecar",  # Perfect palindrome
        "aaa",  # Repeated characters
        "abc",  # No palindrome > 1
        "bbbb",  # All same characters
        "character",  # Single character palindromes
    ]

    for i, s in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {s}")
        print(f"Longest Palindromic Substring: {longest_palindrome(s)}")


if __name__ == "__main__":
    main()
