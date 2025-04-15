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
        """
        Floyd's Tortoise and Hare (Cycle Detection)
        Time: O(n), Space: O(1)
        Most optimal solution satisfying all constraints
        """
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
    
    def find_duplicate_binary_search(self, nums: List[int]) -> int:
        """
        Binary Search approach
        Time: O(n log n), Space: O(1)
        Satisfies non-modification and constant space constraints
        """
        low, high = 1, len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            count = sum(1 for num in nums if num <= mid)
            
            # If count is greater than mid, duplicate is in the lower half
            if count > mid:
                high = mid
            else:
                low = mid + 1
                
        return low
    
    def find_duplicate_sum(self, nums: List[int]) -> int:
        """
        Sum method approach
        Time: O(n), Space: O(1)
        Optimal solution but with limitation: may overflow with large arrays
        """
        n = len(nums) - 1
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        
        # If there's one duplicate, then actual_sum - expected_sum = duplicate
        # But this only works if the duplicate appears exactly twice
        # For the general case, we need to account for how many times it appears
        
        # First, find how many unique numbers are present
        unique_count = len(set(nums))
        missing_count = n - unique_count + 1
        
        # The duplicate appears (missing_count + 1) times
        duplicate = (actual_sum - expected_sum) // missing_count
        return duplicate


def main():
    solution = FindDuplicated()
    nums = [1, 3, 4, 2, 2]
    
    # Test optimized solutions
    print(f"Input array: {nums}")
    
    # Floyd's Tortoise and Hare (Cycle Detection) - Most optimal
    result = solution.find_duplicate(nums)
    print(f"Floyd's Cycle Detection: {result}")  # Expected output: 2
    
    # Binary Search approach
    result = solution.find_duplicate_binary_search(nums)
    print(f"Binary Search approach: {result}")
    
    # Sum method approach - Optimal but with limitations
    result = solution.find_duplicate_sum(nums)
    print(f"Sum method approach: {result}")


if __name__ == "__main__":
    main()
