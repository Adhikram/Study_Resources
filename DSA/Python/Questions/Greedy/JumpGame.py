"""
# Question: Jump Game
# Link: https://leetcode.com/problems/jump-game/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Track maximum reachable position
# 2. Iterate through array
# 3. Update max reach at each position
# 4. Check if target is reachable
"""


class JumpGame:
    def can_jump(self, nums: list[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])

        return True


def main():
    solution = JumpGame()
    nums = [2, 3, 1, 1, 4]
    print(solution.can_jump(nums))  # Expected: True

    nums = [3, 2, 1, 0, 4]
    print(solution.can_jump(nums))  # Expected: False


if __name__ == "__main__":
    main()
