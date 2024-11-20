"""
# Question: Unique Binary Search Trees II
# Link: https://leetcode.com/problems/unique-binary-search-trees-ii/

# Generate all structurally unique BSTs with values 1 to n

# Time Complexity: O(4^n)
# Space Complexity: O(4^n)

# Algorithm:
# 1. Generate all possible root values
# 2. Recursively build left and right subtrees
# 3. Combine subtrees with root
# 4. Return all unique BSTs

# Key Components:
# - TreeNode class for BST structure
# - generate_trees(): Main implementation
# - generate_subtrees(): Recursive helper
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class UniqueBinarySearchTree:
    def generate_trees(self, n: int) -> list[TreeNode]:
        return self.generate_subtrees(1, n)

    def generate_subtrees(self, start: int, end: int) -> list[TreeNode]:
        result = []

        if start > end:
            result.append(None)
            return result

        for i in range(start, end + 1):
            left_subtrees = self.generate_subtrees(start, i - 1)
            right_subtrees = self.generate_subtrees(i + 1, end)

            for left in left_subtrees:
                for right in right_subtrees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    result.append(root)

        return result


def main():
    solution = UniqueBinarySearchTree()
    result = solution.generate_trees(3)
    print(f"Number of unique BSTs: {len(result)}")


if __name__ == "__main__":
    main()
