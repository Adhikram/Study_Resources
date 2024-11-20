"""
# Question: Minimum Multiplications to Reach End
# Find minimum steps to reach target by multiplying with given numbers

# Time Complexity: O(N * M) where N is range of values and M is number of allowed multipliers
# Space Complexity: O(N)

# Algorithm:
# 1. BFS approach with modulo arithmetic
# 2. Track visited numbers
# 3. Find shortest path to target
"""

from collections import deque


class MinimumMultiplications:
    def min_multiplications(self, arr: list[int], start: int, end: int) -> int:
        MOD = 100000
        queue = deque([(start, 0)])  # (number, steps)
        visited = {start}

        while queue:
            num, steps = queue.popleft()

            if num == end:
                return steps

            for multiplier in arr:
                next_num = (num * multiplier) % MOD
                if next_num not in visited:
                    visited.add(next_num)
                    queue.append((next_num, steps + 1))

        return -1


def main():
    solution = MinimumMultiplications()
    arr = [2, 3, 5]
    print(solution.min_multiplications(arr, 4, 40))


if __name__ == "__main__":
    main()
