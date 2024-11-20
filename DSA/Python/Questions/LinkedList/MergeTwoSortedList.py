"""
# Question: Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists/

# Merge two sorted linked lists into one sorted list

# Time Complexity: O(n + m) where n, m are lengths of lists
# Space Complexity: O(1) iterative, O(n + m) recursive

# Algorithm:
# 1. Compare nodes from both lists
# 2. Recursively build merged list
# 3. Handle remaining nodes
# 4. Return merged sorted list

# Key Components:
# - ListNode class for linked list structure
# - merge_two_lists(): Recursive merging implementation
# - Comparison-based node selection
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeTwoSortedList:
    def merge_two_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Base cases
        if not list1:
            return list2
        if not list2:
            return list1

        # Recursive merge
        if list1.val < list2.val:
            list1.next = self.merge_two_lists(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_two_lists(list1, list2.next)
            return list2


def main():
    solution = MergeTwoSortedList()

    # Create first sorted list: 1->2->4
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    # Create second sorted list: 1->3->4
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    # Merge lists
    merged = solution.merge_two_lists(list1, list2)

    # Print merged list
    while merged:
        print(merged.val)
        merged = merged.next


if __name__ == "__main__":
    main()
