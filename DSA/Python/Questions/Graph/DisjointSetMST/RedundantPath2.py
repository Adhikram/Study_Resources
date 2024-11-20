"""
# Question: Redundant Connection II
# Link: https://leetcode.com/problems/redundant-connection-ii/

# Time Complexity: O(N * α(N))
# Space Complexity: O(N)

# Algorithm:
# 1. Find nodes with two parents
# 2. Try removing each candidate edge
# 3. Check if remaining graph is valid tree
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


class RedundantPath2:
    def find_redundant_directed_connection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = [0] * (n + 1)
        first_edge = second_edge = cycle_edge = None

        # Find nodes with two parents
        for i, (u, v) in enumerate(edges):
            if parent[v] == 0:
                parent[v] = u
            else:
                first_edge = [parent[v], v]
                second_edge = [u, v]
                edges[i][1] = 0  # Remove second edge temporarily

        # Check for cycle
        dsu = DisjointSet(n + 1)
        for u, v in edges:
            if v == 0:
                continue
            if not dsu.union(u, v):
                cycle_edge = [u, v]
                break

        if second_edge is None:
            return cycle_edge
        if cycle_edge is None:
            return second_edge
        return first_edge


def main():
    solution = RedundantPath2()
    edges = [[1, 2], [2, 3], [3, 1], [1, 4]]
    print(solution.find_redundant_directed_connection(edges))


if __name__ == "__main__":
    main()
