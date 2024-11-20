"""
# Question: Copy List with Random Pointer
# Link: https://leetcode.com/problems/copy-list-with-random-pointer/

# Create deep copy of linked list with random pointers

# Time Complexity: O(n)
# Space Complexity: O(n) for HashMap approach, O(1) for interweaving approach

# Two Solution Approaches:
# 1. HashMap Method:
#    - Map original nodes to copied nodes
#    - Connect random pointers using map
# 2. Interweaving Method:
#    - Create copied nodes between original nodes
#    - Set random pointers
#    - Separate lists

# Key Components:
# - Node class with random pointer
# - Two implementation methods
# - In-place list manipulation
"""


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class CopyRandomList:
    def copy_random_list(self, head: Node) -> Node:
        if not head:
            return head

        # Create mapping of original to copied nodes
        node_map = {}
        new_head = Node(head.val)
        node_map[head] = new_head
        tail = new_head
        temp = head.next

        # Create all nodes and map them
        while temp:
            new_node = Node(temp.val)
            tail.next = new_node
            tail = new_node
            node_map[temp] = new_node
            temp = temp.next

        # Set random pointers using map
        t = new_head
        while head:
            if head.random:
                t.random = node_map[head.random]
            t = t.next
            head = head.next

        return new_head

    def copy_random_node(self, head: Node) -> Node:
        if not head:
            return None

        # Create interweaved list
        temp = head
        while temp:
            new_node = Node(temp.val)
            new_node.next = temp.next
            temp.next = new_node
            temp = new_node.next

        # Set random pointers
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        # Separate lists
        new_head = head.next
        new_temp = new_head
        temp = head

        while temp:
            temp.next = new_temp.next
            if new_temp.next:
                new_temp.next = new_temp.next.next
            temp = temp.next
            new_temp = new_temp.next

        return new_head


def main():
    solution = CopyRandomList()

    # Create test list
    head = Node(7)
    head.next = Node(13)
    head.next.next = Node(11)
    head.next.next.next = Node(10)
    head.next.next.next.next = Node(1)

    # Test both methods
    result1 = solution.copy_random_list(head)
    result2 = solution.copy_random_node(head)

    # Print results
    while result1:
        print(f"Value: {result1.val}")
        result1 = result1.next


if __name__ == "__main__":
    main()
