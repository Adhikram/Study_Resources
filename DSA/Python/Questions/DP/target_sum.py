"""
# Question: Target Sum
# Link: https://leetcode.com/problems/target-sum/

# Problem Statement:
# Given an array of integers nums and an integer target, build an expression by adding 
# one of the symbols '+' and '-' before each integer in nums and concatenate them.
# Return the number of different expressions that evaluate to target.

# Example:
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: -1+1+1+1+1, +1-1+1+1+1, +1+1-1+1+1, +1+1+1-1+1, +1+1+1+1-1
"""

from typing import List

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. Convert problem to subset sum
2. Find count of subsets with sum = (total_sum + target) / 2
3. Use memoization to store intermediate results

Time Complexity: O(N*K) where K is sum of array elements
Space Complexity: O(N*K) + O(N) for recursion stack
"""


def target_sum_recursive(nums: List[int], target: int) -> int:
    total_sum = sum(nums)
    n = len(nums)

    # Edge cases
    if total_sum < abs(target):
        return 0
    if (total_sum + target) % 2:
        return 0

    target_sum = (total_sum + target) // 2
    dp = [[-1] * (target_sum + 1) for _ in range(n)]

    def solve(ind: int, target: int) -> int:
        if ind == 0:
            if target == 0 and nums[0] == 0:
                return 2
            if target == 0 or target == nums[0]:
                return 1
            return 0

        if dp[ind][target] != -1:
            return dp[ind][target]

        not_take = solve(ind - 1, target)
        take = 0
        if nums[ind] <= target:
            take = solve(ind - 1, target - nums[ind])

        dp[ind][target] = take + not_take
        return dp[ind][target]

    return solve(n - 1, target_sum)


# 2. Tabulation Solution
"""
Algorithm:
1. Create dp table of size n * target_sum
2. Initialize base cases
3. Fill dp table iteratively
4. Handle special case of zero elements

Time Complexity: O(N*K)
Space Complexity: O(N*K)
"""


def target_sum_tabulation(nums: List[int], target: int) -> int:
    total_sum = sum(nums)
    n = len(nums)

    if total_sum < abs(target):
        return 0
    if (total_sum + target) % 2:
        return 0

    target_sum = (total_sum + target) // 2
    dp = [[0] * (target_sum + 1) for _ in range(n)]

    # Base cases
    if nums[0] == 0:
        dp[0][0] = 2
    else:
        dp[0][0] = 1
        if nums[0] <= target_sum:
            dp[0][nums[0]] = 1

    # Fill dp table
    for ind in range(1, n):
        for sum_ in range(target_sum + 1):
            not_take = dp[ind - 1][sum_]
            take = 0
            if nums[ind] <= sum_:
                take = dp[ind - 1][sum_ - nums[ind]]
            dp[ind][sum_] = take + not_take

    return dp[n - 1][target_sum]


# 3. Space Optimized Solution
"""
Algorithm:
1. Use single array instead of 2D array
2. Update array for each number
3. Process from right to left to avoid overwriting

Time Complexity: O(N*K)
Space Complexity: O(K)
"""


def target_sum_optimized(nums: List[int], target: int) -> int:
    total_sum = sum(nums)
    n = len(nums)

    if total_sum < abs(target):
        return 0
    if (total_sum + target) % 2:
        return 0

    target_sum = (total_sum + target) // 2
    prev = [0] * (target_sum + 1)

    # Base cases
    if nums[0] == 0:
        prev[0] = 2
    else:
        prev[0] = 1
        if nums[0] <= target_sum:
            prev[nums[0]] = 1

    # Fill array
    for ind in range(1, n):
        curr = [0] * (target_sum + 1)
        for sum_ in range(target_sum + 1):
            not_take = prev[sum_]
            take = 0
            if nums[ind] <= sum_:
                take = prev[sum_ - nums[ind]]
            curr[sum_] = take + not_take
        prev = curr[:]

    return prev[target_sum]


def main():
    test_cases = [
        {"nums": [1, 1, 1, 1, 1], "target": 3},
        {"nums": [1], "target": 1},
        {"nums": [1, 0], "target": 1},
        {"nums": [0, 0, 0, 0, 0, 0, 0, 0, 1], "target": 1},
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Numbers: {test['nums']}")
        print(f"Target: {test['target']}")
        print(
            f"Recursive Solution: {target_sum_recursive(test['nums'], test['target'])}"
        )
        print(
            f"Tabulation Solution: {target_sum_tabulation(test['nums'], test['target'])}"
        )
        print(
            f"Optimized Solution: {target_sum_optimized(test['nums'], test['target'])}"
        )


if __name__ == "__main__":
    main()
