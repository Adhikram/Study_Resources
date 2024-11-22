"""
# Question: LRU (Least Recently Used) Cache
# Link: https://leetcode.com/problems/lru-cache/

# Problem Statement:
# Design a data structure that implements the LRU cache with the following operations:
# - get(key): Get the value of the key if it exists in the cache
# - put(key, value): Set or insert the value if the key is not already present
# When the cache reaches its capacity, it should invalidate the least recently used item.

# Example:
# Input: 
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output: [null, null, null, 1, null, -1, null, -1, 3, 4]
"""

from collections import OrderedDict


class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCacheDoublyLinkedList:
    """Implementation using Doubly Linked List and HashMap"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru_node = self.head.next
            self._remove(lru_node)
            del self.cache[lru_node.key]

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node: Node) -> None:
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail


class LRUCacheOrderedDict:
    """Implementation using OrderedDict"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


def test_lru_cache(implementation, operations, inputs):
    """Helper function to test LRU cache implementations"""
    results = []
    cache = None

    for op, args in zip(operations, inputs):
        if op == "LRUCache":
            cache = implementation(args[0])
            results.append(None)
        elif op == "put":
            results.append(cache.put(args[0], args[1]))
        else:  # get
            results.append(cache.get(args[0]))

    return results


def main():
    test_cases = [
        {
            "operations": [
                "LRUCache",
                "put",
                "put",
                "get",
                "put",
                "get",
                "put",
                "get",
                "get",
                "get",
            ],
            "inputs": [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            "expected": [None, None, None, 1, None, -1, None, -1, 3, 4],
        },
        {
            "operations": ["LRUCache", "put", "get"],
            "inputs": [[1], [2, 1], [2]],
            "expected": [None, None, 1],
        },
    ]

    implementations = [LRUCacheDoublyLinkedList, LRUCacheOrderedDict]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Operations: {test['operations']}")
        print(f"Inputs: {test['inputs']}")
        print(f"Expected: {test['expected']}")

        for impl in implementations:
            results = test_lru_cache(impl, test["operations"], test["inputs"])
            print(f"{impl.__name__} Results: {results}")
            assert (
                results == test["expected"]
            ), f"Test case {i + 1} failed for {impl.__name__}"


if __name__ == "__main__":
    main()
