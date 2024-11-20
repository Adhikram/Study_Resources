"""
# Question: Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/

# Add two numbers represented by linked lists in reverse order

# Time Complexity: O(max(m,n)) where m,n are lengths of lists
# Space Complexity: O(max(m,n)) for result list

# Algorithm:
# 1. Traverse both lists simultaneously
# 2. Add digits with carry
# 3. Create new nodes for sum
# 4. Handle remaining carry

# Key Components:
# - ListNode class for linked list structure
# - add_two_numbers(): Main addition implementation
# - Carry handling between digits
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)
        result = head

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            current_sum = l1_val + l2_val + carry
            carry = current_sum // 10

            head.next = ListNode(current_sum % 10)
            head = head.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            head.next = ListNode(carry)

        return result.next


def main():
    solution = AddTwoNumbers()

    # Create first number: 342
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    # Create second number: 465
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    # Calculate sum
    result = solution.add_two_numbers(l1, l2)

    # Print result
    while result:
        print(result.val, end=" ")
        result = result.next


if __name__ == "__main__":
    main()
