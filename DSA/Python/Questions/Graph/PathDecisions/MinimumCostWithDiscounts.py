"""
# Question: Minimum Cost Path with Discounts
# Find shortest path considering possible discounts on edges

# Time Complexity: O(E * logV)
# Space Complexity: O(V + E)

# Algorithm:
# 1. Modified Dijkstra with state
# 2. Track paths with/without discount
# 3. Return minimum total cost
"""

from collections import defaultdict
import heapq


class MinimumCostWithDiscounts:
    def min_cost_path(self, n: int, edges: list[list[int]], discounts: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # State: (cost, node, remaining_discounts)
        pq = [(0, 0, discounts)]
        visited = set()

        while pq:
            cost, node, rem_disc = heapq.heappop(pq)

            state = (node, rem_disc)
            if state in visited:
                continue
            visited.add(state)

            if node == n - 1:
                return cost

            for next_node, weight in graph[node]:
                # Without discount
                heapq.heappush(pq, (cost + weight, next_node, rem_disc))

                # With discount
                if rem_disc > 0:
                    heapq.heappush(pq, (cost + weight // 2, next_node, rem_disc - 1))

        return -1


def main():
    solution = MinimumCostWithDiscounts()
    edges = [[0, 1, 10], [1, 2, 20]]
    print(solution.min_cost_path(3, edges, 1))


if __name__ == "__main__":
    main()
