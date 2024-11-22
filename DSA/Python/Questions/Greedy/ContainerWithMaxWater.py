"""
# Question: Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/

# Problem Statement:
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
# Find two lines, which, together with the x-axis forms a container that contains the most water.

# Example:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The maximum area is obtained by choosing height[1] = 8 and height[8] = 7
"""

from typing import List


class ContainerWithMaxWater:
    def max_area_two_pointer(self, height: List[int]) -> int:
        """
        Two pointer approach to find maximum water container
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            # Calculate current area
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)

            # Move pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

    def max_area_optimized(self, height: List[int]) -> int:
        """
        Optimized approach with early termination conditions
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_area = 0
        left, right = 0, len(height) - 1
        max_height = max(height)

        while left < right:
            # Early termination if remaining area cannot exceed max_area
            if (right - left) * max_height <= max_area:
                break

            # Calculate current area
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)

            # Skip elements that cannot contribute to a larger area
            if height[left] < height[right]:
                curr_height = height[left]
                while left < right and height[left] <= curr_height:
                    left += 1
            else:
                curr_height = height[right]
                while left < right and height[right] <= curr_height:
                    right -= 1

        return max_area


def main():
    test_cases = [
        {"height": [1, 8, 6, 2, 5, 4, 8, 3, 7], "expected": 49},
        {"height": [1, 1], "expected": 1},
        {"height": [4, 3, 2, 1, 4], "expected": 16},
        {"height": [1, 2, 4, 3], "expected": 4},
    ]

    solution = ContainerWithMaxWater()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Height Array: {test['height']}")
        result_two_pointer = solution.max_area_two_pointer(test["height"])
        result_optimized = solution.max_area_optimized(test["height"])
        print(f"Two Pointer Result: {result_two_pointer}")
        print(f"Optimized Result: {result_optimized}")
        print(f"Expected: {test['expected']}")
        assert (
            result_two_pointer == result_optimized == test["expected"]
        ), f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
