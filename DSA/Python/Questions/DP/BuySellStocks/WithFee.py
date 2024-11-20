"""
# Question: Best Time to Buy and Sell Stock with Transaction Fee
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

# Approaches:
# 1. State Machine DP
# 2. Space-optimized solution
# 3. Cash and Hold states

# Key Points:
# - Transaction fee for each trade
# - Two states: holding and not holding stock
# - Maximize profit considering fees
"""


class WithFee:
    def max_profit_state_machine(self, prices: list[int], fee: int) -> int:
        """
        State Machine Approach
        Time: O(N), Space: O(1)
        """
        cash = 0
        hold = -prices[0]

        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)

        return cash

    def max_profit_dp(self, prices: list[int], fee: int) -> int:
        """
        Dynamic Programming Approach
        Time: O(N), Space: O(N)
        """
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[n - 1][0]


def main():
    solution = WithFee()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(solution.max_profit_state_machine(prices, fee))  # Expected: 8
    print(solution.max_profit_dp(prices, fee))  # Expected: 8


if __name__ == "__main__":
    main()
