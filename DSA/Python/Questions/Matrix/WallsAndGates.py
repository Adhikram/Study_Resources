"""
# Question: Walls and Gates
# Link: https://leetcode.com/problems/walls-and-gates/

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

# Algorithm:
# 1. Start BFS from all gates
# 2. Update distances to empty rooms
# 3. Process rooms level by level
# 4. Fill shortest distances
"""

from collections import deque


class WallsAndGates:
    def walls_and_gates(self, rooms: list[list[int]]) -> None:
        if not rooms or not rooms[0]:
            return

        m, n = len(rooms), len(rooms[0])
        queue = deque()
        INF = 2147483647

        # Find all gates
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        # BFS from gates
        while queue:
            row, col = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and rooms[r][c] == INF:
                    rooms[r][c] = rooms[row][col] + 1
                    queue.append((r, c))


def main():
    solution = WallsAndGates()
    INF = 2147483647
    rooms = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]
    solution.walls_and_gates(rooms)
    print(rooms)


if __name__ == "__main__":
    main()
