"""
# Question: Best Time to Buy and Sell Stock with Cooldown
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# Approaches:
# 1. State Machine DP
# 2. Space-optimized DP
# 3. Recursive with memoization

# Key Points:
# - Must cooldown one day after selling
# - Track three states: buy, sell, rest
# - Optimize state transitions
"""


class WithCoolDown:
    def max_profit_state_machine(self, prices: list[int]) -> int:
        """
        State Machine Approach
        Time: O(N), Space: O(1)
        """
        sold = 0
        hold = -float("inf")
        rest = 0

        for price in prices:
            prev_sold = sold
            sold = hold + price
            hold = max(hold, rest - price)
            rest = max(rest, prev_sold)

        return max(sold, rest)

    def max_profit_dp(self, prices: list[int]) -> int:
        """
        Dynamic Programming Approach
        Time: O(N), Space: O(N)
        """
        if not prices:
            return 0

        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[1][1] = -prices[0]

        for i in range(2, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i - 1])

        return dp[n][0]


def main():
    solution = WithCoolDown()
    prices = [1, 2, 3, 0, 2]
    print(solution.max_profit_state_machine(prices))  # Expected: 3
    print(solution.max_profit_dp(prices))  # Expected: 3


if __name__ == "__main__":
    main()
