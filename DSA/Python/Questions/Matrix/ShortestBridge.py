"""
# Question: Shortest Bridge
# Link: https://leetcode.com/problems/shortest-bridge/

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

# Algorithm:
# 1. Find first island using DFS
# 2. Use BFS to expand and find second island
# 3. Track minimum distance
# 4. Return shortest bridge length
"""

from collections import deque


class ShortestBridge:
    def shortest_bridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        queue = deque()
        found = False

        # DFS to find first island
        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = 2
            queue.append((i, j))
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                dfs(ni, nj)

        # Find first 1 and mark first island
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        # BFS to find shortest bridge
        distance = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= ni < n and 0 <= nj < n:
                        if grid[ni][nj] == 1:
                            return distance
                        elif grid[ni][nj] == 0:
                            grid[ni][nj] = 2
                            queue.append((ni, nj))
            distance += 1

        return distance


def main():
    solution = ShortestBridge()
    grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    print(solution.shortest_bridge(grid))  # Expected: 2


if __name__ == "__main__":
    main()
