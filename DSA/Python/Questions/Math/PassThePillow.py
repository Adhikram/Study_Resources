"""
# Question: Pass the Pillow
# Link: https://leetcode.com/problems/pass-the-pillow/

# Time Complexity: O(1)
# Space Complexity: O(1)

# Algorithm:
# 1. Calculate complete cycles
# 2. Determine direction based on cycle count
# 3. Return current position
"""


class PassThePillow:
    def pass_the_pillow(self, n: int, time: int) -> int:
        chunks = time // (n - 1)
        return (time % (n - 1) + 1) if chunks % 2 == 0 else (n - time % (n - 1))


def main():
    solution = PassThePillow()
    n = 5
    time = 3
    print(solution.pass_the_pillow(n, time))  # Expected output based on test case


if __name__ == "__main__":
    main()
