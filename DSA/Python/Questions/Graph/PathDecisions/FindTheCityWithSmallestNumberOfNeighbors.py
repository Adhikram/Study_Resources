"""
# Question: Find the City With the Smallest Number of Neighbors at a Threshold Distance
# Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

# Time Complexity: O(N^3)
# Space Complexity: O(N^2)

# Algorithm:
# 1. Floyd-Warshall for all pairs shortest paths
# 2. Count reachable cities within threshold
# 3. Find city with minimum neighbors
"""


class FindTheCityWithSmallestNumberOfNeighbors:
    def find_the_city(
        self, n: int, edges: list[list[int]], distance_threshold: int
    ) -> int:
        # Initialize distance matrix
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        # Build initial distances
        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w

        # Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Find city with minimum reachable neighbors
        min_cities = n
        result = 0

        for i in range(n):
            reachable = sum(
                1 for j in range(n) if i != j and dist[i][j] <= distance_threshold
            )
            if reachable <= min_cities:
                min_cities = reachable
                result = i

        return result


def main():
    solution = FindTheCityWithSmallestNumberOfNeighbors()
    edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    print(solution.find_the_city(4, edges, 4))


if __name__ == "__main__":
    main()
