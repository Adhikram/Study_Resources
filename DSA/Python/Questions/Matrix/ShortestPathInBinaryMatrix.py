"""
# Question: Shortest Path in Binary Matrix
# Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

# Algorithm:
# 1. Use BFS to find shortest path
# 2. Consider all 8 directions
# 3. Track visited cells
# 4. Return shortest path length
"""

from collections import deque


class ShortestPathInBinaryMatrix:
    def shortest_path_binary_matrix(self, grid: list[list[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1

        n = len(grid)
        if n == 1:
            return 1

        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        queue = deque([(0, 0, 1)])  # row, col, distance
        grid[0][0] = 1  # mark as visited

        while queue:
            row, col, dist = queue.popleft()

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if new_row == n - 1 and new_col == n - 1:
                    return dist + 1

                if (
                    0 <= new_row < n
                    and 0 <= new_col < n
                    and grid[new_row][new_col] == 0
                ):
                    grid[new_row][new_col] = 1
                    queue.append((new_row, new_col, dist + 1))

        return -1


def main():
    solution = ShortestPathInBinaryMatrix()
    grid = [[0, 1], [1, 0]]
    print(solution.shortest_path_binary_matrix(grid))  # Expected: 2


if __name__ == "__main__":
    main()
