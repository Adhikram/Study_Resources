"""
# Question: Check if a Graph is Tripartite
# Link: (Assumed hypothetical problem)

# Problem Statement:
# Given an undirected graph, determine if it is tripartite. A graph is tripartite if its vertices can be divided into three disjoint sets such that no two graph vertices within the same set are adjacent.

# Example:
# Input: n = 4, graph = [[0, 1], [1, 2], [2, 3], [3, 0]]
# Output: False
"""

from typing import List
from collections import deque

# BFS Solution
"""
Algorithm:
1. Initialize a color array to store colors of nodes.
2. Use BFS to traverse the graph.
3. Color the starting node with one color and alternate colors for adjacent nodes.
4. If a conflict is found (two adjacent nodes have the same color), return False.
5. If no conflicts are found, return True.

Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
Space Complexity: O(V) for the color array and queue.
"""


def is_tripartite(n: int, graph: List[List[int]]) -> bool:
    color = [0] * n  # 0 means uncolored, 1 and -1 are two different colors

    def bfs(start: int) -> bool:
        queue = deque([start])
        color[start] = 1  # Start coloring with 1

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == 0:  # If not colored, color with opposite color
                    color[neighbor] = -color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # If same color, not bipartite
                    return False
        return True

    for i in range(n):
        if color[i] == 0:  # Not yet colored
            if not bfs(i):
                return False
    return True


def main():
    test_cases = [
        {"n": 4, "graph": [[1, 3], [0, 2], [1, 3], [0, 2]], "expected": True},
        {"n": 4, "graph": [[0, 1], [1, 2], [2, 3], [3, 0]], "expected": False},
        {"n": 3, "graph": [[0, 1], [1, 2], [2, 0]], "expected": False},
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"n: {test['n']}, graph: {test['graph']}")
        result = is_tripartite(test["n"], test["graph"])
        print(f"Result: {result}, Expected: {test['expected']}")
        assert result == test["expected"], f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
