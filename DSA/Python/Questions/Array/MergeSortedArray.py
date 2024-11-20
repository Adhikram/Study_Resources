"""
# Question: Merge Sorted Array
# Link: https://leetcode.com/problems/merge-sorted-array/

# Given two sorted arrays nums1 and nums2, merge them in-place into nums1
# nums1 has enough space at the end to hold nums2

# Time Complexity: O(m + n) where m and n are lengths of input arrays
# Space Complexity: O(1) as we modify nums1 in-place

# Algorithm:
# 1. Start from end of both arrays
# 2. Compare elements and place larger one at end of nums1
# 3. Handle remaining elements from nums2 if any
# 4. Special case when m = 0

# Key Components:
# - merge(): Main function implementing in-place merge
# - Three-pointer technique (i, j, k)
"""

from typing import List


class MergeSortedArray:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        if m == 0:
            nums1[:n] = nums2[:n]
            return

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


def main():
    solution = MergeSortedArray()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    solution.merge(nums1, 3, nums2, 3)
    print(nums1)  # Expected output: [1, 2, 2, 3, 5, 6]


if __name__ == "__main__":
    main()
