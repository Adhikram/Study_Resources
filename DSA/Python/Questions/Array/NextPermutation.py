"""
# Question: Next Permutation
# Link: https://leetcode.com/problems/next-permutation/

# Find the next lexicographically greater permutation of numbers

# Time Complexity: O(n)
# Space Complexity: O(1) as we modify array in-place

# Algorithm:
# 1. Find first decreasing element from right (break1)
# 2. Find next greater element than break1 from right (break2)
# 3. Swap elements at break1 and break2
# 4. Reverse array from break1+1 to end

# Key Components:
# - next_permutation(): Main function implementing the algorithm
# - Two-pass scan approach
# - In-place reversal
"""

from typing import List


class NextPermutation:
    def next_permutation(self, nums: List[int]) -> None:
        n = len(nums)
        break1 = break2 = -1

        # Find break1: first decreasing element from right
        for idx in range(n - 1, 0, -1):
            if nums[idx - 1] < nums[idx]:
                break1 = idx - 1
                break

        # If no break1, array is reverse sorted
        if break1 == -1:
            nums.sort()
            return

        # Find break2: next greater element than break1
        for idx in range(n - 1, 0, -1):
            if nums[break1] < nums[idx]:
                break2 = idx
                break

        # Swap elements at break1 and break2
        nums[break1], nums[break2] = nums[break2], nums[break1]

        # Reverse array from break1+1 to end
        left = break1 + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


def main():
    solution = NextPermutation()
    nums = [1, 2, 3, 4, 6, 5, 4, 3]
    print(f"Original array: {nums}")
    solution.next_permutation(nums)
    print(f"Next permutation: {nums}")


if __name__ == "__main__":
    main()
