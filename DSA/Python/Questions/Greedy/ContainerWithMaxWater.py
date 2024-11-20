"""
# Question: Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Use two pointers approach
# 2. Calculate area between lines
# 3. Move pointer with smaller height
# 4. Track maximum area
"""


class ContainerWithMaxWater:
    def max_area(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

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


def main():
    solution = ContainerWithMaxWater()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.max_area(height))  # Expected: 49


if __name__ == "__main__":
    main()
