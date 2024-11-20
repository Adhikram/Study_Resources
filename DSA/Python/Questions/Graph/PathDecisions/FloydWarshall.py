"""
# Question: Floyd Warshall Algorithm Implementation
# Finds all pairs shortest paths in a weighted graph

# Time Complexity: O(V^3)
# Space Complexity: O(V^2)

# Algorithm:
# 1. Initialize distance matrix
# 2. Consider all vertices as intermediate
# 3. Update shortest paths through intermediates
"""


class FloydWarshall:
    def all_pairs_shortest_paths(
        self, n: int, edges: list[list[int]]
    ) -> list[list[int]]:
        # Initialize distances
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        # Set direct edges
        for u, v, w in edges:
            dist[u][v] = w

        # Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist


def main():
    solution = FloydWarshall()
    edges = [[0, 1, 4], [0, 2, 3], [1, 2, 1], [2, 3, 2]]
    print(solution.all_pairs_shortest_paths(4, edges))


if __name__ == "__main__":
    main()
