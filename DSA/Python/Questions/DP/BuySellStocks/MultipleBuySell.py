"""
# Question: Best Time to Buy and Sell Stock II
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Approaches:
# 1. Peak Valley approach
# 2. Simple one pass
# 3. State machine approach

# Time Complexity: O(N)
# Space Complexity: O(1)
"""


class MultipleBuySell:
    def max_profit_peak_valley(self, prices: list[int]) -> int:
        """
        Peak Valley Approach
        Time: O(N), Space: O(1)
        """
        i = 0
        valley = peak = prices[0]
        max_profit = 0

        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]

            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]

            max_profit += peak - valley

        return max_profit

    def max_profit_simple(self, prices: list[int]) -> int:
        """
        Simple One Pass Solution
        Time: O(N), Space: O(1)
        """
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))

    def max_profit_state_machine(self, prices: list[int]) -> int:
        """
        State Machine Approach
        Time: O(N), Space: O(1)
        """
        hold = -float("inf")
        sold = 0

        for price in prices:
            prev_sold = sold
            sold = max(sold, hold + price)
            hold = max(hold, prev_sold - price)

        return sold


def main():
    solution = MultipleBuySell()
    prices = [7, 1, 5, 3, 6, 4]
    print(solution.max_profit_peak_valley(prices))
    print(solution.max_profit_simple(prices))
    print(solution.max_profit_state_machine(prices))


if __name__ == "__main__":
    main()
