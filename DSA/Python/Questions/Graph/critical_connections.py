"""
# Question: Critical Connections in a Network
# Link: https://leetcode.com/problems/critical-connections-in-a-network/

# Problem Statement:
# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network
# where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers
# directly or indirectly through the network. A critical connection is a connection that, if removed, will make some
# servers unable to reach some other server. Return all critical connections in the network in any order.

# Example:
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
"""

from typing import List
from collections import defaultdict

# Tarjan's Algorithm for finding bridges
"""
Algorithm:
1. Initialize discovery and low arrays to track discovery times and lowest reachable nodes.
2. Perform DFS traversal to explore the graph.
3. For each node, update its discovery and low values.
4. If a node's lowest reachable node is greater than its discovery time, it's a critical connection.
5. Return all critical connections found.

Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
Space Complexity: O(V + E) for the graph representation and auxiliary data structures.
"""


def critical_connections(n: int, connections: List[List[int]]) -> List[List[int]]:
    def dfs(node: int, parent: int):
        nonlocal time
        discovery[node] = low[node] = time
        time += 1

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if discovery[neighbor] == -1:  # If neighbor is not visited
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > discovery[node]:
                    result.append([node, neighbor])
            else:
                low[node] = min(low[node], discovery[neighbor])

    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    discovery = [-1] * n
    low = [-1] * n
    result = []
    time = 0

    for i in range(n):
        if discovery[i] == -1:
            dfs(i, -1)

    return result


def main():
    test_cases = [
        {"n": 4, "connections": [[0, 1], [1, 2], [2, 0], [1, 3]], "expected": [[1, 3]]},
        {
            "n": 5,
            "connections": [[1, 0], [2, 0], [3, 2], [4, 2], [4, 3], [3, 0], [4, 0]],
            "expected": [],
        },
        {
            "n": 6,
            "connections": [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]],
            "expected": [[1, 3]],
        },
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"n: {test['n']}, connections: {test['connections']}")
        result = critical_connections(test["n"], test["connections"])
        print(f"Result: {result}, Expected: {test['expected']}")
        # Note: The expected results may vary in order, so sorting might be necessary for comparison
        assert sorted(result) == sorted(test["expected"]), f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
