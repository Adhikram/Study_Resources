"""
# Question: Count Unreachable Pairs of Nodes in an Undirected Graph
# Link: https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

# Problem Statement:
# You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1.
# You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an
# undirected edge connecting nodes ai and bi. Return the number of pairs of different nodes that
# are unreachable from each other.

# Example:
# Input: n = 3, edges = [[0,1],[0,2],[1,2]]
# Output: 0
# Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
"""

from typing import List
from collections import defaultdict

# 1. DFS Solution
"""
Algorithm:
1. Build an adjacency list from the edges.
2. Use DFS to find the size of each connected component.
3. Calculate the number of unreachable pairs using the sizes of the components.

Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
Space Complexity: O(V) for the visited array and recursion stack.
"""


def count_unreachable_pairs_dfs(n: int, edges: List[List[int]]) -> int:
    def dfs(node: int) -> int:
        visited[node] = True
        size = 1
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                size += dfs(neighbor)
        return size

    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = [False] * n
    component_sizes = []

    for i in range(n):
        if not visited[i]:
            component_size = dfs(i)
            component_sizes.append(component_size)

    total_pairs = n * (n - 1) // 2
    reachable_pairs = sum(size * (size - 1) // 2 for size in component_sizes)
    return total_pairs - reachable_pairs


# 2. Union-Find Solution
"""
Algorithm:
1. Initialize a parent array where each node is its own parent.
2. Define find and union functions to manage connected components.
3. For each edge, union the two nodes.
4. Calculate the number of unreachable pairs using the sizes of the components.

Time Complexity: O(E * α(V)) where α is the inverse Ackermann function.
Space Complexity: O(V) for the parent array.
"""


def count_unreachable_pairs_union_find(n: int, edges: List[List[int]]) -> int:
    parent = list(range(n))
    size = [1] * n

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX
            size[rootX] += size[rootY]

    for u, v in edges:
        union(u, v)

    component_sizes = [size[i] for i in range(n) if parent[i] == i]
    total_pairs = n * (n - 1) // 2
    reachable_pairs = sum(s * (s - 1) // 2 for s in component_sizes)
    return total_pairs - reachable_pairs


def main():
    test_cases = [
        {"n": 3, "edges": [[0, 1], [0, 2], [1, 2]], "expected": 0},
        {"n": 7, "edges": [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]], "expected": 14},
        {"n": 5, "edges": [[0, 1], [1, 2], [3, 4]], "expected": 8},
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"n: {test['n']}, edges: {test['edges']}")
        result_dfs = count_unreachable_pairs_dfs(test["n"], test["edges"])
        result_union_find = count_unreachable_pairs_union_find(test["n"], test["edges"])
        print(f"DFS Solution: {result_dfs}, Expected: {test['expected']}")
        print(f"Union-Find Solution: {result_union_find}, Expected: {test['expected']}")
        assert result_dfs == test["expected"], f"Test case {i + 1} failed for DFS"
        assert (
            result_union_find == test["expected"]
        ), f"Test case {i + 1} failed for Union-Find"


if __name__ == "__main__":
    main()
