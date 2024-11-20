"""
# Question: LRU (Least Recently Used) Cache
# Link: https://leetcode.com/problems/lru-cache/

# Design Goals:
# 1. O(1) time complexity for all operations
# 2. Track most recently used items
# 3. Evict least recently used items when capacity is reached

# Time Complexity: O(1) for all operations
# Space Complexity: O(capacity)

# Key Components:
# - Node class for doubly linked list
# - HashMap for O(1) key access
# - Doubly linked list for O(1) removal/insertion
"""


class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # Initialize cache structure
        self.capacity = capacity
        self.cache_map = {}

        # Create dummy head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # Return value if key exists and update position
        if key in self.cache_map:
            node = self.cache_map[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        # Remove existing key if present
        if key in self.cache_map:
            self._remove(self.cache_map[key])

        # Evict least recently used if at capacity
        if len(self.cache_map) == self.capacity:
            self._remove(self.tail.prev)

        # Add new node
        self._insert(Node(key, value))

    def _remove(self, node: Node) -> None:
        # Remove node from cache map
        del self.cache_map[node.key]

        # Update doubly linked list pointers
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node: Node) -> None:
        # Add to cache map
        self.cache_map[node.key] = node

        # Insert at head of doubly linked list
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head


def main():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # returns 1
    cache.put(3, 3)  # evicts key 2
    print(cache.get(2))  # returns -1 (not found)
    cache.put(4, 4)  # evicts key 1
    print(cache.get(1))  # returns -1 (not found)
    print(cache.get(3))  # returns 3
    print(cache.get(4))  # returns 4


if __name__ == "__main__":
    main()
