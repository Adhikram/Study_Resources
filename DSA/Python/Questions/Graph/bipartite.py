"""
# Question: Check if a Graph is Bipartite
# Link: https://leetcode.com/problems/is-graph-bipartite/

# Problem Statement:
# Given an undirected graph, return true if and only if it is bipartite.
# A graph is bipartite if we can split its set of nodes into two independent subsets A and B
# such that every edge in the graph connects a node in A and a node in B.

# Example:
# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: True
# Explanation: We can split the vertices into two groups: {0, 2} and {1, 3}.
"""

from typing import List
from collections import deque

# 1. BFS Solution
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


def is_bipartite_bfs(graph: List[List[int]]) -> bool:
    n = len(graph)
    color = [-1] * n  # -1 indicates uncolored

    for start in range(n):
        if color[start] == -1:  # Not yet colored
            queue = deque([start])
            color[start] = 0  # Start coloring with 0

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if (
                        color[neighbor] == -1
                    ):  # If not colored, color with opposite color
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:  # If same color, not bipartite
                        return False
    return True


# 2. DFS Solution
"""
Algorithm:
1. Initialize a color array to store colors of nodes.
2. Use DFS to traverse the graph.
3. Color the starting node with one color and alternate colors for adjacent nodes.
4. If a conflict is found (two adjacent nodes have the same color), return False.
5. If no conflicts are found, return True.

Time Complexity: O(V + E)
Space Complexity: O(V) for the color array and recursion stack.
"""


def is_bipartite_dfs(graph: List[List[int]]) -> bool:
    n = len(graph)
    color = [-1] * n

    def dfs(node: int) -> bool:
        for neighbor in graph[node]:
            if color[neighbor] == -1:  # If not colored, color with opposite color
                color[neighbor] = 1 - color[node]
                if not dfs(neighbor):
                    return False
            elif color[neighbor] == color[node]:  # If same color, not bipartite
                return False
        return True

    for start in range(n):
        if color[start] == -1:  # Not yet colored
            color[start] = 0
            if not dfs(start):
                return False
    return True


def main():
    test_cases = [
        {"graph": [[1, 3], [0, 2], [1, 3], [0, 2]], "expected": True},
        {"graph": [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], "expected": False},
        {
            "graph": [
                [],
                [2, 4, 6],
                [1, 4, 8, 9],
                [7, 8],
                [1, 2, 8, 9],
                [6, 9],
                [1, 5, 7, 8, 9],
                [3, 6, 9],
                [2, 3, 4, 6, 9],
                [2, 4, 5, 6, 7, 8],
            ],
            "expected": False,
        },
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Graph: {test['graph']}")
        result_bfs = is_bipartite_bfs(test["graph"])
        result_dfs = is_bipartite_dfs(test["graph"])
        print(f"BFS Solution: {result_bfs}, Expected: {test['expected']}")
        print(f"DFS Solution: {result_dfs}, Expected: {test['expected']}")
        assert result_bfs == test["expected"], f"Test case {i + 1} failed for BFS"
        assert result_dfs == test["expected"], f"Test case {i + 1} failed for DFS"


if __name__ == "__main__":
    main()
