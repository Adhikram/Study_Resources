"""
# Question: Sort List
# Link: https://leetcode.com/problems/sort-list/

# Sort a linked list using merge sort

# Time Complexity: O(n log n)
# Space Complexity: O(log n) for recursion stack

# Algorithm:
# 1. Split list into two halves using slow/fast pointers
# 2. Recursively sort each half
# 3. Merge sorted halves
# 4. Return sorted list

# Key Components:
# - ListNode class for linked list structure
# - sort_list(): Main sorting implementation
# - merge(): Helper for combining sorted lists
# - get_middle(): Helper for finding list middle
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SortList:
    def sort_list(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Get middle of list
        middle = self.get_middle(head)
        right = middle.next
        middle.next = None

        # Recursively sort both halves
        left = self.sort_list(head)
        right = self.sort_list(right)

        # Merge sorted halves
        return self.merge(left, right)

    def get_middle(self, head: ListNode) -> ListNode:
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        return prev if fast else slow

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2
        return dummy.next


def main():
    solution = SortList()

    # Create test list: 4->2->1->3
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    # Sort list
    result = solution.sort_list(head)

    # Print sorted list
    while result:
        print(result.val, end=" ")
        result = result.next


if __name__ == "__main__":
    main()
