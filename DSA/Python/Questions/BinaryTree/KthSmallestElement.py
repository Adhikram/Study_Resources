"""
# Question: Kth Smallest Element in a BST
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Time Complexity: O(H + k)
# Space Complexity: O(H)

# Algorithm:
# 1. Inorder traversal
# 2. Track count
# 3. Return kth element
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class KthSmallestElement:
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.result = 0

        def inorder(node: TreeNode) -> None:
            if not node:
                return

            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.result


def main():
    solution = KthSmallestElement()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    print(solution.kth_smallest(root, 1))


if __name__ == "__main__":
    main()
