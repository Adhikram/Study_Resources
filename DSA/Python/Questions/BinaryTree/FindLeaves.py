"""
# Question: Find Leaves of Binary Tree
# Link: https://leetcode.com/problems/find-leaves-of-binary-tree/

# Time Complexity: O(N)
# Space Complexity: O(N)

# Algorithm:
# 1. Calculate height from bottom
# 2. Group nodes by height
# 3. Return leaves by level
"""

from collections import defaultdict


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class FindLeaves:
    def find_leaves(self, root: TreeNode) -> list[list[int]]:
        height_map = defaultdict(list)

        def get_height(node: TreeNode) -> int:
            if not node:
                return -1

            height = max(get_height(node.left), get_height(node.right)) + 1
            height_map[height].append(node.val)
            return height

        get_height(root)
        return [height_map[i] for i in range(len(height_map))]


def main():
    solution = FindLeaves()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.find_leaves(root))


if __name__ == "__main__":
    main()
