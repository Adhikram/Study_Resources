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
        # Initialize result array with -1 for each car
        n = len(cars)
        result = [-1.0] * n
        # Stack to keep track of potential collisions
        stack = deque()

        def catch_time(cars: List[List[int]], i: int, j: int) -> float:
            """
            Calculate collision time between car i and car j
            i: index of current car
            j: index of car ahead
            Returns: time of collision
            """
            # Distance between cars divided by relative speed
            dist = cars[j][0] - cars[i][0]
            v = cars[i][1] - cars[j][1]
            return dist / v

        # Process cars from right to left
        for i in range(n - 1, -1, -1):
            # While there are cars ahead to potentially collide with
            while stack:
                j = stack[-1]
                c1, c2 = cars[i], cars[j]

                # Check if current car is faster and will collide
                # before the car ahead collides with another car
                if c1[1] > c2[1] and (
                    result[j] == -1.0 or catch_time(cars, i, j) <= result[j]
                ):
                    result[i] = catch_time(cars, i, j)
                    break
                stack.pop()

            # Add current car to stack
            stack.append(i)

        return result


def main():
    # Test cases
    test_cases = [
        {
            "cars": [[1, 2], [2, 1], [4, 3], [7, 2]],
            "expected": [1.00000, -1.00000, 3.00000, -1.00000],
        },
        {
            "cars": [[3, 4], [5, 4], [6, 3], [9, 1]],
            "expected": [2.00000, 1.00000, 1.50000, -1.00000],
        },
    ]

    solution = CarFleet2()
    for i, test in enumerate(test_cases):
        result = solution.get_collision_times(test["cars"])
        print(f"\nTest Case {i + 1}:")
        print(f"Input: {test['cars']}")
        print(f"Expected: {test['expected']}")
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
