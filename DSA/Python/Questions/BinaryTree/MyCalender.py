"""
# Question: My Calendar I
# Link: https://leetcode.com/problems/my-calendar-i/

# Time Complexity: O(log N) per operation
# Space Complexity: O(N)

# Algorithm:
# 1. BST implementation
# 2. Check for overlapping intervals
# 3. Insert new bookings
"""


class Node:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True

        return self._insert(self.root, start, end)

    def _insert(self, node: Node, start: int, end: int) -> bool:
        if start >= node.end:
            if node.right:
                return self._insert(node.right, start, end)
            node.right = Node(start, end)
            return True

        if end <= node.start:
            if node.left:
                return self._insert(node.left, start, end)
            node.left = Node(start, end)
            return True

        return False


def main():
    calendar = MyCalendar()
    print(calendar.book(10, 20))  # True
    print(calendar.book(15, 25))  # False
    print(calendar.book(20, 30))  # True


if __name__ == "__main__":
    main()
