"""
# Question: Validate Binary Tree Nodes
# Link: https://leetcode.com/problems/validate-binary-tree-nodes/

# Problem Statement:
# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i].
# Return true if and only if all the given nodes form exactly one valid binary tree.

# Example:
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: True

# Example 2:
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# Output: False
"""

from typing import List

# Solution using Union-Find
"""
Algorithm:
1. Initialize a parent array where each node is its own parent.
2. Define find and union functions to manage connected components.
3. For each node, union its left and right children with the node itself.
4. Ensure there is exactly one root and no cycles.

Time Complexity: O(n) where n is the number of nodes.
Space Complexity: O(n) for the parent array.
"""


def validate_binary_tree_nodes(
    n: int, leftChild: List[int], rightChild: List[int]
) -> bool:
    parent = list(range(n))  # Initialize each node as its own parent
    indegree = [0] * n  # Track the indegree of each node

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

    for i in range(n):
        if leftChild[i] != -1:
            # Check if left child already has a parent or if union fails
            if indegree[leftChild[i]] > 0 or not union(i, leftChild[i]):
                return False
            indegree[leftChild[i]] += 1  # Increment indegree for left child
        if rightChild[i] != -1:
            # Check if right child already has a parent or if union fails
            if indegree[rightChild[i]] > 0 or not union(i, rightChild[i]):
                return False
            indegree[rightChild[i]] += 1  # Increment indegree for right child

    # Check if there is exactly one root and the total indegree is n - 1
    root_count = sum(1 for i in range(n) if find(i) == i)
    return root_count == 1 and sum(indegree) == n - 1


def main():
    test_cases = [
        {
            "n": 4,
            "leftChild": [1, -1, 3, -1],
            "rightChild": [2, -1, -1, -1],
            "expected": True,
        },
        {
            "n": 4,
            "leftChild": [1, -1, 3, -1],
            "rightChild": [2, 3, -1, -1],
            "expected": False,
        },
        {"n": 2, "leftChild": [1, 0], "rightChild": [-1, -1], "expected": False},
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(
            f"n: {test['n']}, leftChild: {test['leftChild']}, rightChild: {test['rightChild']}"
        )
        result = validate_binary_tree_nodes(
            test["n"], test["leftChild"], test["rightChild"]
        )
        print(f"Result: {result}, Expected: {test['expected']}")
        assert result == test["expected"], f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
