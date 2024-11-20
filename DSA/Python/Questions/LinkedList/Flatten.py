"""
# Question: Flatten a Multilevel Doubly Linked List
# Link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

# Time Complexity: O(n) where n is total number of nodes
# Space Complexity: O(1) for iterative, O(n) for recursive due to stack

# Two Solution Approaches:
# 1. Recursive:
#    - Process each level recursively
#    - Connect child lists to main list
# 2. Iterative:
#    - Use stack to track next pointers
#    - Process child lists first

# Key Components:
# - Node class with next, prev, and child pointers
# - flatten(): Iterative implementation
# - flatten_recursive(): Recursive implementation
"""


class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Flatten:
    def flatten_recursive(self, head: Node) -> Node:
        if not head:
            return None

        current = head
        while current:
            if current.child:
                next_node = current.next

                # Connect current node to child list
                current.next = self.flatten_recursive(current.child)
                current.next.prev = current
                current.child = None

                # Find tail of child list
                tail = current.next
                while tail.next:
                    tail = tail.next

                # Connect tail to next node
                tail.next = next_node
                if next_node:
                    next_node.prev = tail

            current = current.next

        return head

    def flatten(self, head: Node) -> Node:
        if not head:
            return None

        current = head
        stack = []

        while current:
            if current.child:
                if current.next:
                    stack.append(current.next)

                current.next = current.child
                current.child.prev = current
                current.child = None

            elif not current.next and stack:
                current.next = stack.pop()
                current.next.prev = current

            current = current.next

        return head


def main():
    solution = Flatten()

    # Create test multilevel linked list
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.child = Node(3)
    head.child.next = Node(4)
    head.child.next.prev = head.child

    # Test both approaches
    result1 = solution.flatten(head)
    result2 = solution.flatten_recursive(head)

    # Print results
    def print_list(node):
        while node:
            print(node.val, end=" ")
            node = node.next
        print()

    print("Iterative result:", end=" ")
    print_list(result1)
    print("Recursive result:", end=" ")
    print_list(result2)


if __name__ == "__main__":
    main()
