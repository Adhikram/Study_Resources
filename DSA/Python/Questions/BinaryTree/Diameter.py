"""
# Question: Diameter of Binary Tree
# Link: https://leetcode.com/problems/diameter-of-binary-tree/

# Time Complexity: O(N)
# Space Complexity: O(H)

# Algorithm:
# 1. DFS traversal
# 2. Track max diameter
# 3. Return height at each node
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Diameter:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        self.diameter = 0

        def height(node: TreeNode) -> int:
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            self.diameter = max(self.diameter, left_height + right_height)
            return max(left_height, right_height) + 1

        height(root)
        return self.diameter


def main():
    solution = Diameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.diameter_of_binary_tree(root))


if __name__ == "__main__":
    main()
