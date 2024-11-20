"""
# Question: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Time Complexity: O(N)
# Space Complexity: O(1)

# Algorithm:
# 1. Track minimum price seen so far
# 2. Calculate maximum profit at each step
# 3. Return maximum profit found

# Key Points:
# - Single transaction allowed
# - Buy before selling
# - Maximize profit
"""


class BestTimeToBuySellStocks:
    def max_profit_kadane(self, prices: list[int]) -> int:
        """
        Kadane's algorithm approach
        Time: O(N), Space: O(1)
        """
        curr_max = max_so_far = 0

        for i in range(1, len(prices)):
            curr_max = max(0, curr_max + prices[i] - prices[i - 1])
            max_so_far = max(max_so_far, curr_max)

        return max_so_far

    def max_profit_simple(self, prices: list[int]) -> int:
        """
        Simple one-pass approach
        Time: O(N), Space: O(1)
        """
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit


def main():
    solution = BestTimeToBuySellStocks()
    prices = [7, 1, 5, 3, 6, 4]
    print(solution.max_profit_simple(prices))  # Expected: 5
    print(solution.max_profit_kadane(prices))  # Expected: 5


if __name__ == "__main__":
    main()
