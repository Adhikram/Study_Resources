"""
# Question: The Maze
# Link: https://leetcode.com/problems/the-maze/

# Time Complexity: O(m*n*max(m,n))
# Space Complexity: O(m*n)

# Algorithm:
# 1. Use DFS to explore paths
# 2. Roll ball until hitting wall
# 3. Track visited positions
# 4. Check if destination is reachable
"""


class TheMaze:
    def has_path(
        self, maze: list[list[int]], start: list[int], destination: list[int]
    ) -> bool:
        m, n = len(maze), len(maze[0])
        visited = set()

        def dfs(x: int, y: int) -> bool:
            if (x, y) in visited:
                return False

            if [x, y] == destination:
                return True

            visited.add((x, y))

            # Try all four directions
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x, y

                # Roll the ball until hitting wall
                while (
                    0 <= new_x + dx < m
                    and 0 <= new_y + dy < n
                    and maze[new_x + dx][new_y + dy] == 0
                ):
                    new_x += dx
                    new_y += dy

                if dfs(new_x, new_y):
                    return True

            return False

        return dfs(start[0], start[1])


def main():
    solution = TheMaze()
    maze = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
    ]
    start = [0, 4]
    destination = [4, 4]
    print(solution.has_path(maze, start, destination))  # Expected: True


if __name__ == "__main__":
    main()
