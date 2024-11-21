"""
# Question: Best Time to Buy and Sell Stock with Transaction Fee
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

# Problem Statement:
# You are given an array prices where prices[i] is the price of a given stock on the ith day,
# and an integer fee representing a transaction fee. Find the maximum profit you can achieve.
# You may complete as many transactions as you like, but you need to pay the transaction fee
# for each transaction.

# Example:
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8
"""

from typing import List

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. For each day, maintain buy/sell state
2. When selling, subtract transaction fee
3. Use memoization to store computed states
4. Return maximum achievable profit

Time Complexity: O(n*2)
Space Complexity: O(n*2) + O(n) recursion stack
"""
def max_profit_recursive(prices: List[int], fee: int) -> int:
    n = len(prices)
    dp = {}
    
    def solve(index: int, can_buy: bool) -> int:
        if index >= n:
            return 0
            
        if (index, can_buy) in dp:
            return dp[(index, can_buy)]
            
        if can_buy:
            profit = max(-prices[index] + solve(index + 1, False),
                        solve(index + 1, True))
        else:
            profit = max(prices[index] - fee + solve(index + 1, True),
                        solve(index + 1, False))
                        
        dp[(index, can_buy)] = profit
        return profit
        
    return solve(0, True)

# 2. Tabulation Solution
"""
Algorithm:
1. Create 2D DP array [n+1][2]
2. Fill table bottom-up
3. For each state:
   - Buy: max(-price[i] + dp[i+1][0], dp[i+1][1])
   - Sell: max(price[i] - fee + dp[i+1][1], dp[i+1][0])

Time Complexity: O(n*2)
Space Complexity: O(n*2)
"""
def max_profit_tabulation(prices: List[int], fee: int) -> int:
    n = len(prices)
    dp = [[0] * 2 for _ in range(n + 1)]
    
    for i in range(n-1, -1, -1):
        for buy in range(2):
            if buy:
                dp[i][buy] = max(-prices[i] + dp[i+1][0],
                                dp[i+1][1])
            else:
                dp[i][buy] = max(prices[i] - fee + dp[i+1][1],
                                dp[i+1][0])
                                
    return dp[0][1]

# 3. Space Optimized Solution
"""
Algorithm:
1. Use two arrays (ahead and curr) instead of 2D array
2. Process each day and update arrays
3. Include transaction fee in sell operation

Time Complexity: O(n*2)
Space Complexity: O(1)
"""
def max_profit_optimized(prices: List[int], fee: int) -> int:
    n = len(prices)
    ahead = [0] * 2
    curr = [0] * 2
    
    for i in range(n-1, -1, -1):
        for buy in range(2):
            if buy:
                curr[buy] = max(-prices[i] + ahead[0],
                               ahead[1])
            else:
                curr[buy] = max(prices[i] - fee + ahead[1],
                               ahead[0])
        ahead = curr[:]
        
    return ahead[1]

def main():
    test_cases = [
        ([1, 3, 2, 8, 4, 9], 2),      # Regular case
        ([1, 3, 7, 5, 10, 3], 3),     # Multiple transactions
        ([1], 1),                      # Single element
        ([1, 4], 2),                   # Two elements
        ([1, 2, 3, 4, 5], 1),         # Strictly increasing
        ([5, 4, 3, 2, 1], 1)          # Strictly decreasing
    ]
    
    for i, (prices, fee) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: prices = {prices}, fee = {fee}")
        print(f"Recursive Solution: {max_profit_recursive(prices, fee)}")
        print(f"Tabulation Solution: {max_profit_tabulation(prices, fee)}")
        print(f"Optimized Solution: {max_profit_optimized(prices, fee)}")

if __name__ == "__main__":
    main()
