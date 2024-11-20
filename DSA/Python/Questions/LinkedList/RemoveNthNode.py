"""
# Question: Remove Nth Node From End of List
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Remove nth node from end of linked list in one pass

# Time Complexity: O(n) where n is length of list
# Space Complexity: O(n) due to recursion stack

# Algorithm:
# 1. Use recursive approach to reach end
# 2. Count back from end during recursion
# 3. Remove nth node when count matches
# 4. Return modified list

# Key Components:
# - ListNode class for linked list structure
# - ref(): Recursive helper function
# - remove_nth_from_end(): Main removal implementation
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class RemoveNthNode:
    def ref(self, head: ListNode, n: list) -> ListNode:
        # Base case
        if not head:
            return None

        # Recursive call
        head.next = self.ref(head.next, n)
        n[0] -= 1

        # Remove nth node
        if n[0] == 0:
            return head.next

        return head

    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        return self.ref(head, [n])


def main():
    solution = RemoveNthNode()

    # Create test list: 1->2->3->4->5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Remove 2nd node from end
    result = solution.remove_nth_from_end(head, 2)

    # Print result
    while result:
        print(result.val)
        result = result.next


if __name__ == "__main__":
    main()
