"""
# Question: Binary Tree Inorder Traversal
# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

# Time Complexity: O(N)
# Space Complexity: O(H)

# Algorithm:
# 1. Iterative and recursive solutions
# 2. Morris traversal option
# 3. Left -> Root -> Right order
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class InOrderTraversal:
    def inorder_recursive(self, root: TreeNode) -> list[int]:
        result = []

        def dfs(node: TreeNode) -> None:
            if node:
                dfs(node.left)
                result.append(node.val)
                dfs(node.right)

        dfs(root)
        return result

    def inorder_iterative(self, root: TreeNode) -> list[int]:
        result = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result


def main():
    solution = InOrderTraversal()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(solution.inorder_recursive(root))
    print(solution.inorder_iterative(root))


if __name__ == "__main__":
    main()
