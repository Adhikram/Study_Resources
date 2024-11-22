"""
# Question: K Closest Points to Origin
# Link: https://leetcode.com/problems/k-closest-points-to-origin/

# Problem Statement:
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
# and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points is the Euclidean distance: sqrt((x1 - x2)² + (y1 - y2)²).

# Example:
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation: The distance between (-2, 2) and origin is sqrt(8).
# The distance between (1, 3) and origin is sqrt(10).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
"""

from typing import List
import heapq
import math


class KClosestPoints:
    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Find k closest points to origin using max heap
        Time Complexity: O(n log k)
        Space Complexity: O(k)
        """
        # Max heap to maintain k closest points
        heap = []

        for point in points:
            # Calculate negative distance for max heap behavior
            distance = -(point[0] * point[0] + point[1] * point[1])

            # Add point to heap
            heapq.heappush(heap, (distance, point))

            # Keep heap size as k
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract k closest points
        return [point for _, point in heap]

    def k_closest_quick_select(
        self, points: List[List[int]], k: int
    ) -> List[List[int]]:
        """
        Alternative solution using QuickSelect algorithm
        Time Complexity: O(n) average case
        Space Complexity: O(1)
        """

        def distance(point: List[int]) -> int:
            return point[0] * point[0] + point[1] * point[1]

        def partition(left: int, right: int) -> int:
            pivot_dist = distance(points[right])
            store_idx = left

            for i in range(left, right):
                if distance(points[i]) <= pivot_dist:
                    points[store_idx], points[i] = points[i], points[store_idx]
                    store_idx += 1

            points[right], points[store_idx] = points[store_idx], points[right]
            return store_idx

        left, right = 0, len(points) - 1
        while left <= right:
            pivot_idx = partition(left, right)
            if pivot_idx == k:
                return points[:k]
            elif pivot_idx < k:
                left = pivot_idx + 1
            else:
                right = pivot_idx - 1

        return points[:k]


def main():
    test_cases = [
        {"points": [[1, 3], [-2, 2]], "k": 1, "expected": [[-2, 2]]},
        {"points": [[3, 3], [5, -1], [-2, 4]], "k": 2, "expected": [[3, 3], [-2, 4]]},
    ]

    solution = KClosestPoints()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Points: {test['points']}, k: {test['k']}")
        heap_result = solution.k_closest(test["points"], test["k"])
        quick_select_result = solution.k_closest_quick_select(
            test["points"].copy(), test["k"]
        )
        print(f"Heap Result: {heap_result}")
        print(f"QuickSelect Result: {quick_select_result}")


if __name__ == "__main__":
    main()
