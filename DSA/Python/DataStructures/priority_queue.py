import heapq

def add_elements(pq, elements):
    for element in elements:
        heapq.heappush(pq, element)  # O(log n) per insertion

def print_elements(pq, name):
    print(f"{name} Priority Queue elements:")
    while pq:
        print(heapq.heappop(pq), end=' ')  # O(log n) per removal
    print()

def main():
    elements = [5, 1, 3, 10, 2]

    # Default Priority Queue (Min-Heap)
    default_priority_queue = []
    add_elements(default_priority_queue, elements)  # O(n log n) for n elements
    print_elements(default_priority_queue, "Default")  # O(n log n) for n elements

    # Reverse Priority Queue (Max-Heap)
    reverse_priority_queue = []
    add_elements(reverse_priority_queue, [-element for element in elements])  # O(n log n) for n elements
    print("Reverse Priority Queue elements:")
    while reverse_priority_queue:
        print(-heapq.heappop(reverse_priority_queue), end=' ')  # O(log n) per removal
    print()

    # Using heapify to convert a list into a heap
    heap = [5, 1, 3, 10, 2]
    heapq.heapify(heap)  # O(n)
    print("Heapified list:", heap)

    # Using heappushpop to push an element and then pop the smallest element
    heapq.heappushpop(heap, 19)  # O(log n)
    print("Heap after heappushpop(0):", heap)

    # Using heapreplace to pop the smallest element and then push a new element
    heapq.heapreplace(heap, 6)  # O(log n)
    print("Heap after heapreplace(6):", heap)

    # Custom Comparator (Custom Ordering)
    custom_priority_queue = []
    add_elements(custom_priority_queue, [(element % 3, element) for element in elements])  # O(n log n) for n elements
    print("Custom Priority Queue elements:")
    while custom_priority_queue:
        print(heapq.heappop(custom_priority_queue)[1], end=' ')  # O(log n) per removal
    print()

    # Lambda expression for custom comparison logic
    lambda_priority_queue = []
    add_elements(lambda_priority_queue, [(-element, element) for element in elements])  # O(n log n) for n elements
    print("Lambda Priority Queue elements:")
    while lambda_priority_queue:
        print(heapq.heappop(lambda_priority_queue)[1], end=' ')  # O(log n) per removal
    print()

    # Lambda expression for custom comparison logic with even numbers first and then odd numbers in ascending order
    lambda_priority_queue2 = []
    add_elements(lambda_priority_queue2, [(0 if element % 2 == 0 else 1, element) for element in elements])  # O(n log n) for n elements
    print("Lambda Priority Queue 2 elements:")
    while lambda_priority_queue2:
        print(heapq.heappop(lambda_priority_queue2)[1], end=' ')  # O(log n) per removal
    print()

if __name__ == "__main__":
    main()