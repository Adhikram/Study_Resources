"""
# Question: Count All Possible Paths
# Link: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

# Time Complexity: O(E * logV)
# Space Complexity: O(V + E)

# Algorithm:
# 1. Modified Dijkstra's algorithm
# 2. Track count of shortest paths
# 3. Handle modulo arithmetic
"""

from collections import defaultdict
import heapq


class CountPath:
    def count_paths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)

        # Build adjacency list
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Distance and ways arrays
        dist = [float("inf")] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        # Priority queue: (distance, node)
        pq = [(0, 0)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, time in graph[u]:
                if dist[v] > d + time:
                    dist[v] = d + time
                    ways[v] = ways[u]
                    heapq.heappush(pq, (dist[v], v))
                elif dist[v] == d + time:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1]


def main():
    solution = CountPath()
    roads = [[0, 1, 1], [0, 2, 2], [1, 2, 1]]
    print(solution.count_paths(3, roads))


if __name__ == "__main__":
    main()
