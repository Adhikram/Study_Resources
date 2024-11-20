"""
# Question: Dijkstra's Algorithm Implementation
# Finds shortest paths from source to all vertices in weighted graph

# Time Complexity: O(E * logV)
# Space Complexity: O(V + E)

# Algorithm:
# 1. Priority queue based implementation
# 2. Track distances and visited nodes
# 3. Relaxation of edges
"""

from collections import defaultdict
import heapq


class Dijkstra:
    def shortest_path(self, n: int, edges: list[list[int]], source: int) -> list[int]:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        # Initialize distances
        dist = [float("inf")] * n
        dist[source] = 0

        # Priority queue: (distance, node)
        pq = [(0, source)]
        visited = set()

        while pq:
            d, u = heapq.heappop(pq)

            if u in visited:
                continue
            visited.add(u)

            for v, w in graph[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))

        return dist


def main():
    solution = Dijkstra()
    edges = [[0, 1, 4], [0, 2, 1], [2, 1, 2], [1, 3, 1], [2, 3, 5]]
    print(solution.shortest_path(4, edges, 0))


if __name__ == "__main__":
    main()
