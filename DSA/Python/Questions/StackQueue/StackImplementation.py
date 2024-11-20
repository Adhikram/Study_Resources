"""
# Question: Implement Stack
# Link: Custom Stack Implementation

# Basic stack operations implementation

# Time Complexity:
# - Push: O(1)
# - Pop: O(1)
# - Top: O(1)
# - isEmpty: O(1)
# - isFull: O(1)

# Space Complexity: O(n)

# Algorithm:
# 1. Array-based stack implementation
# 2. Track top element position
# 3. Handle stack overflow/underflow
# 4. Maintain capacity constraints

# Key Components:
# - Stack class implementation
# - Array for storage
# - Capacity management
"""


class Stack:
    def __init__(self, capacity: int):
        self.top = -1
        self.store = [0] * capacity
        self.capacity = capacity

    def push(self, num: int) -> None:
        if self.is_full() == 1:
            return
        self.top += 1
        self.store[self.top] = num

    def pop(self) -> int:
        if self.is_empty() == 1:
            return -1
        val = self.store[self.top]
        self.top -= 1
        return val

    def top_element(self) -> int:
        if self.is_empty() == 1:
            return -1
        return self.store[self.top]

    def is_empty(self) -> int:
        return 1 if self.top == -1 else 0

    def is_full(self) -> int:
        return 1 if self.top == (self.capacity - 1) else 0


def main():
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(f"Top element of the stack: {stack.top_element()}")


if __name__ == "__main__":
    main()
