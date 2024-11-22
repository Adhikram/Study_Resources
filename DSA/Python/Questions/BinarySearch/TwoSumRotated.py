"""
# Question: Two Sum in Rotated Sorted Array
# Problem Statement:
# Given a rotated sorted array, find two numbers that sum up to a target value.
# Return the two numbers in any order.

# Example:
# Input: nums = [4,5,6,7,0,1,2], target = 6
# Output: [4,2] or [2,4]
# Explanation: 4 + 2 = 6
"""

from typing import List


class TwoSumRotated:
    def find_pair_binary(self, nums: List[int], target: int) -> List[int]:
        """
        Binary search approach
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """

        def find_pivot():
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) >> 1
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left

        pivot = find_pivot()
        n = len(nums)
        left = pivot
        right = (pivot - 1) % n

        while left != right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [nums[left], nums[right]]
            elif current_sum < target:
                left = (left + 1) % n
            else:
                right = (right - 1 + n) % n
        return []

    def find_pair_two_pointer(self, nums: List[int], target: int) -> List[int]:
        """
        Two pointer approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        max_idx = 0

        # Find maximum element index
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                max_idx = i - 1
                break

        left = (max_idx + 1) % n  # Smallest element
        right = max_idx  # Largest element

        while left != right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                return [nums[left], nums[right]]
            elif curr_sum < target:
                left = (left + 1) % n
            else:
                right = (right - 1 + n) % n
        return []

    def find_pair_hash(self, nums: List[int], target: int) -> List[int]:
        """
        Hash table approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        for num in nums:
            complement = target - num
            if complement in seen:
                return [num, complement]
            seen.add(num)
        return []


def main():
    test_cases = [
        {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 6, "expected_sum": 6},
        {"nums": [3, 4, 5, 1, 2], "target": 7, "expected_sum": 7},
        {"nums": [2, 3, 4, 5, 1], "target": 3, "expected_sum": 3},
    ]

    solution = TwoSumRotated()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Array: {test['nums']}")
        print(f"Target: {test['target']}")

        result_binary = solution.find_pair_binary(test["nums"], test["target"])
        result_two_pointer = solution.find_pair_two_pointer(
            test["nums"], test["target"]
        )
        result_hash = solution.find_pair_hash(test["nums"], test["target"])

        print(f"Binary Search Result: {result_binary}")
        print(f"Two Pointer Result: {result_two_pointer}")
        print(f"Hash Table Result: {result_hash}")

        # Verify results
        if result_binary:
            assert sum(result_binary) == test["expected_sum"]
        if result_two_pointer:
            assert sum(result_two_pointer) == test["expected_sum"]
        if result_hash:
            assert sum(result_hash) == test["expected_sum"]


if __name__ == "__main__":
    main()
