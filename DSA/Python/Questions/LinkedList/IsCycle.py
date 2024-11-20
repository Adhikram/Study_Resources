"""
# Question: Linked List Cycle
# Link: https://leetcode.com/problems/linked-list-cycle/

# Detect if a linked list has a cycle

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Use fast and slow pointers
# 2. Fast moves two steps, slow moves one step
# 3. If pointers meet, cycle exists
# 4. If fast reaches end, no cycle

# Key Components:
# - ListNode class for linked list structure
# - has_cycle(): Main cycle detection implementation
# - Two-pointer technique (Floyd's Cycle Detection)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class IsCycle:
    def has_cycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow.next and fast.next:
            slow = slow.next
            if not fast.next.next:
                break
            fast = fast.next.next

            if slow == fast:
                return True

        return False


def main():
    solution = IsCycle()

    # Create test list with cycle: 3->2->0->-4->2
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next  # Create cycle

    result = solution.has_cycle(head)
    print(f"Has cycle: {result}")


if __name__ == "__main__":
    main()
