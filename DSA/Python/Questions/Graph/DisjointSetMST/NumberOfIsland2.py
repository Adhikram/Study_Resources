"""
# Question: Number of Islands II
# Link: https://leetcode.com/problems/number-of-islands-ii/

# Time Complexity: O(k * α(mn)) where k is number of operations
# Space Complexity: O(mn)

# Algorithm:
# 1. Process land additions sequentially
# 2. Use DSU to merge adjacent lands
# 3. Track number of distinct islands
"""


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.count -= 1
        return True


class NumberOfIsland2:
    def num_islands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        dsu = DisjointSet(m * n)
        grid = [[0] * n for _ in range(m)]
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for x, y in positions:
            if grid[x][y] == 1:
                result.append(dsu.count)
                continue

            grid[x][y] = 1
            dsu.count += 1

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    dsu.union(x * n + y, nx * n + ny)

            result.append(dsu.count)

        return result


def main():
    solution = NumberOfIsland2()
    positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
    print(solution.num_islands2(3, 3, positions))


if __name__ == "__main__":
    main()
