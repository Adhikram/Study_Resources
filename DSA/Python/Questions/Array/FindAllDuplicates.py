"""
# Question: Find All Duplicates in an Array
# Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/

# Given an integer array nums of length n where:
# - All integers are in range [1, n]
# - Each integer appears once or twice
# Return an array of all integers that appear twice

# Time Complexity: O(n) where n is the length of input array
# Space Complexity: O(1) excluding the space for output list

# Algorithm:
# 1. Traverse the array once
# 2. For each number x, mark the number at index |x|-1 as negative
# 3. If we find a number that's already negative, x is a duplicate
# 4. This works because array values are in range [1, n]

# Key insight:
# - Use array elements as indices
# - Use sign of numbers to mark presence
# - No extra space needed except for output
"""

from typing import List


class FindAllDuplicates:
    def find_duplicates(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                result.append(abs(num))
            else:
                nums[index] = -nums[index]

        return result


def main():
    solution = FindAllDuplicates()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    result = solution.find_duplicates(nums)
    print(f"Input array: {nums}")
    print(f"Duplicates found: {result}")  # Expected output: [2, 3]


if __name__ == "__main__":
    main()
