"""
# Question: Binary Tree Level Order Traversal
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Time Complexity: O(N)
# Space Complexity: O(W) where W is max width

# Algorithm:
# 1. BFS traversal
# 2. Track levels
# 3. Build result list
"""

from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class LevelOrderTraversal:
    def level_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([(root, 0)])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node, level = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

            result.append(current_level)

        return result


def main():
    solution = LevelOrderTraversal()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    print(solution.level_order(root))


if __name__ == "__main__":
    main()
