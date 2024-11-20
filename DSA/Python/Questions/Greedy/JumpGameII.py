"""
# Question: Jump Game II
# Link: https://leetcode.com/problems/jump-game-ii/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Track current reach and max reach
# 2. Count minimum jumps needed
# 3. Update reach boundaries
# 4. Return minimum jumps
"""


class JumpGameII:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        current_max_reach = 0
        next_max_reach = 0

        for i in range(len(nums) - 1):
            next_max_reach = max(next_max_reach, i + nums[i])

            if i == current_max_reach:
                jumps += 1
                current_max_reach = next_max_reach

        return jumps


def main():
    solution = JumpGameII()
    nums = [2, 3, 1, 1, 4]
    print(solution.jump(nums))  # Expected: 2

    nums = [2, 3, 0, 1, 4]
    print(solution.jump(nums))  # Expected: 2


if __name__ == "__main__":
    main()
