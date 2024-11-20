"""
# Question: Count of Range Sum
# Track range of values in a stream

# Time Complexity: O(log N) per operation
# Space Complexity: O(N)

# Algorithm:
# 1. BST implementation
# 2. Track count of values in range
# 3. Update counts during insertion
"""


class Node:
    def __init__(self, val: int):
        self.val = val
        self.count = 1
        self.left = None
        self.right = None


class RangeValuesFromStream:
    def __init__(self):
        self.root = None

    def track(self, num: int) -> None:
        self.root = self._insert(self.root, num)

    def _insert(self, node: Node, val: int) -> Node:
        if not node:
            return Node(val)

        if val == node.val:
            node.count += 1
        elif val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)

        return node

    def count_range(self, low: int, high: int) -> int:
        return self._count_range(self.root, low, high)

    def _count_range(self, node: Node, low: int, high: int) -> int:
        if not node:
            return 0

        if low <= node.val <= high:
            return (
                node.count
                + self._count_range(node.left, low, high)
                + self._count_range(node.right, low, high)
            )
        elif node.val < low:
            return self._count_range(node.right, low, high)
        else:
            return self._count_range(node.left, low, high)


def main():
    solution = RangeValuesFromStream()
    solution.track(5)
    solution.track(3)
    solution.track(7)
    print(solution.count_range(3, 6))


if __name__ == "__main__":
    main()
