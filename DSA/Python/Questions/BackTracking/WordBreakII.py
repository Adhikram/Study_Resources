"""
# Question: Word Break II
# Link: https://leetcode.com/problems/word-break-ii/

# Find all possible word combinations from dictionary

# Time Complexity: O(2^n) for backtracking
# Space Complexity: O(2^n) for storing results

# Algorithm:
# 1. Use backtracking to find all combinations
# 2. Use DP for memoization optimization
# 3. Track current sentence building
# 4. Return all valid sentences

# Key Components:
# - word_break(): Main implementation with multiple approaches
# - backtrack(): Helper for recursive solution
# - dp_solution(): Dynamic programming approach
"""

from typing import List
from collections import defaultdict


class WordBreakII:
    def word_break_backtrack(self, s: str, word_dict: List[str]) -> List[str]:
        results = []
        word_set = set(word_dict)

        def backtrack(start: int, current_sentence: str):
            if start == len(s):
                results.append(current_sentence.strip())
                return

            for i in range(start, len(s)):
                word = s[start : i + 1]
                if word in word_set:
                    backtrack(i + 1, current_sentence + word + " ")

        backtrack(0, "")
        return results

    def word_break_dp(self, s: str, word_dict: List[str]) -> List[str]:
        word_set = set(word_dict)
        dp = defaultdict(list)
        dp[0] = [""]

        for i in range(1, len(s) + 1):
            sentences = []
            for j in range(i):
                word = s[j:i]
                if word in word_set and j in dp:
                    for sentence in dp[j]:
                        sentences.append((sentence + " " + word).strip())
            dp[i] = sentences

        return dp[len(s)]

    def word_break(self, s: str, word_dict: List[str]) -> List[str]:
        word_set = set(word_dict)
        memo = {}

        def helper(s: str) -> List[str]:
            if s in memo:
                return memo[s]

            result = []
            if s in word_set:
                result.append(s)

            for i in range(1, len(s)):
                prefix = s[:i]
                if prefix in word_set:
                    suffix_ways = helper(s[i:])
                    for way in suffix_ways:
                        result.append(prefix + " " + way)

            memo[s] = result
            return result

        return helper(s)


def main():
    solution = WordBreakII()
    s = "catsanddog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    print(solution.word_break(s, word_dict))
    print(solution.word_break_dp(s, word_dict))
    print(solution.word_break_backtrack(s, word_dict))


if __name__ == "__main__":
    main()
