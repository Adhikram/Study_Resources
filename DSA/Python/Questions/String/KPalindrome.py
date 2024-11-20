"""
# Question: K-Palindrome
# Link: https://leetcode.com/problems/valid-palindrome-iii/

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

# Algorithm:
# 1. Use dynamic programming for palindrome check
# 2. Calculate minimum deletions needed
# 3. Compare with k value
# 4. Handle character frequency for optimization

# Key Components:
# - is_k_palindrome(): Main implementation using DP
# - can_construct(): Alternative approach using character frequency
"""


class KPalindrome:
    def is_k_palindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Initialize base cases
        for i in range(n + 1):
            dp[i][0] = i
            dp[0][i] = i

        # Fill dp table
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s[n - j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

        return dp[n][n] <= 2 * k

    def can_construct(self, s: str, k: int) -> bool:
        char_count = [0] * 26
        n = len(s)

        if k > n:
            return False

        # Count character frequencies
        for char in s:
            char_count[ord(char) - ord("a")] += 1

        odd_count = sum(1 for count in char_count if count % 2 != 0)
        return odd_count <= k


def main():
    solution = KPalindrome()
    s = "abcdeca"
    k = 2
    print(solution.is_k_palindrome(s, k))
    print(solution.can_construct(s, k))


if __name__ == "__main__":
    main()
