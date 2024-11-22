"""
# Question: Jump Game II
# Link: https://leetcode.com/problems/jump-game-ii/

# Problem Statement:
# Given an array of non-negative integers nums, you are initially positioned at the first index.
# Each element represents the maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

# Example:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: Minimum number of jumps to reach the last index is 2: 
# Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""

from typing import List


class JumpGameII:
    def jump_greedy(self, nums: List[int]) -> int:
        """
        Greedy approach using current and maximum reach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        jumps = 0
        current_max_reach = 0
        next_max_reach = 0

        for i in range(len(nums) - 1):
            next_max_reach = max(next_max_reach, i + nums[i])

            if i == current_max_reach:
                jumps += 1
                current_max_reach = next_max_reach

        return jumps

    def jump_dp(self, nums: List[int]) -> int:
        """
        Dynamic Programming approach
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0

        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

        return dp[n - 1]

    def jump_bfs(self, nums: List[int]) -> int:
        """
        BFS-like approach treating array as a graph
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(nums) <= 1:
            return 0

        level = 0
        current_max = 0
        next_max = 0
        i = 0

        while current_max - i + 1 > 0:
            level += 1
            while i <= current_max:
                next_max = max(next_max, nums[i] + i)
                if next_max >= len(nums) - 1:
                    return level
                i += 1
            current_max = next_max

        return 0


def main():
    test_cases = [
        {"nums": [2, 3, 1, 1, 4], "expected": 2},
        {"nums": [2, 3, 0, 1, 4], "expected": 2},
        {"nums": [1, 2, 3], "expected": 2},
        {"nums": [1], "expected": 0},
    ]

    solution = JumpGameII()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Input: {test['nums']}")
        result_greedy = solution.jump_greedy(test["nums"])
        result_dp = solution.jump_dp(test["nums"])
        result_bfs = solution.jump_bfs(test["nums"])
        print(f"Greedy Result: {result_greedy}")
        print(f"DP Result: {result_dp}")
        print(f"BFS Result: {result_bfs}")
        print(f"Expected: {test['expected']}")
        assert (
            result_greedy == result_dp == result_bfs == test["expected"]
        ), f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
