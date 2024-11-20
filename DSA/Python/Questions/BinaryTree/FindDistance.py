"""
# Question: Find Distance Between Two Nodes
# Find the shortest path distance between two nodes in a binary tree

# Time Complexity: O(N)
# Space Complexity: O(H)

# Algorithm:
# 1. Find LCA of nodes
# 2. Calculate distance from LCA to nodes
# 3. Return total distance
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class FindDistance:
    def find_distance(self, root: TreeNode, p: int, q: int) -> int:
        def find_lca(node: TreeNode) -> TreeNode:
            if not node or node.val == p or node.val == q:
                return node

            left = find_lca(node.left)
            right = find_lca(node.right)

            if left and right:
                return node
            return left if left else right

        def find_level(node: TreeNode, target: int, level: int) -> int:
            if not node:
                return -1
            if node.val == target:
                return level

            left = find_level(node.left, target, level + 1)
            if left != -1:
                return left
            return find_level(node.right, target, level + 1)

        lca = find_lca(root)
        if not lca:
            return -1

        d1 = find_level(lca, p, 0)
        d2 = find_level(lca, q, 0)

        return d1 + d2


def main():
    solution = FindDistance()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    print(solution.find_distance(root, 5, 1))


if __name__ == "__main__":
    main()
