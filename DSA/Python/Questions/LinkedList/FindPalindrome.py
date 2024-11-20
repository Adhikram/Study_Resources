"""
# Question: Palindrome Linked List
# Link: https://leetcode.com/problems/palindrome-linked-list/

# Check if a linked list is a palindrome

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Find middle using fast/slow pointers
# 2. Reverse second half of list
# 3. Compare first half with reversed second half
# 4. Return true if values match

# Key Components:
# - ListNode class for linked list structure
# - is_palindrome(): Main palindrome check implementation
# - Two-pointer and reversal techniques
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class FindPalindrome:
    def is_palindrome(self, head: ListNode) -> bool:
        slow = fast = head

        # Find middle
        while fast and fast.next:
            fast = fast.next.next
            if not fast:
                break
            slow = slow.next

        # Reverse second half
        prev = slow
        slow = slow.next
        prev.next = None

        while slow:
            next_elem = slow.next
            slow.next = prev
            prev = slow
            slow = next_elem

        # Compare halves
        fast = head
        slow = prev
        while slow and fast:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next

        return True


def main():
    solution = FindPalindrome()

    # Create test list: 1->2->3->4->3->2->1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(2)
    head.next.next.next.next.next.next = ListNode(1)

    result = solution.is_palindrome(head)
    print(f"Is palindrome: {result}")


if __name__ == "__main__":
    main()
