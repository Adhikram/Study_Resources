"""
# Question: Vertical View of Binary Tree
# Print nodes visible from vertical view

# Time Complexity: O(N log N)
# Space Complexity: O(N)

# Algorithm:
# 1. Level order traversal with horizontal distance
# 2. Track nodes at each vertical line
# 3. Return first visible node at each level
"""

from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class VerticalView:
    def vertical_view(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        column_table = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()
            column_table[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        return [column_table[x][0] for x in sorted(column_table.keys())]


def main():
    solution = VerticalView()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.vertical_view(root))


if __name__ == "__main__":
    main()
