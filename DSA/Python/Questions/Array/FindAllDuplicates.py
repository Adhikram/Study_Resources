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
        """
        Original solution using sign flipping technique.
        Time: O(n), Space: O(1) excluding output list
        """
        result = []

        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                result.append(abs(num))
            else:
                nums[index] = -nums[index]

        return result
    
    def find_duplicates_hashset(self, nums: List[int]) -> List[int]:
        """
        Solution using a hash set to track seen numbers.
        Time: O(n), Space: O(n)
        """
        seen = set()
        result = []
        
        for num in nums:
            if num in seen:
                result.append(num)
            else:
                seen.add(num)
                
        return result
    
    def find_duplicates_count_array(self, nums: List[int]) -> List[int]:
        """
        Solution using a count array.
        Time: O(n), Space: O(n)
        """
        n = len(nums)
        counts = [0] * (n + 1)
        result = []
        
        for num in nums:
            counts[num] += 1
            
        for i in range(1, n + 1):
            if counts[i] == 2:
                result.append(i)
                
        return result
    
    def find_duplicates_sort(self, nums: List[int]) -> List[int]:
        """
        Solution using sorting.
        Time: O(n log n), Space: O(1) or O(n) depending on sorting algorithm
        """
        nums = sorted(nums)  # Create a copy to avoid modifying input
        result = []
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                result.append(nums[i])
                
        return result
    
    def find_duplicates_cyclic_sort(self, nums: List[int]) -> List[int]:
        """
        Solution using cyclic sort.
        Time: O(n), Space: O(1) excluding output list
        """
        i = 0
        while i < len(nums):
            correct_idx = nums[i] - 1
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
                
        result = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(nums[i])
                
        return result


def main():
    solution = FindAllDuplicates()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    
    # Test all solutions
    print(f"Input array: {nums}")
    
    # Original solution
    nums_copy = nums.copy()
    result = solution.find_duplicates(nums_copy)
    print(f"Original solution: {result}")  # Expected output: [2, 3]
    
    # Hash set solution
    result = solution.find_duplicates_hashset(nums)
    print(f"Hash set solution: {result}")
    
    # Count array solution
    result = solution.find_duplicates_count_array(nums)
    print(f"Count array solution: {result}")
    
    # Sorting solution
    result = solution.find_duplicates_sort(nums)
    print(f"Sorting solution: {result}")
    
    # Cyclic sort solution
    nums_copy = nums.copy()
    result = solution.find_duplicates_cyclic_sort(nums_copy)
    print(f"Cyclic sort solution: {result}")


if __name__ == "__main__":
    main()
