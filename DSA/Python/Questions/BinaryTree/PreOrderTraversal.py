"""
# Question: Binary Tree Preorder Traversal
# Link: https://leetcode.com/problems/binary-tree-preorder-traversal/

# Time Complexity: O(N)
# Space Complexity: O(H)

# Algorithm:
# 1. Root -> Left -> Right traversal
# 2. Iterative and recursive solutions
# 3. Morris traversal option
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class PreOrderTraversal:
    def preorder_recursive(self, root: TreeNode) -> list[int]:
        result = []

        def dfs(node: TreeNode) -> None:
            if node:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return result

    def preorder_iterative(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result


def main():
    solution = PreOrderTraversal()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(solution.preorder_recursive(root))
    print(solution.preorder_iterative(root))


if __name__ == "__main__":
    main()
