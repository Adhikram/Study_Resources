"""
# Question: Merge In Between Linked Lists
# Link: https://leetcode.com/problems/merge-in-between-linked-lists/

# Merge list2 into list1 between positions a and b

# Time Complexity: O(n) where n is length of lists
# Space Complexity: O(1)

# Algorithm:
# 1. Find nodes at positions a and b in list1
# 2. Connect start node to list2
# 3. Find end of list2
# 4. Connect end of list2 to remainder of list1

# Key Components:
# - Node class for linked list structure
# - merge_in_between(): Main merging implementation
# - Position tracking and list connection
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeInBetween:
    def merge_in_between(self, list1: Node, a: int, b: int, list2: Node) -> Node:
        start = end = list1
        i = 1

        # Find positions a and b
        while i <= b:
            if i == a:
                start = end
            end = end.next
            i += 1

        # Connect list2
        start.next = list2

        # Find end of list2
        while list2.next:
            list2 = list2.next

        # Connect to remainder of list1
        list2.next = end.next

        return list1


def main():
    # Create test lists
    list1 = Node(0)
    list1.next = Node(1)
    list1.next.next = Node(2)
    list1.next.next.next = Node(3)
    list1.next.next.next.next = Node(4)
    list1.next.next.next.next.next = Node(5)

    list2 = Node(1000000)
    list2.next = Node(1000001)
    list2.next.next = Node(1000002)

    solution = MergeInBetween()
    result = solution.merge_in_between(list1, 3, 4, list2)

    # Print result
    while result:
        print(result.val, end=" ")
        result = result.next


if __name__ == "__main__":
    main()
