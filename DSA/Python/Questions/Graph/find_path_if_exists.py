"""
# Question: Find if Path Exists in Graph
# Link: https://leetcode.com/problems/find-if-path-exists-in-graph/

# Problem Statement:
# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
# The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes
# a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge,
# and no vertex has an edge to itself. You want to determine if there is a valid path that exists from vertex
# source to vertex destination.

# Example:
# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: True
# Explanation: There are two paths from vertex 0 to vertex 2: 0 → 1 → 2 and 0 → 2.
"""

from typing import List
from collections import defaultdict, deque

# 1. BFS Solution
"""
Algorithm:
1. Build an adjacency list from the edges.
2. Use BFS to explore the graph starting from the source node.
3. If the destination node is reached, return True.
4. If the queue is exhausted without reaching the destination, return False.

Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
Space Complexity: O(V) for the visited array and queue.
"""


def valid_path_bfs(
    n: int, edges: List[List[int]], source: int, destination: int
) -> bool:
    if source == destination:
        return True

    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    queue = deque([source])
    visited = [False] * n
    visited[source] = True

    while queue:
        node = queue.popleft()
        for neighbor in adj_list[node]:
            if neighbor == destination:
                return True
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return False


# 2. Union-Find Solution
"""
Algorithm:
1. Initialize a parent array where each node is its own parent.
2. Define find and union functions to manage connected components.
3. For each edge, union the two nodes.
4. Check if the source and destination nodes have the same root.

Time Complexity: O(E * α(V)) where α is the inverse Ackermann function.
Space Complexity: O(V) for the parent array.
"""


def valid_path_union_find(
    n: int, edges: List[List[int]], source: int, destination: int
) -> bool:
    parent = list(range(n))

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX

    for u, v in edges:
        union(u, v)

    return find(source) == find(destination)


def main():
    test_cases = [
        {
            "n": 3,
            "edges": [[0, 1], [1, 2], [2, 0]],
            "source": 0,
            "destination": 2,
            "expected": True,
        },
        {
            "n": 6,
            "edges": [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]],
            "source": 0,
            "destination": 5,
            "expected": False,
        },
        {"n": 1, "edges": [], "source": 0, "destination": 0, "expected": True},
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(
            f"n: {test['n']}, edges: {test['edges']}, source: {test['source']}, destination: {test['destination']}"
        )
        result_bfs = valid_path_bfs(
            test["n"], test["edges"], test["source"], test["destination"]
        )
        result_union_find = valid_path_union_find(
            test["n"], test["edges"], test["source"], test["destination"]
        )
        print(f"BFS Solution: {result_bfs}, Expected: {test['expected']}")
        print(f"Union-Find Solution: {result_union_find}, Expected: {test['expected']}")
        assert result_bfs == test["expected"], f"Test case {i + 1} failed for BFS"
        assert (
            result_union_find == test["expected"]
        ), f"Test case {i + 1} failed for Union-Find"


if __name__ == "__main__":
    main()
