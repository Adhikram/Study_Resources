"""
# Question: Minimum Cost to Supply Water
# Link: https://leetcode.com/problems/optimize-water-distribution-in-a-village/

# Time Complexity: O(E log E) where E is number of edges
# Space Complexity: O(N) where N is number of houses

# Algorithm:
# 1. Convert well costs to edges from virtual node
# 2. Use Kruskal's algorithm with DSU
# 3. Find minimum spanning tree cost
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


class MinimumCostToWaterSupply:
    def min_cost_to_supply_water(
        self, n: int, wells: list[int], pipes: list[list[int]]
    ) -> int:
        edges = []

        # Add well costs as edges from virtual node 0
        for i, cost in enumerate(wells, 1):
            edges.append((cost, 0, i))

        # Add pipe costs
        for house1, house2, cost in pipes:
            edges.append((cost, house1, house2))

        # Sort edges by cost
        edges.sort()

        # Apply Kruskal's algorithm
        dsu = DisjointSet(n + 1)
        total_cost = 0

        for cost, u, v in edges:
            if dsu.union(u, v):
                total_cost += cost

        return total_cost


def main():
    solution = MinimumCostToWaterSupply()
    wells = [1, 2, 2]
    pipes = [[1, 2, 1], [2, 3, 1]]
    print(solution.min_cost_to_supply_water(3, wells, pipes))


if __name__ == "__main__":
    main()
