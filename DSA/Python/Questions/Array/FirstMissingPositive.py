"""
# Question: First Missing Positive
# Link: https://leetcode.com/problems/first-missing-positive/

# Given an unsorted integer array nums, return the smallest positive integer that is not present in nums.
# Must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Time Complexity: O(n) where n is the length of input array
# Space Complexity: O(1) as we modify array in-place

# Algorithm:
# 1. Iterate through array and place each number at its correct position (nums[i] at index nums[i]-1)
# 2. Skip numbers that are negative, greater than array length, or already in correct position
# 3. After rearrangement, iterate through array to find first position where number doesn't match index+1
# 4. That position+1 is our answer, or if all match, return length+1

# Key Components:
# - first_missing_positive(): Main function that processes input array
# - Cyclic sort approach to arrange numbers in their correct positions
"""

from typing import List


class FirstMissingPositive:
    def first_missing_positive(self, nums: List[int]) -> int:
        n = len(nums)
        index = 0

        # Place numbers in their correct positions
        while index < n:
            curr = nums[index] - 1
            if 0 <= curr < n and nums[curr] != nums[index]:
                nums[curr], nums[index] = nums[index], nums[curr]
            else:
                index += 1

        # Find first missing positive number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


def main():
    solution = FirstMissingPositive()
    nums = [3, 4, -1, 1]
    result = solution.first_missing_positive(nums)
    print(result)  # Expected output: 2


if __name__ == "__main__":
    main()
