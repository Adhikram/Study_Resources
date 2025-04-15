"""
Common Stack and Queue Tricks and Patterns for Coding Interviews

This file contains popular stack and queue manipulation techniques
that frequently appear in coding interviews.
"""

def monotonic_stack_patterns():
    """
    Monotonic Stack Patterns:
    Used for problems involving finding next/previous greater/smaller elements
    """
    def next_greater_element(arr):
        n = len(arr)
        result = [-1] * n
        stack = []  # Stack will store indices
        
        for i in range(n):
            # Pop elements from stack while current element is greater
            while stack and arr[i] > arr[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = arr[i]
            stack.append(i)
        
        return result

def stack_for_parentheses():
    """
    Stack-based Solutions for Parentheses Problems:
    1. Valid Parentheses
    2. Longest Valid Parentheses
    3. Remove Invalid Parentheses
    """
    def is_valid_parentheses(s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets:
                if not stack or stack.pop() != brackets[char]:
                    return False
        
        return len(stack) == 0

def min_max_stack():
    """
    Implementing Min/Max Stack:
    Keep track of minimum/maximum elements in O(1) time
    """
    class MinMaxStack:
        def __init__(self):
            self.stack = []
            self.min_stack = []  # Keeps track of minimums
            self.max_stack = []  # Keeps track of maximums
        
        def push(self, x):
            self.stack.append(x)
            
            # Update min_stack
            if not self.min_stack or x <= self.min_stack[-1]:
                self.min_stack.append(x)
            
            # Update max_stack
            if not self.max_stack or x >= self.max_stack[-1]:
                self.max_stack.append(x)
        
        def pop(self):
            if not self.stack:
                return None
            
            x = self.stack.pop()
            
            # Update min_stack and max_stack
            if x == self.min_stack[-1]:
                self.min_stack.pop()
            if x == self.max_stack[-1]:
                self.max_stack.pop()
            
            return x
        
        def get_min(self):
            return self.min_stack[-1] if self.min_stack else None
        
        def get_max(self):
            return self.max_stack[-1] if self.max_stack else None

def queue_using_stacks():
    """
    Implementing Queue using Stacks:
    Two approaches: O(1) amortized enqueue or O(1) amortized dequeue
    """
    class QueueUsingStacks:
        def __init__(self):
            self.stack1 = []  # For enqueue
            self.stack2 = []  # For dequeue
        
        def enqueue(self, x):
            self.stack1.append(x)
        
        def dequeue(self):
            if not self.stack2:
                # Transfer elements from stack1 to stack2
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            return self.stack2.pop() if self.stack2 else None

def sliding_window_maximum():
    """
    Sliding Window Maximum using Deque:
    Maintain a monotonic decreasing deque
    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    from collections import deque
    
    def max_sliding_window(arr, k):
        result = []
        window = deque()  # Store indices
        
        for i in range(len(arr)):
            # Remove elements outside current window
            while window and window[0] <= i - k:
                window.popleft()
            
            # Remove smaller elements from back
            while window and arr[i] >= arr[window[-1]]:
                window.pop()
            
            window.append(i)
            
            # Add maximum of current window
            if i >= k - 1:
                result.append(arr[window[0]])
        
        return result

def stack_for_calculator():
    """
    Stack-based Calculator:
    Evaluate arithmetic expressions
    """
    def calculate(s: str) -> int:
        stack = []
        num = 0
        sign = '+'
        
        for i, char in enumerate(s + '+'):
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in '+-*/':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                
                num = 0
                sign = char
        
        return sum(stack)

# Interview Tips:
"""
1. Stack Applications:
   - Expression evaluation (infix, postfix)
   - Parentheses matching
   - Function call stack/recursion
   - Undo operations
   - Browser history
   - Syntax parsing
   - Monotonic stack problems

2. Queue Applications:
   - BFS traversal
   - Task scheduling
   - Cache implementation
   - Stream processing
   - Print queue
   - Message queue

3. Common Edge Cases:
   - Empty stack/queue
   - Single element
   - Operations on empty structure
   - Stack overflow/underflow
   - Queue full/empty conditions

4. Optimization Tips:
   - Use deque for O(1) operations at both ends
   - Consider space-time tradeoffs
   - Look for monotonic patterns
   - Consider using multiple stacks/queues
   - Think about amortized complexity

5. Problem-Solving Patterns:
   - Monotonic stack for next/previous greater/smaller
   - Two stacks for min/max tracking
   - Deque for sliding window
   - Stack for parsing/validation
   - Queue for level-order processing
""" 