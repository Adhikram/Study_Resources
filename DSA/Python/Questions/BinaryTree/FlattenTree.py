"""
# Question: Flatten Binary Tree to Linked List
# Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Time Complexity: O(N)
# Space Complexity: O(1)

# Algorithm:
# 1. Morris Traversal approach
# 2. Find predecessor node
# 3. Flatten tree in-place
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class FlattenTree:
    def flatten(self, root: TreeNode) -> None:
        curr = root

        while curr:
            if curr.left:
                # Find predecessor
                prev = curr.left
                while prev.right:
                    prev = prev.right

                # Make connections
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None

            curr = curr.right


def main():
    solution = FlattenTree()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    solution.flatten(root)

    # Print flattened tree
    while root:
        print(root.val, end=" ")
        root = root.right


if __name__ == "__main__":
    main()
