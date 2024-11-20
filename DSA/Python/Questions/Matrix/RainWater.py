"""
# Question: Trapping Rain Water II
# Link: https://leetcode.com/problems/trapping-rain-water-ii/

# Time Complexity: O(m*n*log(m*n))
# Space Complexity: O(m*n)

# Algorithm:
# 1. Use min heap to track boundary cells
# 2. Process cells from outside to inside
# 3. Track water level and trapped water
# 4. Return total trapped water
"""

from heapq import heappush, heappop


class RainWater:
    def trap_rain_water(self, height_map: list[list[int]]) -> int:
        if not height_map or not height_map[0]:
            return 0

        m, n = len(height_map), len(height_map[0])
        heap = []
        visited = [[False] * n for _ in range(m)]

        # Add border cells to heap
        for i in range(m):
            heappush(heap, (height_map[i][0], i, 0))
            heappush(heap, (height_map[i][n - 1], i, n - 1))
            visited[i][0] = visited[i][n - 1] = True

        for j in range(1, n - 1):
            heappush(heap, (height_map[0][j], 0, j))
            heappush(heap, (height_map[m - 1][j], m - 1, j))
            visited[0][j] = visited[m - 1][j] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        water = 0
        max_height = 0

        while heap:
            height, i, j = heappop(heap)
            max_height = max(max_height, height)

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    visited[ni][nj] = True
                    water += max(0, max_height - height_map[ni][nj])
                    heappush(heap, (height_map[ni][nj], ni, nj))

        return water


def main():
    solution = RainWater()
    height_map = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
    print(solution.trap_rain_water(height_map))  # Expected: 4


if __name__ == "__main__":
    main()
