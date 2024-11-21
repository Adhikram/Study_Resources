"""
# Question: Best Time to Buy and Sell Stock with Cooldown
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# Problem Statement:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# After selling stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Find the maximum profit you can achieve.

# Example:
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: Buy on day 1 (price = 1) and sell on day 2 (price = 2), profit = 1.
# Then buy on day 4 (price = 0) and sell on day 5 (price = 2), profit = 2.
# Total profit = 3.
"""

from typing import List

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. For each day, three possible states:
   - Buy stock if not in cooldown
   - Sell stock and enter cooldown
   - Skip current day
2. Use memoization to store results
3. Handle cooldown by skipping next day after sell

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
            profit = max(-prices[index] + solve(index + 1, False),
                        solve(index + 1, True))
        else:
            profit = max(prices[index] + solve(index + 2, True),
                        solve(index + 1, False))
                        
        dp[(index, can_buy)] = profit
        return profit
        
    return solve(0, True)

# 2. Tabulation Solution
"""
Algorithm:
1. Create 2D DP array [n+2][2]
2. Fill table bottom-up
3. For each state:
   - Buy: max(-price[i] + dp[i+1][0], dp[i+1][1])
   - Sell: max(price[i] + dp[i+2][1], dp[i+1][0])
4. Handle cooldown in sell state

Time Complexity: O(n*2)
Space Complexity: O(n*2)
"""
def max_profit_tabulation(prices: List[int]) -> int:
    n = len(prices)
    dp = [[0] * 2 for _ in range(n + 2)]
    
    for i in range(n-1, -1, -1):
        for buy in range(2):
            if buy:
                dp[i][buy] = max(-prices[i] + dp[i+1][0],
                                dp[i+1][1])
            else:
                dp[i][buy] = max(prices[i] + dp[i+2][1],
                                dp[i+1][0])
                                
    return dp[0][1]

# 3. Space Optimized Solution
"""
Algorithm:
1. Use three arrays for current and next two days
2. Process each day updating arrays
3. Handle cooldown period using two ahead states

Time Complexity: O(n*2)
Space Complexity: O(1)
"""
def max_profit_optimized(prices: List[int]) -> int:
    n = len(prices)
    front1 = [0] * 2
    front2 = [0] * 2
    curr = [0] * 2
    
    for i in range(n-1, -1, -1):
        for buy in range(2):
            if buy:
                curr[buy] = max(-prices[i] + front1[0],
                               front1[1])
            else:
                curr[buy] = max(prices[i] + front2[1],
                               front1[0])
                               
        front2 = front1[:]
        front1 = curr[:]
        
    return curr[1]

def main():
    test_cases = [
        [1, 2, 3, 0, 2],              # Regular case
        [1],                          # Single element
        [1, 2],                       # Two elements
        [1, 2, 3, 4, 5],              # Strictly increasing
        [5, 4, 3, 2, 1],              # Strictly decreasing
        [2, 1, 4, 5, 2, 9, 7]         # Multiple peaks and valleys
    ]
    
    for i, prices in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {prices}")
        print(f"Recursive Solution: {max_profit_recursive(prices)}")
        print(f"Tabulation Solution: {max_profit_tabulation(prices)}")
        print(f"Optimized Solution: {max_profit_optimized(prices)}")

if __name__ == "__main__":
    main()
