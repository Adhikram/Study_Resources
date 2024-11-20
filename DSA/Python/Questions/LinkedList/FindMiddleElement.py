"""
# Question: Middle of the Linked List
# Link: https://leetcode.com/problems/middle-of-the-linked-list/

# Find the middle node of a linked list

# Time Complexity: O(n) where n is number of nodes
# Space Complexity: O(1)

# Algorithm:
# 1. Use fast and slow pointers
# 2. Move fast pointer twice as fast as slow
# 3. When fast reaches end, slow is at middle
# 4. Handle both even and odd length lists

# Key Components:
# - ListNode class for linked list structure
# - middle_node(): Main middle finding implementation
# - Two-pointer technique
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class FindMiddleElement:
    def middle_node(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            if not fast:
                return slow
            slow = slow.next

        return slow


def main():
    solution = FindMiddleElement()

    # Create test list: 1->2->3->4->5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    result = solution.middle_node(head)
    print(f"Middle node value: {result.val}")


if __name__ == "__main__":
    main()
