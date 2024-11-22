"""
# Question: Binary Search Bounds
# Problem Statement:
# Implement functions to find lower and upper bounds in a sorted array.
# Lower bound: First element greater than or equal to target
# Upper bound: First element greater than target

# Example:
# Input: arr = [1,2,2,3,3,3,4,5], target = 3
# Lower Bound Output: 3 (index of first 3)
# Upper Bound Output: 6 (index after last 3)
"""

from typing import List


class Bounds:
    def lower_bound_binary(self, arr: List[int], target: int) -> int:
        """
        Binary search approach for lower bound
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) >> 1
            if arr[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left

    def upper_bound_binary(self, arr: List[int], target: int) -> int:
        """
        Binary search approach for upper bound
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) >> 1
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def lower_bound_two_pointer(self, arr: List[int], target: int) -> int:
        """
        Two pointer approach for lower bound
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i in range(len(arr)):
            if arr[i] >= target:
                return i
        return len(arr)

    def upper_bound_two_pointer(self, arr: List[int], target: int) -> int:
        """
        Two pointer approach for upper bound
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i in range(len(arr)):
            if arr[i] > target:
                return i
        return len(arr)


def main():
    test_cases = [
        {
            "arr": [1, 2, 2, 3, 3, 3, 4, 5],
            "target": 3,
            "expected_lower": 3,
            "expected_upper": 6,
        },
        {"arr": [1, 2, 3, 4, 5], "target": 0, "expected_lower": 0, "expected_upper": 0},
        {"arr": [1, 2, 3, 4, 5], "target": 6, "expected_lower": 5, "expected_upper": 5},
        {"arr": [1, 1, 1, 1, 1], "target": 1, "expected_lower": 0, "expected_upper": 5},
    ]

    solution = Bounds()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Array: {test['arr']}")
        print(f"Target: {test['target']}")

        # Binary Search Results
        lower_binary = solution.lower_bound_binary(test["arr"], test["target"])
        upper_binary = solution.upper_bound_binary(test["arr"], test["target"])

        # Two Pointer Results
        lower_two_pointer = solution.lower_bound_two_pointer(
            test["arr"], test["target"]
        )
        upper_two_pointer = solution.upper_bound_two_pointer(
            test["arr"], test["target"]
        )

        print(
            f"Binary Search - Lower Bound: {lower_binary}, Upper Bound: {upper_binary}"
        )
        print(
            f"Two Pointer - Lower Bound: {lower_two_pointer}, Upper Bound: {upper_two_pointer}"
        )
        print(
            f"Expected - Lower Bound: {test['expected_lower']}, Upper Bound: {test['expected_upper']}"
        )

        assert lower_binary == lower_two_pointer == test["expected_lower"]
        assert upper_binary == upper_two_pointer == test["expected_upper"]


if __name__ == "__main__":
    main()
