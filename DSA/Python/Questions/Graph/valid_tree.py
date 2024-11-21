"""
# Question: Graph Valid Tree
# Link: https://leetcode.com/problems/graph-valid-tree/

# Problem Statement:
# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
# Return true if the edges of the given graph make up a valid tree, and false otherwise.

# Example:
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: True

# Example 2:
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: False
"""

from typing import List

# Solution using Union-Find
"""
Algorithm:
1. Initialize a parent array where each node is its own parent.
2. Define find and union functions to manage connected components.
3. For each edge, union the two nodes.
4. Ensure there are no cycles and the graph is fully connected.

Time Complexity: O(E * α(V)) where E is the number of edges and V is the number of vertices.
Space Complexity: O(V) for the parent array.
"""


def valid_tree(n: int, edges: List[List[int]]) -> bool:
    if len(edges) != n - 1:
        return False  # A valid tree must have exactly n - 1 edges

    parent = list(range(n))  # Initialize each node as its own parent

    def find(x: int) -> int:
        # Find the root of the node x
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x: int, y: int) -> bool:
        # Union the sets containing x and y
        rootX = find(x)
        rootY = find(y)
        if rootX == rootY:
            return False  # Cycle detected
        parent[rootY] = rootX  # Union the sets
        return True

    for u, v in edges:
        if not union(u, v):
            return False  # If union fails, a cycle is detected

    return True  # If no cycles are detected and the edge count is correct, it's a valid tree


def main():
    test_cases = [
        {"n": 5, "edges": [[0, 1], [0, 2], [0, 3], [1, 4]], "expected": True},
        {"n": 5, "edges": [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], "expected": False},
        {"n": 4, "edges": [[0, 1], [2, 3]], "expected": False},
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"n: {test['n']}, edges: {test['edges']}")
        result = valid_tree(test["n"], test["edges"])
        print(f"Result: {result}, Expected: {test['expected']}")
        assert result == test["expected"], f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
