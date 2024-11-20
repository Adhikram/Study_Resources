"""
# Question: Rectangle Intersections
# Count intersection points between rectangles and grid lines

# Time Complexity: O(n * (lx + ly)) where n is number of rectangles, 
# lx and ly are number of lines
# Space Complexity: O(1)

# Algorithm:
# 1. Define Rectangle class to store coordinates
# 2. Check intersections with X-axis parallel lines
# 3. Check intersections with Y-axis parallel lines
# 4. Count total intersections

# Key Components:
# - Rectangle class for coordinate storage
# - count_intersection_points(): Main counting function
# - Separate X and Y axis intersection checks
"""

from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class Rectangle:
    bottom_left: Tuple[int, int]
    top_right: Tuple[int, int]


class RectangleIntersections:
    def count_intersection_points(
        self, lines_x: List[int], lines_y: List[int], rectangles: List[Rectangle]
    ) -> int:
        intersection_count = 0

        # Check X-axis parallel lines
        for line_x in lines_x:
            for rectangle in rectangles:
                if rectangle.bottom_left[1] <= line_x <= rectangle.top_right[1]:
                    intersection_count += 1

        # Check Y-axis parallel lines
        for line_y in lines_y:
            for rectangle in rectangles:
                if rectangle.bottom_left[0] <= line_y <= rectangle.top_right[0]:
                    intersection_count += 1

        return intersection_count


def main():
    lines_x = [1, 2, 4, 19]
    lines_y = [2, 5, 9]
    rectangles = [Rectangle((1, 3), (3, 6))]

    solution = RectangleIntersections()
    result = solution.count_intersection_points(lines_x, lines_y, rectangles)
    print(f"Total intersection points: {result}")


if __name__ == "__main__":
    main()
