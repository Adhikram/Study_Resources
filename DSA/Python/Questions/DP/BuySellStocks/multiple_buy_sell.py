"""
# Question: Best Time to Buy and Sell Stock with Multiple Transactions
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Problem Statement:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times).

# Example:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 3.
# Total profit = 7.
"""

from typing import List

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. For each day, we have two choices:
   - Buy/Sell the stock
   - Skip the day
2. Track buy/sell state using boolean
3. Use memoization to store computed states

Time Complexity: O(n*2)
Space Complexity: O(n*2) + O(n) recursion stack
"""


def max_profit_recursive(prices: List[int]) -> int:
    n = len(prices)
    dp = {}

    def solve(index: int, can_buy: bool) -> int:
        if index >= n:
            return 0

        if (index, can_buy) in dp:
            return dp[(index, can_buy)]

        if can_buy:
            profit = max(
                -prices[index] + solve(index + 1, False), solve(index + 1, True)
            )
        else:
            profit = max(
                prices[index] + solve(index + 1, True), solve(index + 1, False)
            )

        dp[(index, can_buy)] = profit
        return profit

    return solve(0, True)


# 2. Tabulation Solution
"""
Algorithm:
1. Create 2D DP array [n+1][2]
2. Fill table bottom-up
3. For each state:
   - If can buy: max(-price[i] + dp[i+1][0], dp[i+1][1])
   - If can sell: max(price[i] + dp[i+1][1], dp[i+1][0])

Time Complexity: O(n*2)
Space Complexity: O(n*2)
"""


def max_profit_tabulation(prices: List[int]) -> int:
    n = len(prices)
    dp = [[0] * 2 for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for buy in range(2):
            if buy:
                dp[i][buy] = max(-prices[i] + dp[i + 1][0], dp[i + 1][1])
            else:
                dp[i][buy] = max(prices[i] + dp[i + 1][1], dp[i + 1][0])

    return dp[0][1]


# 3. Space Optimized Solution
"""
Algorithm:
1. Use two arrays (ahead and curr) instead of 2D array
2. Process each day and update arrays
3. Optimize space by using only previous day's values

Time Complexity: O(n*2)
Space Complexity: O(1)
"""


def max_profit_optimized(prices: List[int]) -> int:
    n = len(prices)
    ahead = [0] * 2
    curr = [0] * 2

    for i in range(n - 1, -1, -1):
        for buy in range(2):
            if buy:
                curr[buy] = max(-prices[i] + ahead[0], ahead[1])
            else:
                curr[buy] = max(prices[i] + ahead[1], ahead[0])
        ahead = curr[:]

    return ahead[1]


def main():
    test_cases = [
        [7, 1, 5, 3, 6, 4],  # Regular case
        [1, 2, 3, 4, 5],  # Strictly increasing
        [7, 6, 4, 3, 1],  # Strictly decreasing
        [1],  # Single element
        [1, 2],  # Two elements
        [3, 3, 5, 0, 0, 3, 1, 4],  # Multiple peaks and valleys
    ]

    for i, prices in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {prices}")
        print(f"Recursive Solution: {max_profit_recursive(prices)}")
        print(f"Tabulation Solution: {max_profit_tabulation(prices)}")
        print(f"Optimized Solution: {max_profit_optimized(prices)}")


if __name__ == "__main__":
    main()
