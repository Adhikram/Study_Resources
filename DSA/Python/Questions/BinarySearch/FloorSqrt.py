"""
# Question: Floor Square Root
# Find floor of square root of a number using binary search

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search between 1 and n
# 2. Find largest number whose square is <= n
# 3. Return floor value
"""


class FloorSqrt:
    def floor_sqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left, right = 1, x
        result = 0

        while left <= right:
            mid = (left + right) >> 1
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result


def main():
    solution = FloorSqrt()
    print(solution.floor_sqrt(8))  # Expected: 2
    print(solution.floor_sqrt(16))  # Expected: 4


if __name__ == "__main__":
    main()
