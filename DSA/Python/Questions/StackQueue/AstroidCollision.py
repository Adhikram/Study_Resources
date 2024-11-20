"""
# Question: Asteroid Collision
# Link: https://leetcode.com/problems/asteroid-collision/

# Simulate asteroid collisions based on direction and size

# Time Complexity: O(n)
# Space Complexity: O(n)

# Algorithm:
# 1. Use stack to track asteroids
# 2. Process right-moving asteroids
# 3. Handle collisions with left-moving asteroids
# 4. Return surviving asteroids

# Key Components:
# - asteroid_collision(): Main collision simulator
# - Stack for tracking asteroids
# - Collision resolution logic
"""


class AsteroidCollision:
    def asteroid_collision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for asteroid in asteroids:
            # Right-moving asteroid or empty stack
            if asteroid > 0 or not stack:
                stack.append(asteroid)
                continue

            # Handle collisions
            while stack:
                # No collision if top asteroid moving left
                if stack[-1] < 0:
                    stack.append(asteroid)
                    break

                # Current asteroid destroyed
                if abs(stack[-1]) > abs(asteroid):
                    break

                # Equal size destruction
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    break

                # Top asteroid destroyed
                stack.pop()
                if not stack:
                    stack.append(asteroid)
                    break

        return stack


def main():
    solution = AsteroidCollision()
    print(solution.asteroid_collision([5, 10, -5]))  # Expected: [5, 10]
    print(solution.asteroid_collision([8, -8]))  # Expected: []
    print(solution.asteroid_collision([10, 2, -5]))  # Expected: [10]


if __name__ == "__main__":
    main()
