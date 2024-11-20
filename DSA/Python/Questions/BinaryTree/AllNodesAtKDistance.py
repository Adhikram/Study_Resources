"""
# Question: All Nodes Distance K in Binary Tree
# Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Time Complexity: O(N)
# Space Complexity: O(N)

# Algorithm:
# 1. Build parent pointers using DFS
# 2. BFS from target node
# 3. Track visited nodes
# 4. Return nodes at distance k
"""

from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class AllNodesAtKDistance:
    def distance_k(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Build parent pointers
        parent = defaultdict(TreeNode)

        def dfs(node: TreeNode, prev: TreeNode) -> None:
            if node:
                parent[node] = prev
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root, None)

        # BFS from target
        queue = deque([(target, 0)])
        seen = {target}
        result = []

        while queue:
            node, dist = queue.popleft()

            if dist == k:
                result.append(node.val)

            for next_node in (node.left, node.right, parent[node]):
                if next_node and next_node not in seen and dist < k:
                    seen.add(next_node)
                    queue.append((next_node, dist + 1))

        return result


def main():
    solution = AllNodesAtKDistance()
    # Create test tree and run example
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    print(solution.distance_k(root, root.left, 2))


if __name__ == "__main__":
    main()
