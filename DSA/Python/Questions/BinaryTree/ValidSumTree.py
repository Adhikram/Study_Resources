"""
# Question: Binary Tree Sum Tree Validation
# Check if tree is a valid sum tree where each node equals sum of its children

# Time Complexity: O(N)
# Space Complexity: O(H)

# Algorithm:
# 1. Post-order traversal
# 2. Validate sum property
# 3. Return sum of subtree
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class ValidSumTree:
    def is_sum_tree(self, root: TreeNode) -> bool:
        def validate(node: TreeNode) -> tuple[bool, int]:
            if not node:
                return True, 0
            if not node.left and not node.right:
                return True, node.val

            is_left_valid, left_sum = validate(node.left)
            is_right_valid, right_sum = validate(node.right)

            is_current_valid = node.val == left_sum + right_sum
            return (
                is_left_valid and is_right_valid and is_current_valid,
                node.val + left_sum + right_sum,
            )

        return validate(root)[0]


def main():
    solution = ValidSumTree()
    root = TreeNode(26)
    root.left = TreeNode(10)
    root.right = TreeNode(3)
    print(solution.is_sum_tree(root))


if __name__ == "__main__":
    main()
