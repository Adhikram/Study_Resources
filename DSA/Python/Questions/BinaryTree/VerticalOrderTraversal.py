"""
# Question: Vertical Order Traversal of Binary Tree
# Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Time Complexity: O(N log N)
# Space Complexity: O(N)

# Algorithm:
# 1. DFS with coordinates
# 2. Sort by column, row, and value
# 3. Group by vertical level
"""

from collections import defaultdict


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class VerticalOrderTraversal:
    def vertical_traversal(self, root: TreeNode) -> list[list[int]]:
        nodes = []

        def dfs(node: TreeNode, row: int, col: int) -> None:
            if node:
                nodes.append((col, row, node.val))
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        nodes.sort()

        columns = defaultdict(list)
        for col, row, val in nodes:
            columns[col].append(val)

        return [columns[col] for col in sorted(columns.keys())]


def main():
    solution = VerticalOrderTraversal()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    print(solution.vertical_traversal(root))


if __name__ == "__main__":
    main()
