"""
# Question: All O(1) Data Structure
# Link: https://leetcode.com/problems/all-one-data-structure/

# Design a data structure supporting string operations with O(1) time complexity

# Time Complexity: O(1) for all operations
# Space Complexity: O(n) where n is number of unique strings

# Key Features:
# 1. String frequency tracking
# 2. Get maximum/minimum frequency strings
# 3. Increment/decrement string counts

# Components:
# - DoublyLinkedList for frequency tracking
# - HashMap for string-node mapping
# - CountNode for frequency nodes
"""


class CountNode:
    def __init__(self, count: int):
        self.count = count
        self.prev = None
        self.next = None


class ListNode(CountNode):
    def __init__(self, key: str, count: int):
        super().__init__(count)
        self.key = key


class DoublyLinkedList:
    def __init__(self):
        self.head = CountNode(-1)
        self.tail = CountNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_first(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get_last(self):
        return None if self.is_empty() else self.tail.prev

    def get_first(self):
        return None if self.is_empty() else self.head.next

    def is_empty(self):
        return self.head.next == self.tail


class AllOne:
    def __init__(self):
        self.key_to_node = {}
        self.count_to_list = {}
        self.count_to_node = {}
        self.count_list = DoublyLinkedList()

    def inc(self, key: str) -> None:
        if key in self.key_to_node:
            self._handle_existing_key_increment(key)
        else:
            self._handle_new_key(key)

    def dec(self, key: str) -> None:
        node = self.key_to_node[key]
        if node.count == 1:
            del self.key_to_node[key]
        else:
            self._handle_decrement(node)

    def get_max_key(self) -> str:
        if self.count_list.is_empty():
            return ""
        return self.count_to_list[self.count_list.get_last().count].get_first().key

    def get_min_key(self) -> str:
        if self.count_list.is_empty():
            return ""
        return self.count_to_list[self.count_list.get_first().count].get_first().key


def main():
    all_one = AllOne()
    all_one.inc("hello")
    all_one.inc("hello")
    print(all_one.get_max_key())  # hello
    print(all_one.get_min_key())  # hello
    all_one.inc("leet")
    print(all_one.get_max_key())  # hello
    print(all_one.get_min_key())  # leet


if __name__ == "__main__":
    main()
