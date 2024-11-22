"""
# Question: Median of Two Sorted Arrays
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

# Problem Statement:
# Given two sorted arrays nums1 and nums2, find the median of the combined sorted array.
# The overall run time complexity should be O(log(m+n)).

# Example:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.0
# Explanation: Merged array = [1,2,3], median is 2.0
"""

from typing import List


class MedianOfSortedArrays:
    def find_median_binary(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Binary search approach
        Time Complexity: O(log(min(m,n)))
        Space Complexity: O(1)
        """
        if len(nums1) > len(nums2):
            return self.find_median_binary(nums2, nums1)

        n1, n2 = len(nums1), len(nums2)
        left, right = 0, n1

        while left <= right:
            partition1 = (left + right) >> 1
            partition2 = (n1 + n2 + 1) // 2 - partition1

            left1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            right1 = float("inf") if partition1 == n1 else nums1[partition1]
            left2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            right2 = float("inf") if partition2 == n2 else nums2[partition2]

            if left1 <= right2 and left2 <= right1:
                if (n1 + n2) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                right = partition1 - 1
            else:
                left = partition1 + 1

        return 0.0

    def find_median_merge(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Merge approach
        Time Complexity: O(m+n)
        Space Complexity: O(m+n)
        """
        merged = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        n = len(merged)
        if n % 2 == 0:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
        return float(merged[n // 2])

    def find_median_optimized(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Space optimized approach without merging arrays
        Time Complexity: O(m+n)
        Space Complexity: O(1)
        """
        total = len(nums1) + len(nums2)
        half = total // 2
        i = j = count = 0
        prev = curr = 0

        while count <= half:
            prev = curr
            if i == len(nums1):
                curr = nums2[j]
                j += 1
            elif j == len(nums2):
                curr = nums1[i]
                i += 1
            elif nums1[i] <= nums2[j]:
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
            count += 1

        if total % 2 == 0:
            return (prev + curr) / 2
        return float(curr)


def main():
    test_cases = [
        {"nums1": [1, 3], "nums2": [2], "expected": 2.0},
        {"nums1": [1, 2], "nums2": [3, 4], "expected": 2.5},
        {"nums1": [], "nums2": [1], "expected": 1.0},
    ]

    solution = MedianOfSortedArrays()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"nums1: {test['nums1']}")
        print(f"nums2: {test['nums2']}")

        result_binary = solution.find_median_binary(test["nums1"], test["nums2"])
        result_merge = solution.find_median_merge(test["nums1"], test["nums2"])
        result_optimized = solution.find_median_optimized(test["nums1"], test["nums2"])

        print(f"Binary Search Result: {result_binary}")
        print(f"Merge Result: {result_merge}")
        print(f"Optimized Result: {result_optimized}")
        print(f"Expected: {test['expected']}")

        assert abs(result_binary - test["expected"]) < 1e-6
        assert abs(result_merge - test["expected"]) < 1e-6
        assert abs(result_optimized - test["expected"]) < 1e-6


if __name__ == "__main__":
    main()
