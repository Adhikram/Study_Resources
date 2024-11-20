"""
# Question: Implement Stack using Queues
# Link: https://leetcode.com/problems/implement-stack-using-queues/

# Implement stack operations using queues

# Time Complexity:
# - Push: O(1)
# - Pop: O(1)
# - Top: O(1)
# - Empty: O(1)

# Space Complexity: O(n)

# Algorithm:
# 1. Use two queues for stack simulation
# 2. Transfer elements between queues for operations
# 3. Maintain LIFO order
# 4. Optimize push operation

# Key Components:
# - MyStack class implementation
# - Two queues for storage
# - Element transfer logic
"""

from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


def main():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Top element of the stack: {stack.top()}")


if __name__ == "__main__":
    main()
