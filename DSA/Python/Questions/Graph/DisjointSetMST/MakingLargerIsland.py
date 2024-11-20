"""
# Question: Making A Large Island
# Link: https://leetcode.com/problems/making-a-large-island/

# Time Complexity: O(N²)
# Space Complexity: O(N²)

# Algorithm:
# 1. Use DSU to find connected components
# 2. Track size of each island
# 3. Try changing each 0 to 1 and merge adjacent islands
"""


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        self.parent[py] = px
        self.size[px] += self.size[py]


class MakingLargerIsland:
    def largest_island(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dsu = DisjointSet(n * n)

        def get_index(i: int, j: int) -> int:
            return i * n + j

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # First pass: build components
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            dsu.union(get_index(i, j), get_index(ni, nj))

        # Second pass: try changing 0s
        result = max(dsu.size[dsu.find(i)] for i in range(n * n))

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    size = 1
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            parent = dsu.find(get_index(ni, nj))
                            if parent not in seen:
                                size += dsu.size[parent]
                                seen.add(parent)
                    result = max(result, size)

        return result


def main():
    solution = MakingLargerIsland()
    grid = [[1, 0], [0, 1]]
    print(solution.largest_island(grid))


if __name__ == "__main__":
    main()
