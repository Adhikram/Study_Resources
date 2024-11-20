"""
# Question: Car Fleet
# Link: https://leetcode.com/problems/car-fleet/

# Time Complexity: O(n log n)
# Space Complexity: O(n)

# Algorithm:
# 1. Create position-speed pairs
# 2. Sort by position in reverse order
# 3. Calculate arrival times
# 4. Count number of fleets
"""


class CarFleet:
    def car_fleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Create position-speed pairs and sort by position
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []

        # Calculate arrival times
        for pos, spd in pairs:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)


def main():
    solution = CarFleet()
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(solution.car_fleet(target, position, speed))  # Expected: 3


if __name__ == "__main__":
    main()
