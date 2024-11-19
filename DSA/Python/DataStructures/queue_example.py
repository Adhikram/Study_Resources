from collections import deque

def main():
    # Initialize queue
    queue = deque()

    # Enqueue
    print("Enqueuing element: 1")
    queue.append(1)

    # Dequeue
    if queue:
        removed_element = queue.popleft()
        print(f"Dequeued element: {removed_element}")
    else:
        print("Queue is empty. Cannot dequeue.")

    # Peek
    if queue:
        front_element = queue[0]
        print(f"Front element: {front_element}")
    else:
        print("Queue is empty. No front element to peek.")

    # Add more elements
    queue.append(2)
    queue.append(3)
    print(f"Is the queue empty? {len(queue) == 0}")

    # Length (Size)
    print(f"Size of Queue: {len(queue)}")

    # Iterate through Queue using for loop
    print("\nIterating through Queue using for loop:")
    for element in queue:
        print(f"Element: {element}")

    # Iterate using enumerate
    print("\nIterating using enumerate:")
    for i, element in enumerate(queue):
        print(f"Element: {element}")

    # Iterate using list comprehension
    print("\nIterating using list comprehension:")
    [print(f"Element: {element}") for element in queue]

    # Convert to list and iterate
    print("\nIterating using converted list:")
    elements_list = list(queue)
    for element in elements_list:
        print(f"Element: {element}")

if __name__ == "__main__":
    main()
