"""
# Question: 24 Game
# Link: https://leetcode.com/problems/24-game/

# Find if it's possible to make 24 using 4 numbers with basic operations

# Time Complexity: O(6^N)
# Space Complexity: O(1)

# Algorithm:
# 1. Try all possible pairs of numbers
# 2. Apply all possible operations (+,-,*,/)
# 3. Recursively solve with remaining numbers
# 4. Check if result equals 24

# Key Components:
# - backtrack(): Recursive helper for operation combinations
# - judge_point_24(): Main implementation
# - Floating point comparison handling
"""


class JudgePoint24:
    def __init__(self):
        self.EPS = 1e-6

    def backtrack(self, A: list, n: int) -> bool:
        if n == 1:
            return abs(A[0] - 24) < self.EPS

        for i in range(n):
            for j in range(i + 1, n):
                a, b = A[i], A[j]
                A[j] = A[n - 1]

                # Try all operations
                A[i] = a + b
                if self.backtrack(A, n - 1):
                    return True

                A[i] = a - b
                if self.backtrack(A, n - 1):
                    return True

                A[i] = b - a
                if self.backtrack(A, n - 1):
                    return True

                A[i] = a * b
                if self.backtrack(A, n - 1):
                    return True

                if b != 0:
                    A[i] = a / b
                    if self.backtrack(A, n - 1):
                        return True

                if a != 0:
                    A[i] = b / a
                    if self.backtrack(A, n - 1):
                        return True

                A[i], A[j] = a, b

        return False

    def judge_point_24(self, nums: list) -> bool:
        A = [float(num) for num in nums]
        return self.backtrack(A, len(A))


def main():
    solution = JudgePoint24()
    print(solution.judge_point_24([4, 1, 8, 7]))  # True
    print(solution.judge_point_24([1, 2, 1, 2]))  # False


if __name__ == "__main__":
    main()
