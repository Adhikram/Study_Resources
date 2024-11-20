"""
# Question: Number of Good Paths
# Link: https://leetcode.com/problems/number-of-good-paths/

# Time Complexity: O(N log N)
# Space Complexity: O(N)

# Algorithm:
# 1. Sort nodes by values
# 2. Connect nodes with same or smaller values
# 3. Count good paths in each component
"""

from collections import defaultdict


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
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1


class NoOfGoodPaths:
    def number_of_good_paths(self, vals: list[int], edges: list[list[int]]) -> int:
        n = len(vals)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Group nodes by values
        value_to_nodes = defaultdict(list)
        for i, val in enumerate(vals):
            value_to_nodes[val].append(i)

        dsu = DisjointSet(n)
        result = n  # Each node forms a good path with itself

        # Process nodes in ascending order of values
        for val in sorted(value_to_nodes.keys()):
            # Connect nodes with current value to neighbors with smaller values
            for node in value_to_nodes[val]:
                for neighbor in adj[node]:
                    if vals[neighbor] <= vals[node]:
                        dsu.union(node, neighbor)

            # Count good paths within each component
            component_count = defaultdict(int)
            for node in value_to_nodes[val]:
                component_count[dsu.find(node)] += 1

            # Add number of good paths for current value
            for count in component_count.values():
                result += (count * (count - 1)) // 2

        return result


def main():
    solution = NoOfGoodPaths()
    vals = [1, 3, 2, 1, 3]
    edges = [[0, 1], [0, 2], [2, 3], [2, 4]]
    print(solution.number_of_good_paths(vals, edges))


if __name__ == "__main__":
    main()
