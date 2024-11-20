"""
# Question: Implement Queue using Stacks
# Link: https://leetcode.com/problems/implement-queue-using-stacks/

# Implement queue operations using two stacks

# Time Complexity:
# - Push: O(n)
# - Pop: O(1)
# - Peek: O(1)
# - Empty: O(1)

# Space Complexity: O(n)

# Algorithm:
# 1. Use two stacks for queue simulation
# 2. Transfer elements between stacks for push
# 3. Maintain FIFO order
# 4. Optimize pop and peek operations

# Key Components:
# - MyQueue class implementation
# - Two stacks for storage
# - Element transfer logic
"""


class MyQueue:
    def __init__(self):
        self.s1 = []  # main stack
        self.s2 = []  # auxiliary stack

    def push(self, x: int) -> None:
        # Transfer all elements from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())

        # Add new element to s1
        self.s1.append(x)

        # Transfer back all elements from s2 to s1
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0


def main():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.peek())  # Expected: 1
    print(queue.pop())  # Expected: 1
    print(queue.empty())  # Expected: False


if __name__ == "__main__":
    main()
