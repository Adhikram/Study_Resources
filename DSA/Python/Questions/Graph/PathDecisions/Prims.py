"""
# Question: Prim's Algorithm Implementation
# Finds Minimum Spanning Tree of weighted undirected graph

# Time Complexity: O(E * logV)
# Space Complexity: O(V + E)

# Algorithm:
# 1. Start from arbitrary vertex
# 2. Add minimum weight edge to MST
# 3. Track visited vertices
"""

from collections import defaultdict
import heapq


class Prims:
    def minimum_spanning_tree(self, n: int, edges: list[list[int]]) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Track visited vertices and total cost
        visited = set()
        total_cost = 0

        # Start with vertex 0
        pq = [(0, 0)]  # (weight, vertex)

        while pq and len(visited) < n:
            weight, vertex = heapq.heappop(pq)

            if vertex in visited:
                continue

            visited.add(vertex)
            total_cost += weight

            for next_vertex, edge_weight in graph[vertex]:
                if next_vertex not in visited:
                    heapq.heappush(pq, (edge_weight, next_vertex))

        return total_cost if len(visited) == n else -1


def main():
    solution = Prims()
    edges = [[0, 1, 4], [0, 2, 3], [1, 2, 1], [2, 3, 2]]
    print(solution.minimum_spanning_tree(4, edges))


if __name__ == "__main__":
    main()
