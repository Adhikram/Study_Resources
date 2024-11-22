"""
# Question: Find K Closest Elements
# Link: https://leetcode.com/problems/find-k-closest-elements/

# Problem Statement:
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
# The result should also be sorted in ascending order.

# Example:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Explanation: The 4 closest elements to 3 are [1,2,3,4]
"""

from typing import List
import heapq


class FindKClosestElement:
    def find_closest_binary_search(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Binary search approach to find starting position
        Time Complexity: O(log(n-k))
        Space Complexity: O(1)
        """
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) >> 1
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left : left + k]

    def find_closest_heap(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Heap-based approach using absolute differences
        Time Complexity: O(nlogk)
        Space Complexity: O(k)
        """
        heap = []
        for num in arr:
            diff = abs(num - x)
            heapq.heappush(heap, (-diff, -num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = [-pair[1] for pair in heap]
        return sorted(result)

    def find_closest_two_pointer(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Two pointer approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = 0
        right = len(arr) - 1

        while right - left >= k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1

        return arr[left : right + 1]


def main():
    test_cases = [
        {"arr": [1, 2, 3, 4, 5], "k": 4, "x": 3, "expected": [1, 2, 3, 4]},
        {"arr": [1, 2, 3, 4, 5], "k": 4, "x": -1, "expected": [1, 2, 3, 4]},
        {"arr": [1, 1, 1, 10, 10, 10], "k": 1, "x": 9, "expected": [10]},
    ]

    solution = FindKClosestElement()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Array: {test['arr']}")
        print(f"k: {test['k']}, x: {test['x']}")

        result_binary = solution.find_closest_binary_search(
            test["arr"], test["k"], test["x"]
        )
        result_heap = solution.find_closest_heap(test["arr"], test["k"], test["x"])
        result_two_pointer = solution.find_closest_two_pointer(
            test["arr"], test["k"], test["x"]
        )

        print(f"Binary Search Result: {result_binary}")
        print(f"Heap Result: {result_heap}")
        print(f"Two Pointer Result: {result_two_pointer}")
        print(f"Expected: {test['expected']}")

        assert result_binary == result_heap == result_two_pointer == test["expected"]


if __name__ == "__main__":
    main()
