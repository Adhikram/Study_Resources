"""
# Question: Sum of Distances in Tree
# Link: https://leetcode.com/problems/sum-of-distances-in-tree/

# Problem Statement:
# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

# Example:
# Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
"""

from typing import List
from collections import defaultdict

# Tarjan's Algorithm for finding bridges
"""
Algorithm:
1. Perform a DFS to calculate the count of nodes and initial result for each node.
2. Use another DFS to update the result for each node based on its parent's result.
3. Return the result array.

Time Complexity: O(N) where N is the number of nodes.
Space Complexity: O(N) for the graph representation and auxiliary data structures.
"""


def sum_of_distances_in_tree(n: int, edges: List[List[int]]) -> List[int]:
    def dfs1(node: int, parent: int):
        count[node] = 1  # Each node counts itself
        for neighbor in graph[node]:
            if neighbor != parent:
                dfs1(neighbor, node)
                count[node] += count[neighbor]  # Add the count of child nodes
                res[node] += (
                    res[neighbor] + count[neighbor]
                )  # Add the distances from the child nodes

    def dfs2(node: int, parent: int):
        for neighbor in graph[node]:
            if neighbor != parent:
                res[neighbor] = (
                    res[node] + n - 2 * count[neighbor]
                )  # Update the result for the child node
                dfs2(neighbor, node)

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    res = [0] * n
    count = [0] * n

    dfs1(0, -1)  # First DFS to calculate initial results
    dfs2(0, -1)  # Second DFS to update results based on parent's result

    return res


def main():
    test_cases = [
        {
            "n": 6,
            "edges": [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]],
            "expected": [8, 12, 6, 10, 10, 10],
        },
        {"n": 1, "edges": [], "expected": [0]},
        {"n": 2, "edges": [[1, 0]], "expected": [1, 1]},
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"n: {test['n']}, edges: {test['edges']}")
        result = sum_of_distances_in_tree(test["n"], test["edges"])
        print(f"Result: {result}, Expected: {test['expected']}")
        assert result == test["expected"], f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
