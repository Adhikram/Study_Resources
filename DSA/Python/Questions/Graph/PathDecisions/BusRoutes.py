"""
# Question: Bus Routes
# Link: https://leetcode.com/problems/bus-routes/

# Time Complexity: O(N * R) where N is total stops and R is routes
# Space Complexity: O(N * R)

# Algorithm:
# 1. Build graph of bus stops and routes
# 2. BFS to find shortest path
# 3. Track visited stops and routes
"""

from collections import defaultdict, deque


class BusRoutes:
    def num_buses_to_destination(
        self, routes: list[list[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        # Build graph
        stop_to_routes = defaultdict(set)
        for route_id, stops in enumerate(routes):
            for stop in stops:
                stop_to_routes[stop].add(route_id)

        # BFS
        queue = deque([(source, 0)])
        visited_stops = {source}
        visited_routes = set()

        while queue:
            stop, buses = queue.popleft()

            for route_id in stop_to_routes[stop]:
                if route_id in visited_routes:
                    continue

                visited_routes.add(route_id)
                for next_stop in routes[route_id]:
                    if next_stop == target:
                        return buses + 1
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses + 1))

        return -1


def main():
    solution = BusRoutes()
    routes = [[1, 2, 7], [3, 6, 7]]
    print(solution.num_buses_to_destination(routes, 1, 6))


if __name__ == "__main__":
    main()
