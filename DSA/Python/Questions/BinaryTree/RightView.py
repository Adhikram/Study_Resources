"""
# Question: Binary Tree Right Side View
# Link: https://leetcode.com/problems/binary-tree-right-side-view/

# Time Complexity: O(N)
# Space Complexity: O(H)

# Algorithm:
# 1. Level order traversal
# 2. Track rightmost nodes
# 3. DFS with level tracking
"""

from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class RightView:
    def right_side_view(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []
        max_level = [-1]

        def dfs(node: TreeNode, level: int) -> None:
            if not node:
                return

            if level > max_level[0]:
                result.append(node.val)
                max_level[0] = level

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return result


def main():
    solution = RightView()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.right_side_view(root))


if __name__ == "__main__":
    main()
