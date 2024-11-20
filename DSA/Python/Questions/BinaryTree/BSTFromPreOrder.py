"""
# Question: Construct BST from Preorder Traversal
# Link: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Time Complexity: O(N)
# Space Complexity: O(N)

# Algorithm:
# 1. Use preorder array first element as root
# 2. Find elements less than root for left subtree
# 3. Recursively build left and right subtrees
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class BSTFromPreOrder:
    def bst_from_preorder(self, preorder: list[int]) -> TreeNode:
        self.idx = 0

        def build(bound: int) -> TreeNode:
            if self.idx >= len(preorder) or preorder[self.idx] > bound:
                return None

            root = TreeNode(preorder[self.idx])
            self.idx += 1

            root.left = build(root.val)
            root.right = build(bound)

            return root

        return build(float("inf"))


def main():
    solution = BSTFromPreOrder()
    preorder = [8, 5, 1, 7, 10, 12]
    root = solution.bst_from_preorder(preorder)

    # Print tree values in-order to verify
    def inorder(node):
        if node:
            inorder(node.left)
            print(node.val, end=" ")
            inorder(node.right)

    inorder(root)


if __name__ == "__main__":
    main()
