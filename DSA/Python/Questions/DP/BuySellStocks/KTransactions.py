"""
# Question: Best Time to Buy and Sell Stock IV
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# Approaches:
# 1. DP with state transitions
# 2. Space-optimized DP
# 3. Quick solution for large k

# Key Insights:
# - k transactions limit
# - Buy before selling
# - Optimize state transitions
"""


class KTransactions:
    def max_profit_dp(self, k: int, prices: list[int]) -> int:
        """
        Dynamic Programming approach
        Time: O(n*k), Space: O(n*k)
        """
        if not prices or k == 0:
            return 0

        n = len(prices)
        dp = [[0] * n for _ in range(k + 1)]

        for i in range(1, k + 1):
            local_max = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + local_max)
                local_max = max(local_max, dp[i - 1][j - 1] - prices[j])

        return dp[k][n - 1]

    def max_profit_optimized(self, k: int, prices: list[int]) -> int:
        """
        Space-optimized approach
        Time: O(n*k), Space: O(k)
        """
        if not prices:
            return 0

        if k >= len(prices) // 2:
            return sum(
                max(0, prices[i + 1] - prices[i]) for i in range(len(prices) - 1)
            )

        buy = [-float("inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i - 1] - price)
                sell[i] = max(sell[i], buy[i] + price)

        return sell[k]


def main():
    solution = KTransactions()
    prices = [3, 2, 6, 5, 0, 3]
    k = 2
    print(solution.max_profit_dp(k, prices))  # Expected: 7
    print(solution.max_profit_optimized(k, prices))  # Expected: 7


if __name__ == "__main__":
    main()
