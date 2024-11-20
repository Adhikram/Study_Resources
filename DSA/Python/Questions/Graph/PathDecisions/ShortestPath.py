"""
# Question: Shortest Path in Weighted Graph
# Find shortest path between two vertices considering edge weights

# Time Complexity: O(E * logV)
# Space Complexity: O(V + E)

# Algorithm:
# 1. Dijkstra's algorithm implementation
# 2. Track path along with distances
# 3. Reconstruct shortest path
"""

from collections import defaultdict
import heapq


class ShortestPath:
    def find_shortest_path(
        self, n: int, edges: list[list[int]], source: int, target: int
    ) -> list[int]:
        # Build graph
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        # Distance and parent tracking
        dist = [float("inf")] * n
        parent = [-1] * n
        dist[source] = 0

        # Priority queue
        pq = [(0, source)]

        while pq:
            d, u = heapq.heappop(pq)

            if u == target:
                break

            if d > dist[u]:
                continue

            for v, w in graph[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))

        # Reconstruct path
        if dist[target] == float("inf"):
            return []

        path = []
        curr = target
        while curr != -1:
            path.append(curr)
            curr = parent[curr]

        return path[::-1]


def main():
    solution = ShortestPath()
    edges = [[0, 1, 4], [0, 2, 1], [2, 1, 2], [1, 3, 1]]
    print(solution.find_shortest_path(4, edges, 0, 3))


if __name__ == "__main__":
    main()
