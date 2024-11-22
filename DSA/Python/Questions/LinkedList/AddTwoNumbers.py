"""
# Question: Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/

# Problem Statement:
# Given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each node contains a single digit.
# Add the two numbers and return the sum as a linked list.

# Example:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:
    def add_two_numbers_iterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Iterative approach to add two numbers represented as linked lists
        Time Complexity: O(max(N,M)) where N, M are lengths of input lists
        Space Complexity: O(max(N,M)) for the result list
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get values from the lists or use 0 if list ends
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate sum and new carry
            total = x + y + carry
            carry = total // 10

            # Create new node with sum digit
            current.next = ListNode(total % 10)
            current = current.next

            # Move to next nodes if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

    def add_two_numbers_recursive(
        self, l1: ListNode, l2: ListNode, carry: int = 0
    ) -> ListNode:
        """
        Recursive approach to add two numbers represented as linked lists
        Time Complexity: O(max(N,M))
        Space Complexity: O(max(N,M)) including recursion stack
        """
        if not l1 and not l2 and not carry:
            return None

        # Get values and calculate sum
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        total = x + y + carry

        # Create current node
        result = ListNode(total % 10)

        # Recursive call for next nodes
        next1 = l1.next if l1 else None
        next2 = l2.next if l2 else None
        result.next = self.add_two_numbers_recursive(next1, next2, total // 10)

        return result


def create_linked_list(arr: list) -> ListNode:
    """Helper function to create linked list from array"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(node: ListNode) -> list:
    """Helper function to convert linked list to array"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def main():
    test_cases = [
        {"l1": [2, 4, 3], "l2": [5, 6, 4], "expected": [7, 0, 8]},
        {"l1": [0], "l2": [0], "expected": [0]},
        {"l1": [9, 9, 9, 9], "l2": [9, 9, 9], "expected": [8, 9, 9, 0, 1]},
    ]

    solution = AddTwoNumbers()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        l1 = create_linked_list(test["l1"])
        l2 = create_linked_list(test["l2"])

        result_iterative = solution.add_two_numbers_iterative(l1, l2)
        result_recursive = solution.add_two_numbers_recursive(l1, l2)

        result_iter_arr = linked_list_to_array(result_iterative)
        result_rec_arr = linked_list_to_array(result_recursive)

        print(f"Input: l1 = {test['l1']}, l2 = {test['l2']}")
        print(f"Iterative Result: {result_iter_arr}")
        print(f"Recursive Result: {result_rec_arr}")
        print(f"Expected: {test['expected']}")

        assert (
            result_iter_arr == result_rec_arr == test["expected"]
        ), f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
