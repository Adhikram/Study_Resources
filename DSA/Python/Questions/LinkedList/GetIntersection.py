"""
# Question: Intersection of Two Linked Lists
# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/

# Find the intersection node of two linked lists

# Time Complexity: O(n + m) where n, m are lengths of lists
# Space Complexity: O(1)

# Algorithm:
# 1. Use two pointers starting from heads
# 2. When one pointer reaches end, move to other list's head
# 3. Intersection found when pointers meet
# 4. Return intersection node or None

# Key Components:
# - ListNode class for linked list structure
# - get_intersection_node(): Main intersection finding implementation
# - Two-pointer technique with list switching
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class GetIntersection:
    def get_intersection_node(self, headA: ListNode, headB: ListNode) -> ListNode:
        a_pointer = headA
        b_pointer = headB

        while a_pointer or b_pointer:
            if a_pointer == b_pointer:
                break

            a_pointer = headB if not a_pointer else a_pointer.next
            b_pointer = headA if not b_pointer else b_pointer.next

        return b_pointer


def main():
    solution = GetIntersection()

    # Create test lists with intersection
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = ListNode(8)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)

    headB = ListNode(5)
    headB.next = ListNode(0)
    headB.next.next = ListNode(1)
    headB.next.next.next = headA.next.next  # Create intersection

    result = solution.get_intersection_node(headA, headB)
    print(f"Intersection node value: {result.val}")


if __name__ == "__main__":
    main()
