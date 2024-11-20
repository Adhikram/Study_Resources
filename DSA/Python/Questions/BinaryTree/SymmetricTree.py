"""
# Question: Symmetric Tree
# Link: https://leetcode.com/problems/symmetric-tree/

# Time Complexity: O(N)
# Space Complexity: O(H)

# Algorithm:
# 1. Mirror comparison
# 2. Recursive check
# 3. Compare left and right subtrees
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class SymmetricTree:
    def is_symmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def mirror(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (
                left.val == right.val
                and mirror(left.left, right.right)
                and mirror(left.right, right.left)
            )

        return mirror(root.left, root.right)


def main():
    solution = SymmetricTree()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    print(solution.is_symmetric(root))


if __name__ == "__main__":
    main()
