"""
# Question: Maximum Depth of Binary Tree
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Time Complexity: O(N)
# Space Complexity: O(H)

# Algorithm:
# 1. DFS traversal
# 2. Calculate height recursively
# 3. Return maximum height
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Height:
    def max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_height = self.max_depth(root.left)
        right_height = self.max_depth(root.right)

        return max(left_height, right_height) + 1


def main():
    solution = Height()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    print(solution.max_depth(root))


if __name__ == "__main__":
    main()
