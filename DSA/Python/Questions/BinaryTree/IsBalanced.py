"""
# Question: Balanced Binary Tree
# Link: https://leetcode.com/problems/balanced-binary-tree/

# Time Complexity: O(N)
# Space Complexity: O(H)

# Algorithm:
# 1. Check height difference
# 2. Bottom-up approach
# 3. Return -1 for unbalanced
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class IsBalanced:
    def is_balanced(self, root: TreeNode) -> bool:
        def check_height(node: TreeNode) -> int:
            if not node:
                return 0

            left = check_height(node.left)
            if left == -1:
                return -1

            right = check_height(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return check_height(root) != -1


def main():
    solution = IsBalanced()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    print(solution.is_balanced(root))


if __name__ == "__main__":
    main()
