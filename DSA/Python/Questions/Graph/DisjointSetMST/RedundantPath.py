"""
# Question: Redundant Connection
# Link: https://leetcode.com/problems/redundant-connection/

# Time Complexity: O(N * α(N))
# Space Complexity: O(N)

# Algorithm:
# 1. Process edges in order
# 2. Use DSU to detect cycle
# 3. Return first edge that creates cycle
"""


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

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
        return True


class RedundantPath:
    def find_redundant_connection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        dsu = DisjointSet(n + 1)

        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]

        return []


def main():
    solution = RedundantPath()
    edges = [[1, 2], [1, 3], [2, 3]]
    print(solution.find_redundant_connection(edges))


if __name__ == "__main__":
    main()
