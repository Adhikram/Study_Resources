"""
# Question: Unbounded Knapsack
# Link: https://leetcode.com/problems/unbounded-knapsack/

# Problem Statement:
# Given a set of N items with certain weight and value, and a knapsack of capacity W.
# Each item can be picked any number of times. Find the maximum value that can be achieved.

# Example:
# Input: N = 4, W = 8
# values = [1, 30, 50, 70]
# weights = [1, 5, 3, 4]
# Output: 120
"""

from typing import List

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. For each item, we have two choices:
   - Take current item (can take multiple times)
   - Skip current item
2. Track remaining capacity and current index
3. Use dp table to store computed results

Time Complexity: O(N*W)
Space Complexity: O(N*W) + O(N) for recursion stack
"""


def unbounded_knapsack_recursive(
    weights: List[int], values: List[int], capacity: int
) -> int:
    n = len(weights)
    dp = [[-1] * (capacity + 1) for _ in range(n)]

    def solve(ind: int, W: int) -> int:
        # Base case: first item
        if ind == 0:
            return (W // weights[0]) * values[0]

        if dp[ind][W] != -1:
            return dp[ind][W]

        # Don't take current item
        not_taken = solve(ind - 1, W)

        # Take current item if possible
        taken = 0
        if weights[ind] <= W:
            taken = values[ind] + solve(ind, W - weights[ind])

        dp[ind][W] = max(not_taken, taken)
        return dp[ind][W]

    return solve(n - 1, capacity)


# 2. Tabulation Solution
"""
Algorithm:
1. Create dp table of size n * (capacity + 1)
2. Initialize first row based on first item
3. For each item and capacity:
   - Calculate value without taking item
   - Calculate value with taking item
   - Store maximum value

Time Complexity: O(N*W)
Space Complexity: O(N*W)
"""


def unbounded_knapsack_tabulation(
    weights: List[int], values: List[int], capacity: int
) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n)]

    # Initialize first row
    for w in range(capacity + 1):
        dp[0][w] = (w // weights[0]) * values[0]

    # Fill dp table
    for ind in range(1, n):
        for cap in range(capacity + 1):
            not_taken = dp[ind - 1][cap]

            taken = 0
            if weights[ind] <= cap:
                taken = values[ind] + dp[ind][cap - weights[ind]]

            dp[ind][cap] = max(not_taken, taken)

    return dp[n - 1][capacity]


# 3. Space Optimized Solution
"""
Algorithm:
1. Use single array instead of 2D array
2. Update array for each item
3. Process from left to right

Time Complexity: O(N*W)
Space Complexity: O(W)
"""


def unbounded_knapsack_optimized(
    weights: List[int], values: List[int], capacity: int
) -> int:
    n = len(weights)
    curr = [0] * (capacity + 1)

    # Initialize array
    for w in range(capacity + 1):
        curr[w] = (w // weights[0]) * values[0]

    # Process each item
    for ind in range(1, n):
        for cap in range(capacity + 1):
            not_taken = curr[cap]

            taken = 0
            if weights[ind] <= cap:
                taken = values[ind] + curr[cap - weights[ind]]

            curr[cap] = max(not_taken, taken)

    return curr[capacity]


def main():
    test_cases = [
        {"weights": [1, 5, 3, 4], "values": [1, 30, 50, 70], "capacity": 8},
        {"weights": [2, 4, 6], "values": [5, 11, 13], "capacity": 10},
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Weights: {test['weights']}")
        print(f"Values: {test['values']}")
        print(f"Capacity: {test['capacity']}")
        print(
            f"Recursive Solution: {unbounded_knapsack_recursive(test['weights'], test['values'], test['capacity'])}"
        )
        print(
            f"Tabulation Solution: {unbounded_knapsack_tabulation(test['weights'], test['values'], test['capacity'])}"
        )
        print(
            f"Optimized Solution: {unbounded_knapsack_optimized(test['weights'], test['values'], test['capacity'])}"
        )


if __name__ == "__main__":
    main()
