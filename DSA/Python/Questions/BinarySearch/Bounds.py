"""
# Question: Binary Search Bounds
# Find lower and upper bounds in sorted array

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Algorithm:
# 1. Implement lower bound search
# 2. Implement upper bound search
# 3. Handle edge cases
"""


class Bounds:
    def lower_bound(self, arr: list[int], target: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) >> 1
            if arr[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left

    def upper_bound(self, arr: list[int], target: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) >> 1
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return left


def main():
    solution = Bounds()
    arr = [1, 2, 2, 3, 3, 3, 4, 5]
    print(solution.lower_bound(arr, 3))  # Expected: 3
    print(solution.upper_bound(arr, 3))  # Expected: 6


if __name__ == "__main__":
    main()
