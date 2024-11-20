"""
# Question: Reverse Nodes in k-Group
# Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

# Reverse linked list nodes in groups of k

# Time Complexity: O(n) where n is length of list
# Space Complexity: O(n/k) for recursion stack

# Algorithm:
# 1. Check if k nodes exist ahead
# 2. Reverse k nodes using three pointers
# 3. Recursively handle remaining groups
# 4. Connect reversed groups

# Key Components:
# - ListNode class for linked list structure
# - reverse_k_group(): Main reversal implementation
# - Group validation and reversal logic
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ReverseKGroups:
    def reverse_k_group(self, head: ListNode, k: int) -> ListNode:
        # Check if k nodes exist
        curr = head
        for i in range(k):
            if not curr:
                return head
            curr = curr.next

        # Reverse k nodes
        curr = head
        prev = None
        temp = None
        count = 0

        while curr and count < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1

        # Connect with remaining reversed groups
        if curr:
            head.next = self.reverse_k_group(curr, k)

        return prev


def main():
    solution = ReverseKGroups()

    # Create test list: 1->2->3->4->5->6
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    # Reverse in groups of 2
    result = solution.reverse_k_group(head, 2)

    # Print result
    while result:
        print(result.val)
        result = result.next


if __name__ == "__main__":
    main()
