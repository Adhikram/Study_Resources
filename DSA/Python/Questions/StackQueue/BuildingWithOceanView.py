"""
# Question: Buildings With an Ocean View
# Link: https://leetcode.com/problems/buildings-with-an-ocean-view/

# Find buildings that have an ocean view

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Traverse buildings from right to left
# 2. Track maximum height seen
# 3. Record buildings with ocean view
# 4. Return indices in increasing order

# Key Components:
# - find_buildings(): Main implementation
# - Maximum height tracking
# - Result array optimization
"""


class BuildingWithOceanView:
    def find_buildings(self, heights: list[int]) -> list[int]:
        length = len(heights)
        idx = length - 1
        max_height = heights[idx]
        heights[idx] = idx
        idx -= 1

        for i in range(length - 2, -1, -1):
            if heights[i] > max_height:
                max_height = heights[i]
                heights[idx] = i
                idx -= 1

        return heights[idx + 1 : length]


def main():
    solution = BuildingWithOceanView()
    print(solution.find_buildings([4, 2, 3, 1]))  # Expected: [0, 2, 3]
    print(solution.find_buildings([4, 3, 2, 1]))  # Expected: [0, 1, 2, 3]
    print(solution.find_buildings([1, 3, 2, 4]))  # Expected: [3]


if __name__ == "__main__":
    main()
