"""
# Question: Longest String Chain
# Link: https://leetcode.com/problems/longest-string-chain/

# Problem Statement:
# Given a list of words, each word consists of English lowercase letters.
# A word1 is a predecessor of word2 if and only if we can add exactly one letter
# anywhere in word1 to make it equal to word2.
# Return the longest possible word chain length.

# Example:
# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chains is ["a","ba","bda","bdca"]
"""

from typing import List


def longest_string_chain(words: List[str]) -> int:
    """
    Find the length of longest possible word chain

    Time Complexity: O(NlogN + N*L^2) where N is number of words and L is average word length
    Space Complexity: O(N) for storing dp states
    """
    # Dictionary to store the longest chain ending at each word
    dp = {}

    # Sort words by length for processing shorter words first
    words.sort(key=len)

    # Track maximum chain length
    max_chain = 0

    # Process each word
    for word in words:
        # Initialize best chain length for current word
        best = 0

        # Try removing each character to find predecessor
        for i in range(len(word)):
            # Create predecessor by removing current character
            predecessor = word[:i] + word[i + 1 :]
            # Update best chain length if predecessor exists
            best = max(best, dp.get(predecessor, 0) + 1)

        # Store best chain length for current word
        dp[word] = best
        # Update overall maximum chain length
        max_chain = max(max_chain, best)

    return max_chain


def main():
    # Test cases
    test_cases = [
        ["a", "b", "ba", "bca", "bda", "bdca"],  # Regular case
        ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"],  # Multiple chains
        ["abcd", "dbqca"],  # No valid chain
        ["a", "ab", "abc", "abcd", "abcde"],  # Sequential chain
        ["a"],  # Single word
    ]

    for i, words in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {words}")
        print(f"Longest String Chain Length: {longest_string_chain(words)}")


if __name__ == "__main__":
    main()
