"""
# Question: Second Minimum Node In a Binary Tree
# Link: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

# Time Complexity: O(N)
# Space Complexity: O(H)

# Algorithm:
# 1. Track minimum and second minimum
# 2. DFS traversal
# 3. Update values during traversal
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class FindSecondMinimumValue:
    def find_second_minimum_value(self, root: TreeNode) -> int:
        self.min1 = root.val
        self.ans = float("inf")

        def dfs(node: TreeNode) -> None:
            if node:
                if self.min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == self.min1:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float("inf") else -1


def main():
    solution = FindSecondMinimumValue()
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    print(solution.find_second_minimum_value(root))


if __name__ == "__main__":
    main()
