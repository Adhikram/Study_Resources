"""
# Question: Kth Largest Element in an Array
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

# Given an integer array nums and an integer k, return the kth largest element.
# Note: It is the kth largest element in sorted order, not the kth distinct element.

# Two Solution Approaches:
# 1. QuickSelect:
#    Time Complexity: O(n) average case
#    Space Complexity: O(1) for in-place partitioning
# 2. Min-Heap:
#    Time Complexity: O(n log k)
#    Space Complexity: O(k)

# Key Components:
# - quick_select(): Implements QuickSelect algorithm with random pivot
# - find_kth_largest(): Implements min-heap solution
# - partition(): Helper function for QuickSelect
"""

from typing import List
import random
import heapq


class KthLargestElement:
    def quick_select(self, nums: List[int], k: int, left: int, right: int) -> int:
        if left == right:
            return nums[left]

        pivot_index = left + random.randint(0, right - left)
        pivot_index = self.partition(nums, left, right, pivot_index)

        if k == pivot_index:
            return nums[k]
        elif k < pivot_index:
            return self.quick_select(nums, k, left, pivot_index - 1)
        else:
            return self.quick_select(nums, k, pivot_index + 1, right)

    def partition(
        self, nums: List[int], left: int, right: int, pivot_index: int
    ) -> int:
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    def find_kth_largest(self, nums: List[int], k: int) -> int:
        # Min-heap approach
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
    quick_select_result = solution.quick_select(
        nums.copy(), len(nums) - k, 0, len(nums) - 1
    )

    print(f"Heap approach result: {heap_result}")
    print(f"QuickSelect approach result: {quick_select_result}")


if __name__ == "__main__":
    main()
