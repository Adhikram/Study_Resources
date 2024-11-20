"""
# Question: Three Sum
# Link: https://leetcode.com/problems/3sum/

# Find all unique triplets in array that sum to zero

# Time Complexity: O(n^2) using sorting and two pointers
# Space Complexity: O(1) excluding output space

# Algorithm:
# 1. Sort array for efficient two-pointer approach
# 2. Fix first element and find pairs for remaining sum
# 3. Use two pointers for remaining elements
# 4. Skip duplicates to avoid duplicate triplets

# Key Components:
# - three_sum(): Main function implementing triplet finding
# - Two-pointer technique with duplicate handling
# - Sorted array traversal
"""

from typing import List


class ThreeSum:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicates for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            target = -nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result


def main():
    solution = ThreeSum()
    nums = [-1, 0, 1, 2, -1, -4]
    result = solution.three_sum(nums)
    print(result)  # Expected output: [[-1, -1, 2], [-1, 0, 1]]


if __name__ == "__main__":
    main()
