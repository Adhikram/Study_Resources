"""
# Question: Tiling a Rectangle with the Fewest Squares
# Link: https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

# Find minimum number of squares needed to tile rectangle

# Time Complexity: O(N^2)
# Space Complexity: O(N^2)

# Algorithm:
# 1. Try placing squares at each uncovered position
# 2. Use backtracking to explore all possibilities
# 3. Track minimum squares needed
# 4. Handle special cases and optimizations

# Key Components:
# - tiling_rectangle(): Main implementation
# - backtrack(): Recursive helper for placing squares
# - find_width(): Helper to find maximum possible square size
# - cover(): Helper to mark/unmark squares
"""


class TilingRectangles:
    def __init__(self):
        self.ret = 0
        self.m = 0
        self.n = 0

    def tiling_rectangle(self, m: int, n: int) -> int:
        self.m = m
        self.n = n
        self.ret = m * n
        mat = [[0] * n for _ in range(m)]
        self.backtrack(mat, 0)
        return self.ret

    def backtrack(self, mat: list[list[int]], size: int) -> None:
        if size >= self.ret:
            return

        # Find uncovered position
        x = y = -1
        for i in range(self.m):
            found = False
            for j in range(self.n):
                if mat[i][j] == 0:
                    x, y = i, j
                    found = True
                    break
            if found:
                break

        if x == -1 and y == -1:
            self.ret = min(size, self.ret)
            return

        length = self.find_width(x, y, mat)
        while length >= 1:
            self.cover(x, y, length, mat, 1)
            self.backtrack(mat, size + 1)
            self.cover(x, y, length, mat, 0)
            length -= 1

    def find_width(self, x: int, y: int, mat: list[list[int]]) -> int:
        length = 1
        while x + length < self.m and y + length < self.n:
            flag = True
            for i in range(length + 1):
                if mat[x + i][y + length] == 1 or mat[x + length][y + i] == 1:
                    flag = False
                    break
            if not flag:
                break
            length += 1
        return length

    def cover(
        self, x: int, y: int, length: int, mat: list[list[int]], val: int
    ) -> None:
        for i in range(x, x + length):
            for j in range(y, y + length):
                mat[i][j] = val


def main():
    solution = TilingRectangles()
    print(solution.tiling_rectangle(2, 3))  # Expected: 3
    print(solution.tiling_rectangle(5, 8))  # Expected: 5
    print(solution.tiling_rectangle(11, 13))  # Expected: 6


if __name__ == "__main__":
    main()
