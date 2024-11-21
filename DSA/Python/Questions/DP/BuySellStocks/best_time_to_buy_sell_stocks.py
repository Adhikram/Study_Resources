"""
# Question: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Problem Statement:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a 
# different day in the future to sell that stock. Return the maximum profit you can achieve 
# from this transaction. If you cannot achieve any profit, return 0.

# Example:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5


# Optimization Notes:
# - Space optimized solution is best for production use
# - Single pass through array is sufficient
# - No need to store previous states
# - Can handle large input sizes efficiently

# Edge Cases:
# - Empty array
# - Array with single element
# - Strictly decreasing prices
# - Equal prices throughout
"""

from typing import List


"""
[Previous documentation remains the same until algorithms section]
"""

from typing import List

# 1. Recursive Solution
"""
Algorithm:
1. Base case: if index reaches end of array, return 0
2. Calculate current profit using current price and minimum price seen
3. Update minimum price if current price is lower
4. Recursively calculate profit for remaining days
5. Return maximum of current profit and future profit

Time Complexity: O(2^n) - each day has two choices
Space Complexity: O(n) - recursion stack depth
"""


def max_profit_recursive(prices: List[int], index: int, min_price: int) -> int:
    if index >= len(prices):
        return 0

    curr_profit = prices[index] - min_price
    min_price = min(min_price, prices[index])
    future_profit = max_profit_recursive(prices, index + 1, min_price)

    return max(curr_profit, future_profit)


# 2. Memoization Solution
"""
Algorithm:
1. Use dictionary to cache results for each state (index, min_price)
2. If state exists in cache, return cached result
3. Calculate current profit and update minimum price
4. Cache and return maximum profit possible from current state

Time Complexity: O(n) - each state computed once
Space Complexity: O(n) - storing states in dictionary
"""


def max_profit_memo(prices: List[int]) -> int:
    dp = {}

    def solve(index: int, min_price: int) -> int:
        if index >= len(prices):
            return 0

        if (index, min_price) in dp:
            return dp[(index, min_price)]

        curr_profit = prices[index] - min_price
        min_price = min(min_price, prices[index])
        future_profit = solve(index + 1, min_price)

        dp[(index, min_price)] = max(curr_profit, future_profit)
        return dp[(index, min_price)]

    return solve(0, float("inf"))


# 3. Tabulation Solution
"""
Algorithm:
1. Create DP array of size n initialized with 0
2. Track minimum price starting with first element
3. For each day i from 1 to n:
   - Calculate profit if selling on day i
   - Update dp[i] with max profit possible until day i
   - Update minimum price seen so far

Time Complexity: O(n) - single pass through array
Space Complexity: O(n) - dp array storage
"""


def max_profit_tabulation(prices: List[int]) -> int:
    if not prices:
        return 0

    n = len(prices)
    dp = [0] * n
    min_price = prices[0]

    for i in range(1, n):
        curr_profit = prices[i] - min_price
        dp[i] = max(dp[i - 1], curr_profit)
        min_price = min(min_price, prices[i])

    return dp[-1]


# 4. Space Optimized Solution
"""
Algorithm:
1. Initialize max_profit as 0 and min_price as infinity
2. For each price in array:
   - Update min_price if current price is lower
   - Calculate potential profit with current price
   - Update max_profit if current profit is higher

Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - constant extra space
"""


def max_profit_optimized(prices: List[int]) -> int:
    max_profit = 0
    min_price = float("inf")

    for price in prices:
        min_price = min(min_price, price)
        curr_profit = price - min_price
        max_profit = max(max_profit, curr_profit)

    return max_profit


def main():
    # Test cases
    test_cases = [
        [7, 1, 5, 3, 6, 4],  # Regular case
        [7, 6, 4, 3, 1],  # Strictly decreasing
        [1],  # Single element
        [],  # Empty array
        [1, 1, 1, 1],  # Equal prices
        [3, 2, 6, 5, 0, 3],  # Multiple peaks and valleys
        [2, 4, 1],  # Early peak
        [1, 2, 3, 4, 5],  # Strictly increasing
    ]

    for i, prices in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {prices}")
        if prices:
            print(
                f"Recursive Solution: {max_profit_recursive(prices, 0, float('inf'))}"
            )
            print(f"Memoization Solution: {max_profit_memo(prices)}")
            print(f"Tabulation Solution: {max_profit_tabulation(prices)}")
            print(f"Optimized Solution: {max_profit_optimized(prices)}")
        else:
            print("Empty array - no profit possible")


if __name__ == "__main__":
    main()
