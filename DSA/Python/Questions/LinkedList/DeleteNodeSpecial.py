"""
# Question: Delete Node in a Linked List
# Link: https://leetcode.com/problems/delete-node-in-a-linked-list/

# Delete a node (except the tail) in a singly linked list, given only access to that node

# Time Complexity: O(1)
# Space Complexity: O(1)

# Algorithm:
# 1. Copy next node's value to current node
# 2. Update current node's next pointer to skip next node
# 3. Effectively removes the next node while maintaining list structure

# Key Components:
# - ListNode class for linked list structure
# - delete_node(): Main deletion implementation
# - Value copying approach
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DeleteNodeSpecial:
    def delete_node(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next


def main():
    solution = DeleteNodeSpecial()

    # Create test list: 1->2->3->4->5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Delete node 3
    solution.delete_node(head.next.next)

    # Print result
    current = head
    while current:
        print(current.val)
        current = current.next


if __name__ == "__main__":
    main()
