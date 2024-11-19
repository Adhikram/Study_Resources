from collections import deque

def main():
    linked_list = deque()

    # Insertion
    # Time Complexity: O(1)
    linked_list.append(1)
    linked_list.append(2)
    print("LinkedList after insertion:", list(linked_list))
    linked_list.appendleft(0)
    linked_list.append(10)
    print("LinkedList after insertion:", list(linked_list))

    # Access
    # Time Complexity: O(n)
    element = linked_list[0]
    print("Element at index 0:", element)

    # Search
    # Time Complexity: O(n)
    index = -1
    for i, value in enumerate(linked_list):
        if value == 2:
            index = i
            break
    print("Index of first occurrence of 2:", index)

if __name__ == "__main__":
    main()