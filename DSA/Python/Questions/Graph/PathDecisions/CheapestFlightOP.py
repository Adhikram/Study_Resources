"""
# Question: Optimized Cheapest Flights Within K Stops
# Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/

# Time Complexity: O(E * K) where E is number of flights
# Space Complexity: O(N)

# Algorithm:
# 1. Priority Queue based Dijkstra variant
# 2. Track stops and costs together
# 3. Early termination optimizations
"""

from collections import defaultdict
import heapq


class CheapestFlightOP:
    def find_cheapest_price(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # Priority queue entries: (cost, stops, city)
        pq = [(0, 0, src)]
        # Track best costs for each city and stops
        visited = {}

        while pq:
            cost, stops, city = heapq.heappop(pq)

            # Reached destination
            if city == dst:
                return cost

            # Exceeded stops limit
            if stops > k:
                continue

            # Process neighbors
            for next_city, price in graph[city]:
                next_cost = cost + price

                if (next_city, stops) not in visited or visited[
                    (next_city, stops)
                ] > next_cost:
                    visited[(next_city, stops)] = next_cost
                    heapq.heappush(pq, (next_cost, stops + 1, next_city))

        return -1


def main():
    solution = CheapestFlightOP()
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    print(solution.find_cheapest_price(3, flights, 0, 2, 1))


if __name__ == "__main__":
    main()
