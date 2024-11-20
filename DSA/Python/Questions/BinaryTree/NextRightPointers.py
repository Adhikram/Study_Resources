"""
# Question: Populating Next Right Pointers in Each Node
# Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Time Complexity: O(N)
# Space Complexity: O(1)

# Algorithm:
# 1. Level by level traversal
# 2. Use next pointers
# 3. Connect nodes at each level
"""


class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class NextRightPointers:
    def connect(self, root: Node) -> Node:
        if not root:
            return None

        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left

        return root


def main():
    solution = NextRightPointers()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    solution.connect(root)
    print(root.left.next.val)  # Should print 3


if __name__ == "__main__":
    main()
