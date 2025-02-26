"""
# Question: 0/1 Knapsack Problem
# Link: https://leetcode.com/problems/0-1-knapsack/

# Problem Statement:
# Given weights and values of n items, put these items in a knapsack of capacity W
# to get the maximum total value in the knapsack.

# Example:
# Input: 
# values = [12, 10, 21, 15]
# weights = [2, 1, 3, 2]
# capacity = 5
# Output: 48
"""

from typing import List

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. For each item, explore two choices:
   - Include item if weight allows
   - Skip item and move to next
2. Track remaining capacity and current index
3. Cache results in dp table
4. Return maximum value possible

Time Complexity: O(N*W) where N is number of items and W is capacity
Space Complexity: O(N*W) + O(N) for dp table and recursion stack
"""


def knapsack_recursive(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    dp = [[-1] * (capacity + 1) for _ in range(n)]

    def solve(ind: int, W: int) -> int:
        # Base case: no items left or no capacity
        if ind == 0:
            if weights[0] <= W:
                return values[0]
            return 0

        if dp[ind][W] != -1:
            return dp[ind][W]

        # Don't take current item
        not_take = solve(ind - 1, W)

        # Take current item if possible
        take = 0
        if weights[ind] <= W:
            take = values[ind] + solve(ind - 1, W - weights[ind])

        dp[ind][W] = max(take, not_take)
        return dp[ind][W]

    return solve(n - 1, capacity)


# 2. Tabulation Solution
"""
Algorithm:
1. Create dp table of size n * (capacity + 1)
2. Initialize first row based on first item
3. For each item and capacity:
   - Calculate value without taking item
   - Calculate value with taking item if possible
   - Store maximum value
4. Return value in dp[n-1][capacity]

Time Complexity: O(N*W)
Space Complexity: O(N*W)
"""


def knapsack_tabulation(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n)]

    # Initialize first row
    for w in range(weights[0], capacity + 1):
        dp[0][w] = values[0]

    # Fill dp table
    for ind in range(1, n):
        for cap in range(capacity + 1):
            not_take = dp[ind - 1][cap]

            take = 0
            if weights[ind] <= cap:
                take = values[ind] + dp[ind - 1][cap - weights[ind]]

            dp[ind][cap] = max(take, not_take)

    return dp[n - 1][capacity]


# 3. Space Optimized Solution
"""
Algorithm:
1. Use single array instead of 2D array
2. Process each item and update array
3. Calculate from right to left to avoid overwriting
4. Return final value in array[capacity]

Time Complexity: O(N*W)
Space Complexity: O(W)
"""


def knapsack_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    prev = [0] * (capacity + 1)

    # Initialize first row
    for w in range(weights[0], capacity + 1):
        prev[w] = values[0]

    # Process each item
    for ind in range(1, n):
        for cap in range(capacity, -1, -1):
            not_take = prev[cap]

            take = 0
            if weights[ind] <= cap:
                take = values[ind] + prev[cap - weights[ind]]

            prev[cap] = max(take, not_take)

    return prev[capacity]


# 4. Bitmasking Solution
"""
Algorithm:
1. Use bitmasking to iterate through all possible combinations
2. For each combination:
   - Calculate total weight and
   - Update max value if valid
   Return max value
   Time Complexity: O(2^N)
   ce Complexity: O(1)
   """


def knapsack_bitmask(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    max_value = 0

    # Try all possible combinations using bit masking
    for mask in range(1 << n):
        total_weight = 0
        total_value = 0

        # Check each bit position
        for i in range(n):
            if mask & (1 << i):
                total_weight += weights[i]
                total_value += values[i]

        # Update max_value if current combination is valid
        if total_weight <= capacity:
            max_value = max(max_value, total_value)

    return max_value


def main():
    # Test cases
    test_cases = [
        {"weights": [2, 1, 3, 2], "values": [12, 10, 21, 15], "capacity": 5},
        {"weights": [1, 2, 3], "values": [10, 15, 40], "capacity": 6},
        {"weights": [2], "values": [3], "capacity": 2},
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Weights: {test['weights']}")
        print(f"Values: {test['values']}")
        print(f"Capacity: {test['capacity']}")
        print(
            f"Recursive Solution: {knapsack_recursive(test['weights'], test['values'], test['capacity'])}"
        )
        print(
            f"Tabulation Solution: {knapsack_tabulation(test['weights'], test['values'], test['capacity'])}"
        )
        print(
            f"Optimized Solution: {knapsack_optimized(test['weights'], test['values'], test['capacity'])}"
        )
        print(
            f"Bitmask Solution: {knapsack_bitmask(test['weights'], test['values'], test['capacity'])}"
        )


if __name__ == "__main__":
    main()
