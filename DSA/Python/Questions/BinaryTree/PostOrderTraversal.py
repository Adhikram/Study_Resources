"""
# Question: Binary Tree Postorder Traversal
# Link: https://leetcode.com/problems/binary-tree-postorder-traversal/

# Time Complexity: O(N)
# Space Complexity: O(H)

# Algorithm:
# 1. Left -> Right -> Root traversal
# 2. Iterative and recursive solutions
# 3. Track visited nodes
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class PostOrderTraversal:
    def postorder_recursive(self, root: TreeNode) -> list[int]:
        result = []

        def dfs(node: TreeNode) -> None:
            if node:
                dfs(node.left)
                dfs(node.right)
                result.append(node.val)

        dfs(root)
        return result

    def postorder_iterative(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        result = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if visited:
                result.append(node.val)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return result


def main():
    solution = PostOrderTraversal()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(solution.postorder_recursive(root))
    print(solution.postorder_iterative(root))


if __name__ == "__main__":
    main()
