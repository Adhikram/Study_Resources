"""
# Question: Trapping Rain Water
# Link: https://leetcode.com/problems/trapping-rain-water/

# Calculate how much water can be trapped between buildings

# Time Complexity: O(n) using two pointers
# Space Complexity: O(1)

# Algorithm:
# 1. Use two pointers (left and right)
# 2. Track maximum height from both sides
# 3. Add water based on smaller height boundary
# 4. Move pointers based on height comparison

# Key Components:
# - trap(): Main function implementing water trapping calculation
# - Two-pointer technique with max height tracking
# - Dynamic boundary updates
"""

from typing import List


class TrapRainWater:
    def trap(self, height: List[int]) -> int:
        l_max = float("-inf")
        r_max = float("-inf")
        left = 0
        right = len(height) - 1
        result = 0

        while left <= right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])

            if l_max < r_max:
                result += l_max - height[left]
                left += 1
            else:
                result += r_max - height[right]
                right -= 1

        return result


def main():
    solution = TrapRainWater()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = solution.trap(height)
    print(result)  # Expected output: 6


if __name__ == "__main__":
    main()
