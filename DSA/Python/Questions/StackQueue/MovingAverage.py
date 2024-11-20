"""
# Question: Moving Average from Data Stream
# Link: https://leetcode.com/problems/moving-average-from-data-stream/

# Calculate moving average of numbers in sliding window

# Time Complexity: O(1)
# Space Complexity: O(size)

# Algorithm:
# 1. Maintain fixed-size window using queue
# 2. Track running sum of elements
# 3. Update window by adding/removing elements
# 4. Calculate average on each update

# Key Components:
# - MovingAverage class implementation
# - Queue for window management
# - Running sum maintenance
"""

from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            self.sum -= self.window.popleft()

        self.window.append(val)
        self.sum += val

        return self.sum / len(self.window)


def main():
    moving_average = MovingAverage(3)
    print(moving_average.next(1))  # 1.0
    print(moving_average.next(10))  # 5.5
    print(moving_average.next(3))  # 4.66667
    print(moving_average.next(5))  # 6.0


if __name__ == "__main__":
    main()
