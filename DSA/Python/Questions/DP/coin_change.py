"""
# Question: Coin Change
# Link: https://leetcode.com/problems/coin-change/

# Problem Statement:
# Given an array of distinct coins and a target sum, find the number of ways
# to make change for the target using the coins. You have an infinite supply
# of each coin denomination.

# Example:
# Input: coins = [1,2,3], target = 4
# Output: 4
# Explanation: {1,1,1,1}, {1,1,2}, {2,2}, {1,3}

# Key Insights:
# - Each coin can be used multiple times (infinite supply)
# - Order of coins in combination doesn't matter
# - Need to handle overlapping subproblems efficiently
"""

from typing import List

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. For each coin, we have two choices at each step:
   - Take the current coin if target >= coin value
   - Skip the current coin and move to next
2. Use memoization to avoid recalculating same states

Time Complexity: O(N*T) where N is number of coins and T is target
Space Complexity: O(N*T) for dp array + O(N) for recursion stack
"""


def count_ways_recursive(coins: List[int], target: int) -> int:
    # Initialize dp array for memoization
    n = len(coins)
    dp = [[-1] * (target + 1) for _ in range(n)]

    def solve(ind: int, target: int) -> int:
        # Base case: found valid combination
        if target == 0:
            return 1

        # Base case: processing first coin
        if ind == 0:
            # Check if target is divisible by first coin
            return 1 if target % coins[0] == 0 else 0

        # Return memoized result if available
        if dp[ind][target] != -1:
            return dp[ind][target]

        # Calculate ways without taking current coin
        not_take = solve(ind - 1, target)

        # Calculate ways by taking current coin if possible
        take = 0
        if coins[ind] <= target:
            take = solve(ind, target - coins[ind])

        # Store result in dp array and return
        dp[ind][target] = take + not_take
        return dp[ind][target]

    return solve(n - 1, target)


# 2. Tabulation Solution
"""
Algorithm:
1. Build solution bottom-up using 2D dp array
2. For each coin and target value:
   - Calculate ways without current coin
   - Add ways including current coin if possible

Time Complexity: O(N*T)
Space Complexity: O(N*T)
"""


def count_ways_tabulation(coins: List[int], target: int) -> int:
    n = len(coins)
    # Create and initialize dp array
    dp = [[0] * (target + 1) for _ in range(n)]

    # Initialize first row (base case for first coin)
    for t in range(target + 1):
        dp[0][t] = 1 if t % coins[0] == 0 else 0

    # Fill dp table for remaining coins
    for ind in range(1, n):
        for t in range(target + 1):
            # Ways without current coin
            not_take = dp[ind - 1][t]

            # Ways including current coin
            take = 0
            if coins[ind] <= t:
                take = dp[ind][t - coins[ind]]

            # Total ways = ways with + ways without
            dp[ind][t] = take + not_take

    return dp[n - 1][target]


# 3. Space Optimized Solution
"""
Algorithm:
1. Use only previous row to calculate current row
2. Optimize space by using 1D arrays instead of 2D

Time Complexity: O(N*T)
Space Complexity: O(T)
"""


def count_ways_optimized(coins: List[int], target: int) -> int:
    n = len(coins)
    # Initialize previous array with base case
    prev = [1 if t % coins[0] == 0 else 0 for t in range(target + 1)]

    # Process each coin
    for ind in range(1, n):
        # Current state array
        curr = [0] * (target + 1)

        # Calculate for each target
        for t in range(target + 1):
            # Ways without current coin
            not_take = prev[t]

            # Ways with current coin
            take = 0
            if coins[ind] <= t:
                take = curr[t - coins[ind]]

            # Update current state
            curr[t] = take + not_take

        # Update previous for next iteration
        prev = curr[:]

    return prev[target]


def main():
    # Test cases covering various scenarios
    test_cases = [
        ([1, 2, 3], 4),  # Multiple solutions
        ([2, 5, 10], 15),  # Larger target
        ([1], 5),  # Single coin
        ([1, 2, 5], 0),  # Zero target
        ([186, 419, 83, 408], 6249),  # Large numbers
    ]

    # Run all solutions for each test case
    for i, (coins, target) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: coins = {coins}, target = {target}")
        print(f"Recursive Solution: {count_ways_recursive(coins, target)}")
        print(f"Tabulation Solution: {count_ways_tabulation(coins, target)}")
        print(f"Optimized Solution: {count_ways_optimized(coins, target)}")


if __name__ == "__main__":
    main()
