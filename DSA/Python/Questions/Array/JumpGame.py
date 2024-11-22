"""
# Question: Jump Game
# Link: https://leetcode.com/problems/jump-game/

# Problem Statement:
# Given an array of non-negative integers nums, you are initially positioned at the first index.
# Each element represents the maximum jump length at that position.
# Determine if you can reach the last index.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0.
"""

from typing import List


class JumpGame:
    def can_jump_greedy(self, nums: List[int]) -> bool:
        """
        Greedy approach tracking maximum reachable position
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])

        return True

    def can_jump_dp(self, nums: List[int]) -> bool:
        """
        Dynamic Programming approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = True
                if i + j >= n - 1:
                    return True

        return dp[n - 1]

    def can_jump_backward(self, nums: List[int]) -> bool:
        """
        Backward traversal approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        last_pos = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i

        return last_pos == 0


def main():
    test_cases = [
        {"nums": [2, 3, 1, 1, 4], "expected": True},
        {"nums": [3, 2, 1, 0, 4], "expected": False},
        {"nums": [0], "expected": True},
        {"nums": [2, 0, 0], "expected": True},
    ]

    solution = JumpGame()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Input: {test['nums']}")
        result_greedy = solution.can_jump_greedy(test["nums"])
        result_dp = solution.can_jump_dp(test["nums"])
        result_backward = solution.can_jump_backward(test["nums"])
        print(f"Greedy Result: {result_greedy}")
        print(f"DP Result: {result_dp}")
        print(f"Backward Result: {result_backward}")
        print(f"Expected: {test['expected']}")
        assert (
            result_greedy == result_dp == result_backward == test["expected"]
        ), f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
