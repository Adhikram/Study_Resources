"""
# Question: LFU (Least Frequently Used) Cache
# Link: https://leetcode.com/problems/lfu-cache/

# Design Goals:
# 1. O(1) time complexity for all operations
# 2. Maintain frequency count for each key
# 3. Evict least frequently used items
# 4. Use LRU strategy for ties in frequency

# Data Structure Design:
# - key_map: Maps keys to nodes for direct access
# - count_map: Maps frequencies to node lists
# - Doubly linked list for O(1) node removal
# - Frequency tracking within nodes

# Implementation Details:
# 1. Node Structure:
#    - key: unique identifier
#    - data: stored value
#    - count: access frequency
#    - left/right: pointers for doubly linked list
#
# 2. Cache Operations:
#    - get(): Retrieve value and update frequency
#    - put(): Insert/update value and manage capacity
#    - shift_node(): Handle frequency updates
#    - delete_node(): Remove nodes during eviction
"""


class Node:
    def __init__(self, key=0, data=0):
        self.data = data  # Stored value
        self.count = 1  # Initial frequency count
        self.key = key  # Unique identifier
        self.left = None  # Previous node pointer
        self.right = None  # Next node pointer


class LFUCache:
    def __init__(self, capacity: int):
        # Initialize cache structure
        self.key_map = [None] * 100005  # Direct key to node mapping
        self.count_map = [None] * 10005  # Frequency to node mapping
        self.head = Node(-1, -1)  # Dummy head node
        self.tail = Node(0, 1)  # Dummy tail node
        self.capacity = capacity  # Maximum cache size
        self.current_size = 0  # Current number of items

        # Connect head and tail
        self.head.right = self.tail
        self.tail.left = self.head
        self.count_map[1] = self.tail  # Initialize frequency 1 list

    def get(self, key: int) -> int:
        # Return -1 if key doesn't exist
        if not self.key_map[key]:
            return -1

        # Update frequency and return value
        node = self.key_map[key]
        self._shift_node(node, node.data)
        return node.data

    def put(self, key: int, value: int) -> None:
        # Case 1: Key exists - update value and frequency
        if self.key_map[key]:
            self._shift_node(self.key_map[key], value)
            return

        # Case 2: Cache is full - remove LFU item and add new one
        if self.current_size == self.capacity:
            self._delete_node(self.tail.left.key, self.tail.left)
            self._add_node(key, value)
            return

        # Case 3: Cache has space - add new item
        self._add_node(key, value)
        self.current_size += 1

    def _delete_node(self, key: int, node: Node) -> None:
        # Get current frequency count
        count = node.count

        # Update frequency map if this was the only node
        if self.count_map[count] == node:
            self.count_map[count] = None

        # Ensure frequency 1 always has a reference
        if not self.count_map[1]:
            self.count_map[1] = self.tail

        # Remove node from doubly linked list
        node.left.right = node.right
        node.right.left = node.left

        # Remove key mapping
        self.key_map[key] = None

    def _add_node(self, key: int, value: int) -> None:
        # Create new node
        node = Node(key, value)

        # Get reference node for frequency 1
        ref_node = self.count_map[1]
        self.count_map[1] = node

        # Insert node in doubly linked list
        ref_node.left.right = node
        node.left = ref_node.left
        node.right = ref_node
        ref_node.left = node

        # Update key mapping
        self.key_map[key] = node

    def _shift_node(self, node: Node, value: int) -> None:
        # Increment frequency count
        node.count += 1
        count = node.count
        node.data = value

        # Get adjacent nodes
        prev_node = node.right
        ref_node = (
            self.count_map[count]
            if self.count_map[count]
            else self.count_map[count - 1]
        )

        # Reposition node if needed
        if ref_node != node:
            # Remove from current position
            node.left.right = node.right
            node.right.left = node.left

            # Insert at new position
            node.left = ref_node.left
            node.right = ref_node
            ref_node.left.right = node
            ref_node.left = node

        # Update frequency mappings
        if self.count_map[count - 1] == node:
            if prev_node.count == count - 1:
                self.count_map[prev_node.count] = prev_node
            else:
                self.count_map[count - 1] = None

        self.count_map[count] = node


def main():
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    print(cache.get(3))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))


if __name__ == "__main__":
    main()
