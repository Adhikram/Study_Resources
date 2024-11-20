"""
# Question: Find Median from Data Stream
# Link: https://leetcode.com/problems/find-median-from-data-stream/

# Track median of numbers in a data stream

# Time Complexity: 
# - addNum: O(log n)
# - findMedian: O(1)
# Space Complexity: O(n)

# Algorithm:
# 1. Use two heaps: maxHeap for left half, minHeap for right half
# 2. Balance heaps after each insertion
# 3. Calculate median from heap tops
# 4. Maintain size difference ≤ 1

# Key Components:
# - MedianFinder class with heap implementation
# - add_num(): Number insertion logic
# - find_median(): Median calculation
"""

import heapq


class MedianFinder:
    def __init__(self):
        self.max_heap = []  # left half
        self.min_heap = []  # right half

    def add_num(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Balance heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self) -> float:
        if not self.max_heap:
            return 0

        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]


def main():
    median_finder = MedianFinder()
    median_finder.add_num(1)
    median_finder.add_num(2)
    print(median_finder.find_median())  # 1.5
    median_finder.add_num(3)
    print(median_finder.find_median())  # 2.0


if __name__ == "__main__":
    main()
