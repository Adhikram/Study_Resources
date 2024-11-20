"""
# Question: Serialize and Deserialize Binary Tree
# Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Time Complexity: O(N)
# Space Complexity: O(N)

# Algorithm:
# 1. Preorder traversal for serialization
# 2. String parsing for deserialization
# 3. Null marker handling
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return "null"
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

    def deserialize(self, data: str) -> TreeNode:
        def dfs() -> TreeNode:
            val = next(values)
            if val == "null":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        values = iter(data.split(","))
        return dfs()


def main():
    codec = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    serialized = codec.serialize(root)
    print(serialized)
    deserialized = codec.deserialize(serialized)
    print(codec.serialize(deserialized))


if __name__ == "__main__":
    main()
