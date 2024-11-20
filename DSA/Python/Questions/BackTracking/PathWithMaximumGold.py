"""
# Question: Path with Maximum Gold
# Link: https://leetcode.com/problems/path-with-maximum-gold/

# Find path collecting maximum gold from grid

# Time Complexity: O(4^(m*n))
# Space Complexity: O(m*n)

# Algorithm:
# 1. Try starting from each non-zero cell
# 2. Use DFS to explore all possible paths
# 3. Track visited cells and backtrack
# 4. Return maximum gold collected

# Key Components:
# - get_maximum_gold(): Main implementation
# - collect_gold(): DFS helper for path exploration
# - Direction arrays for movement
"""


class PathWithMaximumGold:
    def __init__(self):
        self.dx = [0, 0, 1, -1]  # directions for row movement
        self.dy = [1, -1, 0, 0]  # directions for column movement

    def get_maximum_gold(self, grid: list[list[int]]) -> int:
        max_gold = 0
        m, n = len(grid), len(grid[0])

        def collect_gold(grid: list[list[int]], x: int, y: int, m: int, n: int) -> int:
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0

            # Collect gold at current cell
            gold = grid[x][y]
            grid[x][y] = 0  # mark as visited

            max_gold = 0
            for i in range(4):
                new_x = x + self.dx[i]
                new_y = y + self.dy[i]
                max_gold = max(max_gold, collect_gold(grid, new_x, new_y, m, n))

            # Backtrack: restore cell's value
            grid[x][y] = gold
            return max_gold + gold

        # Try starting from each cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    max_gold = max(max_gold, collect_gold(grid, i, j, m, n))

        return max_gold


def main():
    solution = PathWithMaximumGold()
    grid1 = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
    print(solution.get_maximum_gold(grid1))  # Expected: 24

    grid2 = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
    print(solution.get_maximum_gold(grid2))  # Expected: 28


if __name__ == "__main__":
    main()
