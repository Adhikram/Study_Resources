"""
# Question: Find the Duplicate Number
# Link: https://leetcode.com/problems/find-the-duplicate-number/

# Given an array of n + 1 integers where each integer is in range [1, n]:
# - Find the one repeated number
# - Must solve without modifying array
# - Must use only constant extra space
# - Array contains only one repeated number

# Time Complexity: O(n) where n is the length of array
# Space Complexity: O(1)

# Algorithm (Floyd's Tortoise and Hare):
# 1. Initialize slow and fast pointers at first element
# 2. Move slow one step, fast two steps until they meet
# 3. Reset slow to start, keep fast at meeting point
# 4. Move both one step until they meet again
# 5. Meeting point is the duplicate number

# Example:
# Input: [1,3,4,2,2]
# Output: 2
"""

from typing import List


class FindDuplicated:
    def find_duplicate(self, nums: List[int]) -> int:
        # Phase 1: Find intersection point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find entrance to cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


def main():
    solution = FindDuplicated()
    nums = [1, 3, 4, 2, 2]
    result = solution.find_duplicate(nums)
    print(f"Input array: {nums}")
    print(f"Duplicate number: {result}")  # Expected output: 2


if __name__ == "__main__":
    main()
