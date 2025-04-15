"""
# Question: Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Given a sorted array, remove duplicates in-place and return new length

# Time Complexity: O(n) where n is length of array
# Space Complexity: O(1) as we modify array in-place

# Algorithm:
# 1. Use two pointers: start and result
# 2. Track previous element to identify duplicates
# 3. Swap elements when non-duplicate found
# 4. Return length of unique elements

# Key Components:
# - remove_duplicates(): Main function implementing in-place removal
# - Two-pointer technique with previous element tracking
"""

from typing import List


class RemoveDuplicate:
    def remove_duplicates(self, nums: List[int]) -> int:
        start = result = 0
        prev = float("inf")
        n = len(nums)

        while start < n:
            if nums[start] != prev:
                prev = nums[start]
                nums[start], nums[result] = nums[result], nums[start]
                result += 1
            start += 1

        return result
    def removeDuplicatesOP(self, nums: List[int]) -> int:
        start = 1
        index = 0
        n = len(nums)
        while start < n :
            if nums[start] != nums[index]:
                nums[index + 1] = nums[start]
                index += 1
            start += 1
        return index + 1


def main():
    solution = RemoveDuplicate()
    nums = [1, 1, 2]
    result = solution.remove_duplicates(nums)
    print(f"Length after removing duplicates: {result}")
    print(f"Array after removing duplicates: {nums[:result]}")
    nums = [1, 1, 2]
    print(f"Length after removing duplicates: {solution.removeDuplicatesOP(nums)}")
    print(f"Array after removing duplicates: {nums[:result]}")

if __name__ == "__main__":
    main()
