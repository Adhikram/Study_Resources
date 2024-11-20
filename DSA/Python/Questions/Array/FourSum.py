"""
# Question: Four Sum
# Link: https://leetcode.com/problems/4sum/

# Given an array nums of n integers, return all unique quadruplets that sum to target.
# Each quadruplet [nums[a], nums[b], nums[c], nums[d]] must have distinct indices.

# Time Complexity: O(n^3) - two nested loops and two pointers for each pair
# Space Complexity: O(1) excluding output space

# Algorithm:
# 1. Sort the input array
# 2. Use two nested loops to fix first two numbers
# 3. Use two pointers technique for remaining two numbers
# 4. Skip duplicates at each level to ensure unique quadruplets
# 5. Handle integer overflow using long type conversions

# Key Components:
# - four_sum(): Main function implementing the algorithm
# - Nested loops with two-pointer approach
# - Duplicate handling for all four positions
"""

from typing import List


class FourSum:
    def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)

        # First two nested loops to fix first two numbers
        for i in range(n - 3):
            # Skip duplicates for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicates for second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1
                target_sum = target - nums[i] - nums[j]

                while left < right:
                    current_sum = nums[left] + nums[right]

                    if current_sum == target_sum:
                        # Found a quadruplet
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for third and fourth elements
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif current_sum < target_sum:
                        left += 1
                    else:
                        right -= 1

        return result


def main():
    solution = FourSum()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    result = solution.four_sum(nums, target)
    print(result)  # Expected output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]


if __name__ == "__main__":
    main()
