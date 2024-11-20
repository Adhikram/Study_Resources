"""
# Question: Binary Tree Root to Node Path
# Find path from root to given node

# Time Complexity: O(N)
# Space Complexity: O(H)

# Algorithm:
# 1. DFS traversal
# 2. Track path during traversal
# 3. Return path when node found
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class RootPath:
    def find_path(self, root: TreeNode, target: int) -> list[int]:
        path = []

        def dfs(node: TreeNode) -> bool:
            if not node:
                return False

            path.append(node.val)

            if node.val == target:
                return True

            if dfs(node.left) or dfs(node.right):
                return True

            path.pop()
            return False

        dfs(root)
        return path


def main():
    solution = RootPath()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.find_path(root, 2))


if __name__ == "__main__":
    main()
