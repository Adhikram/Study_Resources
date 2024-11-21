"""
# Question: Get Direction Between Two Nodes in a Graph
# Link: (Assumed hypothetical problem)

# Problem Statement:
# Given a directed graph represented as an adjacency list and two nodes, source and destination, determine if there is a path from the source to the destination. If such a path exists, return the direction of the path as a list of nodes from source to destination. If no path exists, return an empty list.

# Example:
# Input: graph = {0: [1, 2], 1: [3], 2: [3], 3: []}, source = 0, destination = 3
# Output: [0, 1, 3] or [0, 2, 3]
"""

from typing import List, Dict

# DFS Solution
"""
Algorithm:
1. Use DFS to explore the graph starting from the source node.
2. Track the path taken using a list.
3. If the destination is reached, return the path.
4. If no path is found, return an empty list.

Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
Space Complexity: O(V) for the visited array and recursion stack.
"""


def get_direction(
    graph: Dict[int, List[int]], source: int, destination: int
) -> List[int]:
    def dfs(node: int, path: List[int]) -> bool:
        # Base case: if the current node is the destination, path is found
        if node == destination:
            return True
        visited[node] = True  # Mark the current node as visited
        # Explore each neighbor of the current node
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:  # If neighbor hasn't been visited
                path.append(neighbor)  # Add neighbor to the current path
                if dfs(neighbor, path):  # Recursively explore the neighbor
                    return True
                path.pop()  # Backtrack if the path through this neighbor doesn't lead to the destination
        return False

    visited = {node: False for node in graph}  # Track visited nodes
    path = [source]  # Initialize path with the source node
    if dfs(source, path):  # Start DFS from the source node
        return path  # Return the path if found
    return []  # Return an empty list if no path exists


def main():
    test_cases = [
        {
            "graph": {0: [1, 2], 1: [3], 2: [3], 3: []},
            "source": 0,
            "destination": 3,
            "expected": [[0, 1, 3], [0, 2, 3]],
        },
        {
            "graph": {0: [1], 1: [2], 2: [3], 3: []},
            "source": 0,
            "destination": 3,
            "expected": [[0, 1, 2, 3]],
        },
        {
            "graph": {0: [1], 1: [2], 2: [], 3: []},
            "source": 0,
            "destination": 3,
            "expected": [],
        },
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(
            f"Graph: {test['graph']}, Source: {test['source']}, Destination: {test['destination']}"
        )
        result = get_direction(test["graph"], test["source"], test["destination"])
        print(f"Result: {result}, Expected: {test['expected']}")
        assert result in test["expected"], f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
