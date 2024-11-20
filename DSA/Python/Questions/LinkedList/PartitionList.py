"""
# Question: Partition List
# Link: https://leetcode.com/problems/partition-list/

# Partition linked list around value x, maintaining relative order

# Time Complexity: O(n) where n is length of list
# Space Complexity: O(1)

# Algorithm:
# 1. Create two dummy heads for less and greater lists
# 2. Traverse original list and distribute nodes
# 3. Connect less list to greater list
# 4. Return merged result

# Key Components:
# - Node class for linked list structure
# - partition(): Main partitioning implementation
# - Two-list approach with dummy heads
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class PartitionList:
    def partition(self, head: Node, x: int) -> Node:
        # Create dummy heads
        less_head = Node(0)
        greater_head = Node(0)
        less = less_head
        greater = greater_head

        # Partition nodes
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next

        # Connect partitions
        greater.next = None
        less.next = greater_head.next

        return less_head.next


def main():
    # Create test list: 1->4->3->2->5->2, x = 3
    head = Node(1)
    head.next = Node(4)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(2)

    solution = PartitionList()
    result = solution.partition(head, 3)

    # Print result
    while result:
        print(result.val, end=" ")
        result = result.next


if __name__ == "__main__":
    main()
