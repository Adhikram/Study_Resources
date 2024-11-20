"""
# Question: Cheapest Flights Within K Stops
# Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/

# Time Complexity: O(N * K) where N is number of cities
# Space Complexity: O(N)

# Algorithm:
# 1. Bellman-Ford variant
# 2. Track costs for k stops
# 3. Handle impossible routes
"""


class CheapestFlight:
    def find_cheapest_price(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        # Run k + 1 iterations
        for i in range(k + 1):
            temp_prices = prices.copy()

            for from_city, to_city, price in flights:
                if prices[from_city] == float("inf"):
                    continue
                temp_prices[to_city] = min(
                    temp_prices[to_city], prices[from_city] + price
                )

            prices = temp_prices

        return prices[dst] if prices[dst] != float("inf") else -1

    def find_cheapest_price_dfs(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        graph = {}
        for u, v, w in flights:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))

        min_cost = float("inf")
        visited = set()

        def dfs(city: int, stops: int, cost: int):
            nonlocal min_cost

            if stops > k + 1 or cost >= min_cost:
                return
            if city == dst:
                min_cost = cost
                return

            if city in graph:
                for next_city, price in graph[city]:
                    if (city, next_city) not in visited:
                        visited.add((city, next_city))
                        dfs(next_city, stops + 1, cost + price)
                        visited.remove((city, next_city))

        dfs(src, 0, 0)
        return min_cost if min_cost != float("inf") else -1


def main():
    solution = CheapestFlight()
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    print(solution.find_cheapest_price(3, flights, 0, 2, 1))
    print(solution.find_cheapest_price_dfs(3, flights, 0, 2, 1))


if __name__ == "__main__":
    main()
