"""
# Question: Path with Maximum Probability
# Link: https://leetcode.com/problems/path-with-maximum-probability/

# Time Complexity: O(E * logV)
# Space Complexity: O(V + E)

# Algorithm:
# 1. Modified Dijkstra for maximum probability
# 2. Use priority queue with negative probabilities
# 3. Track maximum probabilities to each node
"""

from collections import defaultdict
import heapq


class PathWithMaxProbability:
    def max_probability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start: int,
        end: int,
    ) -> float:
        # Build graph
        graph = defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))

        # Initialize probabilities
        probs = [0.0] * n
        probs[start] = 1.0

        # Priority queue with negative probabilities for max heap
        pq = [(-1.0, start)]

        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob

            if node == end:
                return prob

            if prob < probs[node]:
                continue

            for next_node, p in graph[node]:
                new_prob = prob * p
                if new_prob > probs[next_node]:
                    probs[next_node] = new_prob
                    heapq.heappush(pq, (-new_prob, next_node))

        return probs[end]


def main():
    solution = PathWithMaxProbability()
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    print(solution.max_probability(3, edges, succProb, 0, 2))


if __name__ == "__main__":
    main()
