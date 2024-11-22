"""
# Question: Find Rotation Count
# Problem Statement:
# Given a sorted array that has been rotated, find the number of times the array has been rotated.
# A rotation moves elements from the end to the front.

# Example:
# Input: arr = [7, 9, 11, 12, 5]
# Output: 4
# Explanation: Original array was [5, 7, 9, 11, 12] and it was rotated 4 times.
"""

from typing import List


class FindRotationCount:
    def count_rotations_binary(self, arr: List[int]) -> int:
        """
        Binary search approach to find rotation count
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(arr) - 1

        # Array is not rotated
        if arr[left] <= arr[right]:
            return 0

        while left <= right:
            # Single element case
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

    def count_rotations_linear(self, arr: List[int]) -> int:
        """
        Linear search approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return i
        return 0

    def count_rotations_pivot(self, arr: List[int]) -> int:
        """
        Find rotation count using pivot element
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) >> 1

            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid

        return left


def main():
    test_cases = [
        {"arr": [7, 9, 11, 12, 5], "expected": 4},
        {"arr": [1, 2, 3, 4, 5], "expected": 0},
        {"arr": [5, 1, 2, 3, 4], "expected": 1},
        {"arr": [2, 3, 4, 5, 1], "expected": 4},
    ]

    solution = FindRotationCount()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Array: {test['arr']}")

        result_binary = solution.count_rotations_binary(test["arr"])
        result_linear = solution.count_rotations_linear(test["arr"])
        result_pivot = solution.count_rotations_pivot(test["arr"])

        print(f"Binary Search Result: {result_binary}")
        print(f"Linear Search Result: {result_linear}")
        print(f"Pivot Search Result: {result_pivot}")
        print(f"Expected: {test['expected']}")

        assert result_binary == result_linear == result_pivot == test["expected"]


if __name__ == "__main__":
    main()
