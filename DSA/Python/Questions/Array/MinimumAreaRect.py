"""
# Question: Minimum Area Rectangle
# Link: https://leetcode.com/problems/minimum-area-rectangle/

# Given points in X-Y plane, find minimum area of rectangle with sides parallel to axes.
# Return 0 if no such rectangle exists.

# Time Complexity: O(n^3) where n is number of points
# Space Complexity: O(n) for storing point set

# Algorithm:
# 1. Convert points to set for O(1) lookup
# 2. Check all possible triplets of points
# 3. Verify if fourth point exists to form rectangle
# 4. Calculate and track minimum area

# Key Components:
# - min_area_free_rect(): Main function implementing area calculation
# - Point set for efficient lookup
# - Perpendicular check using dot product
"""

from typing import List
import math


class MinimumAreaRect:
    def min_area_free_rect(self, points: List[List[int]]) -> float:
        n = len(points)
        area = float("inf")
        point_set = {f"{x},{y}" for x, y in points}

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Check if points form perpendicular edges
                    dx1 = points[k][0] - points[i][0]
                    dy1 = points[k][1] - points[i][1]
                    dx2 = points[j][0] - points[i][0]
                    dy2 = points[j][1] - points[i][1]

                    # Dot product check for perpendicular edges
                    if dy1 * dy2 + dx1 * dx2 == 0:
                        xl = points[j][0] + dx1
                        yl = points[j][1] + dy1

                        if f"{xl},{yl}" in point_set:
                            edge1 = math.sqrt(dx1 * dx1 + dy1 * dy1)
                            edge2 = math.sqrt(dx2 * dx2 + dy2 * dy2)
                            current_area = edge1 * edge2
                            area = min(area, current_area)

        return 0 if area == float("inf") else area


def main():
    solution = MinimumAreaRect()
    points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
    result = solution.min_area_free_rect(points)
    print(result)  # Expected output: 4.0


if __name__ == "__main__":
    main()
