"""
# Question: Frog Position After T Seconds
# Link: https://leetcode.com/problems/frog-position-after-t-seconds/

# Problem Statement:
# Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can only jump to an unvisited vertex. The frog cannot jump back to a visited vertex. In case the frog cannot jump to any unvisited vertex, it will stay on the current vertex.
# Return the probability that after t seconds the frog is on the vertex target.

# Example:
# Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
# Output: 0.16666666666666666
"""

from typing import List
from collections import defaultdict

# DFS Solution
"""
Algorithm:
1. Build an adjacency list from the edges.
2. Use DFS to explore the tree starting from vertex 1.
3. Track the probability of reaching each vertex.
4. Return the probability of reaching the target vertex after t seconds.

Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
Space Complexity: O(V) for the visited array and recursion stack.
"""


def frog_position(n: int, edges: List[List[int]], t: int, target: int) -> float:
    def dfs(node: int, time: int, prob: float) -> float:
        # Base case: if time is up or we reach the target
        if time == 0 or node == target:
            return prob if node == target else 0

        visited[node] = True  # Mark the current node as visited
        # Find all unvisited neighbors
        unvisited_neighbors = [
            neighbor for neighbor in graph[node] if not visited[neighbor]
        ]
        num_unvisited = len(unvisited_neighbors)

        # If there are no unvisited neighbors, check if we're at the target
        if num_unvisited == 0:
            return prob if node == target else 0

        # Explore each unvisited neighbor
        for neighbor in unvisited_neighbors:
            result = dfs(neighbor, time - 1, prob / num_unvisited)
            if result > 0:
                return result

        visited[node] = False  # Unmark the node if not successful
        return 0

    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)  # Track visited nodes
    return dfs(1, t, 1.0)  # Start DFS from node 1 with full probability


def main():
    test_cases = [
        {
            "n": 7,
            "edges": [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]],
            "t": 2,
            "target": 4,
            "expected": 0.16666666666666666,
        },
        {
            "n": 7,
            "edges": [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]],
            "t": 1,
            "target": 7,
            "expected": 0.3333333333333333,
        },
        {"n": 3, "edges": [[2, 1], [3, 2]], "t": 1, "target": 2, "expected": 1.0},
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(
            f"n: {test['n']}, edges: {test['edges']}, t: {test['t']}, target: {test['target']}"
        )
        result = frog_position(test["n"], test["edges"], test["t"], test["target"])
        print(f"Result: {result}, Expected: {test['expected']}")
        assert abs(result - test["expected"]) < 1e-9, f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
