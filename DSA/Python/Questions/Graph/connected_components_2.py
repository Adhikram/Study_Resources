"""
# Question: Number of Connected Components in an Undirected Graph
# Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

# Problem Statement:
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi]
# indicates that there is an edge between ai and bi in the graph. Return the number of connected components
# in the graph.

# Example:
# Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
# Output: 2
# Explanation: There are two connected components: [0, 1, 2] and [3, 4].
"""

from typing import List
from collections import defaultdict

# 1. DFS Solution
"""
Algorithm:
1. Build an adjacency list from the edges.
2. Initialize a visited array to track visited nodes.
3. Use DFS to explore each component starting from an unvisited node.
4. Count the number of DFS calls, which corresponds to the number of connected components.

Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
Space Complexity: O(V) for the visited array and recursion stack.
"""


def count_components_dfs(n: int, edges: List[List[int]]) -> int:
    def dfs(node: int):
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1

    return count


# 2. Union-Find Solution
"""
Algorithm:
1. Initialize a parent array where each node is its own parent.
2. Define find and union functions to manage connected components.
3. For each edge, union the two nodes.
4. Count the number of unique parents, which corresponds to the number of connected components.

Time Complexity: O(E * α(V)) where α is the inverse Ackermann function.
Space Complexity: O(V) for the parent array.
"""


def count_components_union_find(n: int, edges: List[List[int]]) -> int:
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

    # Count unique roots
    return len(set(find(x) for x in range(n)))


def main():
    test_cases = [
        {"n": 5, "edges": [[0, 1], [1, 2], [3, 4]], "expected": 2},
        {"n": 5, "edges": [[0, 1], [1, 2], [2, 3], [3, 4]], "expected": 1},
        {"n": 4, "edges": [[2, 3], [1, 2], [1, 3]], "expected": 2},
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"n: {test['n']}, edges: {test['edges']}")
        result_dfs = count_components_dfs(test["n"], test["edges"])
        result_union_find = count_components_union_find(test["n"], test["edges"])
        print(f"DFS Solution: {result_dfs}, Expected: {test['expected']}")
        print(f"Union-Find Solution: {result_union_find}, Expected: {test['expected']}")
        assert result_dfs == test["expected"], f"Test case {i + 1} failed for DFS"
        assert (
            result_union_find == test["expected"]
        ), f"Test case {i + 1} failed for Union-Find"


if __name__ == "__main__":
    main()
