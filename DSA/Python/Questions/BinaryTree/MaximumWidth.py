"""
# Question: Maximum Width of Binary Tree
# Link: https://leetcode.com/problems/maximum-width-of-binary-tree/

# Time Complexity: O(N)
# Space Complexity: O(W) where W is max width

# Algorithm:
# 1. Level order traversal with indexing
# 2. Track leftmost and rightmost nodes
# 3. Calculate width at each level
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class MaximumWidth:
    def width_of_binary_tree(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_width = 0
        queue = deque([(root, 0)])

        while queue:
            level_length = len(queue)
            _, level_start = queue[0]

            for i in range(level_length):
                node, col_index = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * col_index))
                if node.right:
                    queue.append((node.right, 2 * col_index + 1))

            max_width = max(max_width, col_index - level_start + 1)

        return max_width


def main():
    solution = MaximumWidth()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    print(solution.width_of_binary_tree(root))


if __name__ == "__main__":
    main()
