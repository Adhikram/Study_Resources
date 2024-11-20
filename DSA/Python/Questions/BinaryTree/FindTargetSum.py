"""
# Question: Path Sum III
# Link: https://leetcode.com/problems/path-sum-iii/

# Time Complexity: O(N)
# Space Complexity: O(H)

# Algorithm:
# 1. Use prefix sum technique
# 2. DFS traversal with path sum tracking
# 3. Count valid paths
"""

from collections import defaultdict


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class FindTargetSum:
    def path_sum(self, root: TreeNode, target_sum: int) -> int:
        self.count = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        def dfs(node: TreeNode, curr_sum: int) -> None:
            if not node:
                return

            curr_sum += node.val
            self.count += prefix_sum[curr_sum - target_sum]
            prefix_sum[curr_sum] += 1

            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

            prefix_sum[curr_sum] -= 1

        dfs(root, 0)
        return self.count


def main():
    solution = FindTargetSum()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    print(solution.path_sum(root, 8))


if __name__ == "__main__":
    main()
