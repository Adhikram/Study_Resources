"""
# Question: Rotate List
# Link: https://leetcode.com/problems/rotate-list/

# Rotate linked list to the right by k places

# Time Complexity: O(n) where n is length of list
# Space Complexity: O(1)

# Algorithm:
# 1. Find list length and last node
# 2. Connect last node to head (make circular)
# 3. Find new breakpoint using k
# 4. Break circle at correct position
# 5. Return new head

# Key Components:
# - ListNode class for linked list structure
# - rotate_right(): Main rotation implementation
# - Length calculation and circular list handling
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class RotateRight:
    def rotate_right(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        # Find length and last node
        last = head
        length = 1
        while last.next:
            last = last.next
            length += 1

        # Calculate actual rotation needed
        k = length - (k % length) - 1

        # Connect last to head
        last.next = head

        # Find new breakpoint
        while k > 0:
            head = head.next
            k -= 1

        # Set new head and break circle
        result = head.next
        head.next = None

        return result


def main():
    solution = RotateRight()

    # Create test list: 1->2->3->4->5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Rotate by 2
    result = solution.rotate_right(head, 2)

    # Print result
    while result:
        print(result.val)
        result = result.next


if __name__ == "__main__":
    main()
