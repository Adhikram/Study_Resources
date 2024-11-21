"""
# Question: Subset Sum Problem
# Link: https://leetcode.com/problems/partition-equal-subset-sum/

# Problem Statement:
# Given an array 'ARR' with N positive integers. Find if there is a subset in ARR
# with a sum equal to K. Return true if such a subset exists, false otherwise.

# Example:
# Input: arr = [1, 2, 3, 4], k = 7
# Output: True
# Explanation: Subset [3, 4] sums to 7
"""

from typing import List

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. For each element, we have two choices:
   - Include in sum
   - Exclude from sum
2. Track current index and target sum
3. Use dp table to memoize results

Time Complexity: O(N*K) where N is array length and K is target sum
Space Complexity: O(N*K) + O(N) for dp array and recursion stack
"""


def subset_sum_recursive(arr: List[int], k: int) -> bool:
    n = len(arr)
    dp = [[-1] * (k + 1) for _ in range(n)]

    def solve(ind: int, target: int) -> bool:
        # Base case: target achieved
        if target == 0:
            return True

        # Base case: first element
        if ind == 0:
            return arr[0] == target

        # Return memoized result
        if dp[ind][target] != -1:
            return dp[ind][target] == 1

        # Try not taking current element
        not_take = solve(ind - 1, target)

        # Try taking current element if possible
        take = False
        if arr[ind] <= target:
            take = solve(ind - 1, target - arr[ind])

        # Store result in dp
        dp[ind][target] = 1 if (take or not_take) else 0
        return take or not_take

    return solve(n - 1, k)


# 2. Tabulation Solution
"""
Algorithm:
1. Create dp table of size n * (k+1)
2. Initialize base cases for first row
3. For each element and sum:
   - Try including and excluding current element
   - Store result in dp table

Time Complexity: O(N*K)
Space Complexity: O(N*K)
"""


def subset_sum_tabulation(arr: List[int], k: int) -> bool:
    n = len(arr)
    dp = [[False] * (k + 1) for _ in range(n)]

    # Initialize first row
    for i in range(n):
        dp[i][0] = True
    if arr[0] <= k:
        dp[0][arr[0]] = True

    # Fill dp table
    for ind in range(1, n):
        for target in range(1, k + 1):
            not_take = dp[ind - 1][target]

            take = False
            if arr[ind] <= target:
                take = dp[ind - 1][target - arr[ind]]

            dp[ind][target] = take or not_take

    return dp[n - 1][k]


# 3. Space Optimized Solution
"""
Algorithm:
1. Use single array instead of 2D array
2. Update array for each element
3. Process right to left to avoid overwriting

Time Complexity: O(N*K)
Space Complexity: O(K)
"""


def subset_sum_optimized(arr: List[int], k: int) -> bool:
    n = len(arr)
    prev = [False] * (k + 1)

    # Initialize first row
    prev[0] = True
    if arr[0] <= k:
        prev[arr[0]] = True

    # Process each element
    for ind in range(1, n):
        curr = [False] * (k + 1)
        curr[0] = True
        for target in range(1, k + 1):
            not_take = prev[target]

            take = False
            if arr[ind] <= target:
                take = prev[target - arr[ind]]

            curr[target] = take or not_take
        prev = curr[:]

    return prev[k]


def main():
    # Test cases
    test_cases = [
        {"arr": [1, 2, 3, 4], "k": 7},
        {"arr": [2, 3, 7, 8, 10], "k": 11},
        {"arr": [1, 2, 3], "k": 7},
        {"arr": [3], "k": 3},
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Array: {test['arr']}")
        print(f"Target Sum: {test['k']}")
        print(f"Recursive Solution: {subset_sum_recursive(test['arr'], test['k'])}")
        print(f"Tabulation Solution: {subset_sum_tabulation(test['arr'], test['k'])}")
        print(f"Optimized Solution: {subset_sum_optimized(test['arr'], test['k'])}")


if __name__ == "__main__":
    main()
