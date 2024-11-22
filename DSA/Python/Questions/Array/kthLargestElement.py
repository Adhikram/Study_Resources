"""
# Question: Kth Largest Element in an Array
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

# Problem Statement:
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in sorted order, not the kth distinct element.

# Example:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Solution Approaches:
# 1. QuickSelect:
#    - Time Complexity: O(n) average case
#    - Space Complexity: O(1) for in-place partitioning
# 2. Min-Heap:
#    - Time Complexity: O(n log k)
#    - Space Complexity: O(k)

# Key Components:
# - quick_select(): Implements QuickSelect algorithm with random pivot
# - find_kth_largest(): Implements min-heap solution
# - partition(): Helper function for QuickSelect
"""

from typing import List
import random
import heapq


class KthLargestElement:
    def quick_select(self, nums: List[int], k: int) -> int:
        """
        QuickSelect algorithm to find the kth largest element.
        """
        pivot = random.choice(nums)
        left, right, mid = [], [], []
        for num in nums:
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)
            else:
                mid.append(num)

        if len(left) >= k:
            return self.quick_select(left, k)
        elif k > len(left) + len(mid):
            return self.quick_select(right, k - len(left) - len(mid))
        else:
            return pivot

    def find_kth_largest(self, nums: List[int], k: int) -> int:
        """
        Min-heap approach to find the kth largest element.
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


def main():
    solution = KthLargestElement()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    # Test both approaches
    heap_result = solution.find_kth_largest(nums, k)
    quick_select_result = solution.quick_select(nums.copy(), k)

    print(f"Heap approach result: {heap_result}")
    print(f"QuickSelect approach result: {quick_select_result}")


if __name__ == "__main__":
    main()
