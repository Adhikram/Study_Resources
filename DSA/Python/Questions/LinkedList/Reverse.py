"""
# Question: Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/

# Reverse a singly linked list iteratively

# Time Complexity: O(n) where n is length of list
# Space Complexity: O(1)

# Algorithm:
# 1. Use three pointers: prev, current, and next
# 2. Iterate through list reversing links
# 3. Update pointers in each iteration
# 4. Return new head (prev)

# Key Components:
# - ListNode class for linked list structure
# - reverse_list(): Main reversal implementation
# - Iterative pointer manipulation
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Reverse:
    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            # Store next node
            temp = head.next
            # Reverse the link
            head.next = prev
            # Move prev and head one step forward
            prev = head
            head = temp

        return prev


def main():
    solution = Reverse()

    # Create test list: 1->2->3->4->5->6
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    # Reverse list
    reversed_list = solution.reverse_list(head)

    # Print reversed list
    while reversed_list:
        print(reversed_list.val)
        reversed_list = reversed_list.next


if __name__ == "__main__":
    main()
