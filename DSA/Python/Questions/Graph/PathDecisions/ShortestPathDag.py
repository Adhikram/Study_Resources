"""
# Question: Shortest Path in Directed Acyclic Graph (DAG)
# Find shortest path in DAG using topological sort

# Time Complexity: O(V + E)
# Space Complexity: O(V)

# Algorithm:
# 1. Topological sort using DFS
# 2. Process vertices in topological order
# 3. Relax edges for each vertex
"""

from collections import defaultdict


class ShortestPathDag:
    def topological_sort(self, graph: dict, v: int, visited: set, stack: list) -> None:
        visited.add(v)
        for u, _ in graph[v]:
            if u not in visited:
                self.topological_sort(graph, u, visited, stack)
        stack.append(v)

    def shortest_path(self, n: int, edges: list[list[int]], source: int) -> list[int]:
        # Build graph
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        # Get topological order
        visited = set()
        stack = []
        for v in range(n):
            if v not in visited:
                self.topological_sort(graph, v, visited, stack)

        # Initialize distances
        dist = [float("inf")] * n
        dist[source] = 0

        # Process vertices in topological order
        while stack:
            u = stack.pop()
            if dist[u] != float("inf"):
                for v, w in graph[u]:
                    dist[v] = min(dist[v], dist[u] + w)

        return dist


def main():
    solution = ShortestPathDag()
    edges = [[0, 1, 5], [0, 2, 3], [1, 3, 6], [2, 3, 2]]
    print(solution.shortest_path(4, edges, 0))


if __name__ == "__main__":
    main()
