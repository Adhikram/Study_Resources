"""
# Question: Merge Two Sorted Arrays
# Merge two sorted arrays in-place with optimal space usage

# Time Complexity: O(m + n) where m and n are lengths of input arrays
# Space Complexity: O(1) as we modify arrays in-place

# Algorithm:
# 1. Start from end of both arrays
# 2. Compare and swap elements to maintain sorted order
# 3. Handle remaining elements from second array
# 4. Use final_size pointer for placement

# Key Components:
# - merge(): Main function implementing in-place merge
# - Three-pointer technique with swapping
"""

from typing import List


class MergeTwoSortedArray:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        final_size = len(nums1) - 1
        m -= 1
        n -= 1

        while m > -1 and n > -1:
            if nums1[m] < nums2[n]:
                nums1[final_size], nums2[n] = nums2[n], nums1[final_size]
                n -= 1
            else:
                nums1[final_size], nums1[m] = nums1[m], nums1[final_size]
                m -= 1
            final_size -= 1

        while n > -1:
            nums1[final_size], nums2[n] = nums2[n], nums1[final_size]
            n -= 1
            final_size -= 1


def main():
    solution = MergeTwoSortedArray()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    solution.merge(nums1, 3, nums2, 3)
    print(nums1)  # Expected output: [1, 2, 2, 3, 5, 6]


if __name__ == "__main__":
    main()
