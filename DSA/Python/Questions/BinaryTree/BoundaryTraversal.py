"""
# Question: Boundary Traversal of Binary Tree
# Print boundary nodes of a binary tree in anti-clockwise order

# Time Complexity: O(N)
# Space Complexity: O(N)

# Algorithm:
# 1. Print left boundary (excluding leaves)
# 2. Print leaves
# 3. Print right boundary in reverse
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class BoundaryTraversal:
    def print_boundary(self, root: TreeNode) -> list[int]:
        result = []
        if not root:
            return result

        result.append(root.val)

        def left_boundary(node: TreeNode) -> None:
            if not node or (not node.left and not node.right):
                return
            result.append(node.val)
            if node.left:
                left_boundary(node.left)
            elif node.right:
                left_boundary(node.right)

        def leaves(node: TreeNode) -> None:
            if not node:
                return
            if not node.left and not node.right:
                result.append(node.val)
                return
            leaves(node.left)
            leaves(node.right)

        def right_boundary(node: TreeNode) -> list[int]:
            if not node or (not node.left and not node.right):
                return []
            if node.right:
                values = right_boundary(node.right)
            elif node.left:
                values = right_boundary(node.left)
            else:
                values = []
            values.append(node.val)
            return values

        if root.left:
            left_boundary(root.left)
        if root.left or root.right:
            leaves(root)
        if root.right:
            result.extend(right_boundary(root.right))

        return result


def main():
    solution = BoundaryTraversal()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.print_boundary(root))


if __name__ == "__main__":
    main()
