"""
# Question: Majority Element
# Link: https://leetcode.com/problems/majority-element/

# Given an array nums of size n, return the majority element that appears more than ⌊n/2⌋ times.
# Uses Boyer-Moore Voting Algorithm for optimal solution.

# Time Complexity: O(n) where n is the length of input array
# Space Complexity: O(1) as we only use two variables

# Algorithm:
# 1. Initialize count=0 and element=first number
# 2. For each number in array:
#    - If current number matches element, increment count
#    - Else decrement count and if count reaches 0, update element
# 3. Return the majority element

# Key Components:
# - majority_element(): Implements Boyer-Moore Voting Algorithm
# - Counter approach to track current candidate and its count
"""

from typing import List


class MajorityElement:
    def majority_element(self, nums: List[int]) -> int:
        count = 0
        elem = nums[0]

        for num in nums:
            if elem == num:
                count += 1
            else:
                count -= 1
                if count <= 0:
                    count = 1
                    elem = num

        return elem


def main():
    solution = MajorityElement()
    nums = [3, 2, 3]
    result = solution.majority_element(nums)
    print(result)  # Expected output: 3


if __name__ == "__main__":
    main()
