"""
# Question: Count Nodes Equal to Average of Subtree
# Link: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Time Complexity: O(N)
# Space Complexity: O(H)

# Algorithm:
# 1. DFS traversal
# 2. Track sum and count of nodes
# 3. Calculate average at each node
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class CountOfAverageSubtree:
    def average_of_subtree(self, root: TreeNode) -> int:
        self.result = 0

        def dfs(node: TreeNode) -> tuple[int, int]:
            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            curr_sum = node.val + left_sum + right_sum
            curr_count = 1 + left_count + right_count

            if curr_sum // curr_count == node.val:
                self.result += 1

            return curr_sum, curr_count

        dfs(root)
        return self.result


def main():
    solution = CountOfAverageSubtree()
    root = TreeNode(4)
    root.left = TreeNode(8)
    root.right = TreeNode(5)
    print(solution.average_of_subtree(root))


if __name__ == "__main__":
    main()
