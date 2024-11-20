"""
# Question: Most Stones Removed with Same Row or Column
# Link: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

# Time Complexity: O(N * α(N))
# Space Complexity: O(N)

# Algorithm:
# 1. Connect stones in same row/column using DSU
# 2. Count connected components
# 3. Result is total stones minus components
"""


class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1


class MostStones:
    def remove_stones(self, stones: list[list[int]]) -> int:
        dsu = DisjointSet()

        for x, y in stones:
            # Use row+10001 to avoid collision with column numbers
            dsu.union(x, y + 10001)

        components = len({dsu.find(x) for x, y in stones})
        return len(stones) - components


def main():
    solution = MostStones()
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    print(solution.remove_stones(stones))


if __name__ == "__main__":
    main()
