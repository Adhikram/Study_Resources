"""
# Question: Find Median from Data Stream
# Link: https://leetcode.com/problems/find-median-from-data-stream/

# Problem Statement:
# Implement the MedianFinder class:
# - MedianFinder() initializes the MedianFinder object.
# - void addNum(int num) adds the integer num from the data stream to the data structure.
# - double findMedian() returns the median of all elements so far.

# Example:
# Input:
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output:
# [null, null, null, 1.5, null, 2.0]
"""

import heapq
from typing import List


class MedianFinder:
    def __init__(self):
        """
        Initialize data structure:
        - max_heap for the left half (smaller numbers)
        - min_heap for the right half (larger numbers)
        """
        self.max_heap = []  # stores negatives of numbers for max heap behavior
        self.min_heap = []  # stores numbers as is

    def add_num(self, num: int) -> None:
        """
        Add a number to the data structure while maintaining balance
        Time Complexity: O(log n)
        """
        # If number belongs to left half
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Rebalance heaps if necessary
        self._rebalance_heaps()

    def _rebalance_heaps(self) -> None:
        """
        Helper method to ensure heaps remain balanced:
        - Left heap can have at most one more element than right heap
        - Right heap cannot have more elements than left heap
        """
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self) -> float:
        """
        Returns the median of current data stream
        Time Complexity: O(1)
        """
        if not self.max_heap:
            return 0

        # If odd number of elements
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])

        # If even number of elements
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0


def main():
    test_cases = [
        {
            "operations": [
                "MedianFinder",
                "addNum",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
            ],
            "values": [[], [1], [2], [], [3], []],
            "expected": [None, None, None, 1.5, None, 2.0],
        },
        {
            "operations": [
                "MedianFinder",
                "addNum",
                "findMedian",
                "addNum",
                "findMedian",
            ],
            "values": [[], [1], [], [2], []],
            "expected": [None, None, 1.0, None, 1.5],
        },
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        median_finder = MedianFinder()
        results = []

        for op, val in zip(test["operations"], test["values"]):
            if op == "MedianFinder":
                results.append(None)
            elif op == "addNum":
                median_finder.add_num(val[0])
                results.append(None)
            else:
                results.append(median_finder.find_median())

        print(f"Expected: {test['expected']}")
        print(f"Results:  {results}")


if __name__ == "__main__":
    main()
