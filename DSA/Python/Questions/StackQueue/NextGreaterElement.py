"""
# Question: Next Greater Element
# Link: https://leetcode.com/problems/next-greater-element-i/

# Problem Statement:
# Given two distinct arrays nums1 and nums2, where nums1 is a subset of nums2,
# find the next greater element for each element in nums1 within nums2.
# The next greater element is the first greater element to the right in nums2.
# If no greater element exists, return -1 for that element.

# Example:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,3]
# Explanation: 
# - For 4, no greater element exists, so -1
# - For 1, the next greater element is 3
# - For 2, the next greater element is 3
"""

from typing import List
from collections import deque


class NextGreaterElement:
    def find_next_greater(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find next greater elements using monotonic stack
        Time Complexity: O(n) where n is length of nums2
        Space Complexity: O(n) for stack and hashmap
        """
        # Stack to maintain decreasing elements
        stack = deque()
        # Map to store next greater element for each number
        next_greater = {}

        # Process nums2 to find next greater elements
        for num in nums2:
            # Pop elements smaller than current number
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Remaining elements have no greater element
        while stack:
            next_greater[stack.pop()] = -1

        # Build result array for nums1
        return [next_greater[num] for num in nums1]

    def find_next_greater_optimized(
        self, nums1: List[int], nums2: List[int]
    ) -> List[int]:
        """
        Optimized version using single pass and less memory
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        mapping = {}

        # Process nums2 from right to left
        for i , num in enumerate(reversed(nums2)):
            while stack and stack[-1] <= num:
                stack.pop()
            mapping[num] = stack[-1] if stack else -1
            stack.append(num)

        return [mapping[num] for num in nums1]


def main():
    test_cases = [
        {"nums1": [4, 1, 2], "nums2": [1, 3, 4, 2], "expected": [-1, 3, 3]},
        {"nums1": [2, 4], "nums2": [1, 2, 3, 4], "expected": [3, -1]},
        {
            "nums1": [1, 3, 5, 2, 4],
            "nums2": [6, 5, 4, 3, 2, 1, 7],
            "expected": [7, 7, 7, 7, 7],
        },
    ]

    solution = NextGreaterElement()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"nums1: {test['nums1']}")
        print(f"nums2: {test['nums2']}")
        result1 = solution.find_next_greater(test["nums1"], test["nums2"])
        result2 = solution.find_next_greater_optimized(test["nums1"], test["nums2"])
        print(f"Standard Result: {result1}")
        print(f"Optimized Result: {result2}")
        print(f"Expected: {test['expected']}")
        assert result1 == result2 == test["expected"], f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
