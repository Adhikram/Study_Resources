"""
# Question: Bellman-Ford Algorithm Implementation
# Finds shortest paths from source vertex to all vertices

# Time Complexity: O(VE)
# Space Complexity: O(V)

# Algorithm:
# 1. Initialize distances
# 2. Relax all edges V-1 times
# 3. Check for negative cycles
"""


class BellmanFordAlgorithm:
    def bellman_ford(
        self, vertices: int, edges: list[list[int]], source: int
    ) -> list[int]:
        # Initialize distances
        dist = [float("inf")] * vertices
        dist[source] = 0

        # Relax all edges V-1 times
        for _ in range(vertices - 1):
            for u, v, w in edges:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Check for negative cycles
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                return None  # Negative cycle exists

        return dist


def main():
    solution = BellmanFordAlgorithm()
    edges = [[0, 1, 4], [0, 2, 3], [1, 2, -1], [2, 3, 2]]
    print(solution.bellman_ford(4, edges, 0))


if __name__ == "__main__":
    main()
