"""
# Question: Best Time to Buy and Sell Stock IV (k transactions)
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# Problem Statement:
# Given an array prices[] representing stock prices and an integer k, find the maximum 
# profit that can be earned by doing at most k transactions. One transaction consists
# of buying a stock and then selling it.

# Example:
# Input: prices = [3,2,6,5,0,3], k = 2
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
# Then buy on day 5 (price = 0) and sell on day 6 (prcice = 3), profit = 3-0 = 3.
"""

from typing import List

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. Use 3D DP array to store states: [index][buy/sell][transactions]
2. For each state:
   - If can buy: choose between buying current stock or skipping
   - If can sell: choose between selling current stock or skipping
3. Track remaining transactions and return maximum profit

Time Complexity: O(n*k*2) - three changing parameters in states
Space Complexity: O(n*k*2) + O(n) - DP array + recursion stack
"""


def max_profit_recursive(self, prices: List[int], k: int) -> int:
    n = len(prices)
    dp = [[[-1] * (k + 1) for _ in range(2)] for _ in range(n)]

    def solve(ind: int, can_buy: int, cap: int) -> int:
        if ind == n or cap == 0:
            return 0

        if dp[ind][can_buy][cap] != -1:
            return dp[ind][can_buy][cap]

        profit = 0
        if can_buy:
            profit = max(-prices[ind] + solve(ind + 1, 0, cap), solve(ind + 1, 1, cap))
        else:
            profit = max(
                prices[ind] + solve(ind + 1, 1, cap - 1), solve(ind + 1, 0, cap)
            )

        dp[ind][can_buy][cap] = profit
        return profit

    return solve(0, 1, k)


# 2. Tabulation Solution
"""
Algorithm:
1. Create 3D DP table: [n+1][2][k+1]
2. Fill table bottom-up starting from last day
3. For each state, calculate maximum profit using:
   - Buy state: max(-price[i] + next_day[sell], skip)
   - Sell state: max(price[i] + next_day[buy], skip)

Time Complexity: O(n*k*2) - three nested loops
Space Complexity: O(n*k*2) - 3D DP array
"""


def max_profit_tabulation(self, prices: List[int], k: int) -> int:
    n = len(prices)
    dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(n + 1)]

    for ind in range(n - 1, -1, -1):
        for can_buy in range(2):
            for cap in range(1, k + 1):
                if can_buy:
                    dp[ind][can_buy][cap] = max(
                        -prices[ind] + dp[ind + 1][0][cap], dp[ind + 1][1][cap]
                    )
                else:
                    dp[ind][can_buy][cap] = max(
                        prices[ind] + dp[ind + 1][1][cap - 1], dp[ind + 1][0][cap]
                    )

    return dp[0][1][k]


# 3. Space Optimized Solution
"""
Algorithm:
1. Use two 2D arrays (ahead and curr) instead of 3D array
2. Process each day and update arrays:
   - Calculate current day profits using ahead array
   - Copy curr to ahead for next iteration
3. Space optimization by using only previous day's values

Time Complexity: O(n*k*2) - three nested loops
Space Complexity: O(k*2) - two 2D arrays
"""


def max_profit_optimized(self, prices: List[int], k: int) -> int:
    n = len(prices)
    ahead = [[0] * (k + 1) for _ in range(2)]
    curr = [[0] * (k + 1) for _ in range(2)]

    for ind in range(n - 1, -1, -1):
        for can_buy in range(2):
            for cap in range(1, k + 1):
                if can_buy:
                    curr[can_buy][cap] = max(
                        -prices[ind] + ahead[0][cap], ahead[1][cap]
                    )
                else:
                    curr[can_buy][cap] = max(
                        prices[ind] + ahead[1][cap - 1], ahead[0][cap]
                    )

        ahead = [row[:] for row in curr]

    return ahead[1][k]


def main():
    solver = KTransactions()
    test_cases = [
        ([3, 3, 5, 0, 0, 3, 1, 4], 2),  # Regular case
        ([1, 2, 3, 4, 5], 2),  # Strictly increasing
        ([7, 6, 4, 3, 1], 2),  # Strictly decreasing
        ([3, 2, 6, 5, 0, 3], 2),  # Multiple peaks
        ([1], 1),  # Single element
        ([1, 2], 1),  # Two elements
    ]

    for i, (prices, k) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: prices = {prices}, k = {k}")
        print(f"Recursive Solution: {solver.max_profit_recursive(prices, k)}")
        print(f"Tabulation Solution: {solver.max_profit_tabulation(prices, k)}")
        print(f"Optimized Solution: {solver.max_profit_optimized(prices, k)}")


if __name__ == "__main__":
    main()
