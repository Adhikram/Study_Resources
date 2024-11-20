"""
# Question: Car Fleet II
# Link: https://leetcode.com/problems/car-fleet-ii/

# Calculate collision times for cars moving in same direction

# Time Complexity: O(n)
# Space Complexity: O(n)

# Algorithm:
# 1. Process cars from right to left
# 2. Use stack to track potential collisions
# 3. Calculate collision times
# 4. Handle speed and position differences

# Key Components:
# - get_collision_times(): Main implementation
# - catch_time(): Helper for collision time calculation
# - Stack for tracking car positions
"""

from collections import deque
from typing import List


class CarFleet2:
    def get_collision_times(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        result = [-1.0] * n
        stack = deque()

        def catch_time(cars: List[List[int]], i: int, j: int) -> float:
            dist = cars[j][0] - cars[i][0]
            v = cars[i][1] - cars[j][1]
            return dist / v

        for i in range(n - 1, -1, -1):
            while stack:
                j = stack[-1]
                c1, c2 = cars[i], cars[j]

                if c1[1] > c2[1] and (
                    result[j] == -1.0 or catch_time(cars, i, j) <= result[j]
                ):
                    result[i] = catch_time(cars, i, j)
                    break
                stack.pop()

            stack.append(i)

        return result


def main():
    solution = CarFleet2()
    cars = [[1, 2], [2, 1], [4, 3], [7, 2]]
    print(solution.get_collision_times(cars))
    # Expected: [1.00000,-1.00000,3.00000,-1.00000]


if __name__ == "__main__":
    main()
