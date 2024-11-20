"""
# Question: Lowest Common Ancestor of a Binary Tree
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Time Complexity: O(N)
# Space Complexity: O(H)

# Algorithm:
# 1. DFS traversal
# 2. Find both nodes
# 3. Return LCA node
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class LowestCommonAncestor:
    def lowest_common_ancestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if not root or root == p or root == q:
            return root

        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right


def main():
    solution = LowestCommonAncestor()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    print(solution.lowest_common_ancestor(root, root.left, root.right).val)


if __name__ == "__main__":
    main()
