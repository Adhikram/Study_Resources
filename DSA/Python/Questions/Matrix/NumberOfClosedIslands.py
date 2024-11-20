"""
# Question: Number of Closed Islands
# Link: https://leetcode.com/problems/number-of-closed-islands/

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

# Algorithm:
# 1. DFS to explore each island
# 2. Check if island is closed
# 3. Mark visited cells
# 4. Count valid islands
"""


class NumberOfClosedIslands:
    def closed_island(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i: int, j: int) -> bool:
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if grid[i][j] == 1:
                return True

            grid[i][j] = 1  # mark as visited

            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)

            return up and down and left and right

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and dfs(i, j):
                    count += 1

        return count


def main():
    solution = NumberOfClosedIslands()
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0],
    ]
    print(solution.closed_island(grid))  # Expected: 2


if __name__ == "__main__":
    main()
