"""
# Question: Maximum Subsequence Score
# Link: https://leetcode.com/problems/maximum-subsequence-score/

# Problem Statement:
# Given two arrays nums1 and nums2 of equal length n and an integer k.
# Choose a subsequence of indices of length k from nums1 to maximize:
# sum of selected elements from nums1 multiplied by minimum of selected elements from nums2.

# Example:
# Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
# Output: 12
# Explanation: Selected indices: [0,2,3]. Score = (1+3+2) * min(2,3,4) = 6 * 2 = 12
"""

from typing import List
import heapq


class MaximumSubsequentScore:
    def max_score(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        Calculate maximum score using heap-based approach
        Time Complexity: O(nlogn) for sorting + O(nlogk) for heap operations
        Space Complexity: O(n) for pairs array + O(k) for heap
        """
        # Create pairs of (nums2[i], nums1[i]) and sort by nums2 in descending order
        pairs = sorted(zip(nums2, nums1), reverse=True)

        # Initialize min heap to track k largest elements from nums1
        heap = []
        sum_k = 0
        max_score = 0

        # Process each pair
        for min_val, curr_val in pairs:
            heapq.heappush(heap, curr_val)
            sum_k += curr_val

            # If heap size exceeds k, remove smallest element
            if len(heap) > k:
                sum_k -= heapq.heappop(heap)

            # Update max_score when we have k elements
            if len(heap) == k:
                max_score = max(max_score, sum_k * min_val)

        return max_score


def main():
    test_cases = [
        {"nums1": [1, 3, 3, 2], "nums2": [2, 1, 3, 4], "k": 3, "expected": 12},
        {"nums1": [4, 2, 3, 1, 1], "nums2": [7, 5, 10, 9, 6], "k": 1, "expected": 30},
    ]

    solution = MaximumSubsequentScore()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"nums1: {test['nums1']}")
        print(f"nums2: {test['nums2']}")
        print(f"k: {test['k']}")
        result = solution.max_score(test["nums1"], test["nums2"], test["k"])
        print(f"Expected: {test['expected']}")
        print(f"Result: {result}")
        assert result == test["expected"], f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
