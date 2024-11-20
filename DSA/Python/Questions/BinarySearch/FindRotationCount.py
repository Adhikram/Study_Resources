"""
# Question: Find Rotation Count
# Find number of times a sorted array is rotated

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search to find pivot
# 2. Count rotations based on pivot
# 3. Handle edge cases
"""


class FindRotationCount:
    def count_rotations(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 1

        # Array is not rotated
        if arr[left] <= arr[right]:
            return 0

        while left <= right:
            # If single element
            if left == right:
                return left

            mid = (left + right) >> 1
            next_mid = (mid + 1) % len(arr)
            prev_mid = (mid - 1 + len(arr)) % len(arr)

            # Check if mid is pivot
            if arr[mid] <= arr[next_mid] and arr[mid] <= arr[prev_mid]:
                return mid
            elif arr[mid] <= arr[right]:
                right = mid - 1
            else:
                left = mid + 1

        return 0


def main():
    solution = FindRotationCount()
    arr = [7, 9, 11, 12, 5]
    print(solution.count_rotations(arr))  # Expected: 4


if __name__ == "__main__":
    main()
