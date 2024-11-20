"""
# Question: K Closest Points to Origin
# Link: https://leetcode.com/problems/k-closest-points-to-origin/

# Find k points closest to origin using heap

# Time Complexity: O(nlogk)
# Space Complexity: O(k)

# Algorithm:
# 1. Use max heap to maintain k closest points
# 2. Calculate distance from origin
# 3. Keep heap size at k
# 4. Return k closest points

# Key Components:
# - k_closest(): Main implementation
# - Distance calculation using Euclidean distance
# - Priority queue (heap) management
"""

import heapq
from typing import List
import math


class KClosestPoints:
    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            distance = -math.sqrt(point[0] * point[0] + point[1] * point[1])
            heapq.heappush(heap, (distance, point))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1

        return result


def main():
    solution = KClosestPoints()
    points = [[1, 3], [-2, 2]]
    k = 1
    result = solution.k_closest(points, k)
    for point in result:
        print(f"{point[0]} {point[1]}")


if __name__ == "__main__":
    main()
