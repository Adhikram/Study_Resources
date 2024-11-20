"""
# Question: Serialize and Deserialize N-ary Tree
# Link: https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

# Time Complexity: O(N)
# Space Complexity: O(N)

# Algorithm:
# 1. Level-order traversal for serialization
# 2. Queue-based deserialization
# 3. Handle multiple children
"""

from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []


class Codec:
    def serialize(self, root: Node) -> str:
        if not root:
            return ""

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            result.append(str(node.val))
            result.append(str(len(node.children)))
            queue.extend(node.children)

        return ",".join(result)

    def deserialize(self, data: str) -> Node:
        if not data:
            return None

        values = data.split(",")
        i = 0
        root = Node(int(values[i]))
        queue = deque([root])
        i += 2

        while queue and i < len(values):
            node = queue.popleft()
            num_children = int(values[i - 1])
            for _ in range(num_children):
                child = Node(int(values[i]))
                node.children.append(child)
                queue.append(child)
                i += 2

        return root


def main():
    codec = Codec()
    root = Node(1, [Node(3), Node(2), Node(4)])
    serialized = codec.serialize(root)
    print(serialized)
    deserialized = codec.deserialize(serialized)
    print(codec.serialize(deserialized))


if __name__ == "__main__":
    main()
