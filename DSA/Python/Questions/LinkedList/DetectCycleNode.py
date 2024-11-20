"""
# Question: Linked List Cycle II
# Link: https://leetcode.com/problems/linked-list-cycle-ii/

# Find the node where cycle begins in a linked list

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Use Floyd's Cycle Detection (fast/slow pointers)
# 2. When pointers meet, reset head pointer
# 3. Move head and slow pointers at same speed
# 4. Meeting point is cycle start

# Key Components:
# - ListNode class for linked list structure
# - detect_cycle(): Main cycle detection implementation
# - Two-pointer technique
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DetectCycleNode:
    def detect_cycle(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        while head != slow:
            slow = slow.next
            head = head.next

        return head


def main():
    solution = DetectCycleNode()

    # Create test list with cycle: 1->2->3->4->5->6->3
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = head.next.next  # Creates cycle

    cycle_node = solution.detect_cycle(head)
    print(f"Cycle starts at node with value: {cycle_node.val}")


if __name__ == "__main__":
    main()
