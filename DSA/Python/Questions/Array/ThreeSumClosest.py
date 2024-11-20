"""
# Question: Three Sum Closest
# Link: https://leetcode.com/problems/3sum-closest/

# Find three integers that sum closest to target value

# Time Complexity: O(n^2) using sorting and two pointers
# Space Complexity: O(1)

# Algorithm:
# 1. Sort array for efficient two-pointer approach
# 2. Fix first element and find pairs for remaining sum
# 3. Use two pointers to minimize difference with target
# 4. Track closest sum throughout iteration

# Key Components:
# - three_sum_closest(): Main function implementing closest sum finding
# - Two-pointer technique with difference tracking
# - Early termination on exact match
"""

from typing import List


class ThreeSumClosest:
    def three_sum_closest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1

            while start < end:
                current_sum = nums[i] + nums[start] + nums[end]

                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                if current_sum < target:
                    start += 1
                else:
                    end -= 1

        return closest_sum


def main():
    solution = ThreeSumClosest()
    nums = [1, 2, 4, 8, 16, 32, 64, 128]
    target = 82
    result = solution.three_sum_closest(nums, target)
    print(result)


if __name__ == "__main__":
    main()
