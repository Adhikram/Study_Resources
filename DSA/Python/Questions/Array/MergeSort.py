"""
# Question: Merge Sort Implementation
# Classic divide and conquer sorting algorithm

# Time Complexity: O(n log n)
# Space Complexity: O(n) for temporary arrays

# Algorithm:
# 1. Divide array into two halves recursively
# 2. Sort each half independently
# 3. Merge sorted halves into single sorted array

# Key Components:
# - merge(): Combines two sorted subarrays
# - merge_sort(): Main recursive function
# - In-place merging with temporary arrays
"""

from typing import List


class MergeSort:
    def merge(self, arr: List[int], l: int, m: int, r: int) -> None:
        # Find sizes of two subarrays
        n1, n2 = m - l + 1, r - m

        # Create temporary arrays
        left = [arr[l + i] for i in range(n1)]
        right = [arr[m + 1 + i] for i in range(n2)]

        # Merge temporary arrays back into arr[l..r]
        i = j = 0
        k = l

        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements if any
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1

    def merge_sort(self, arr: List[int], l: int, r: int) -> None:
        if l < r:
            m = (l + r) >> 1
            self.merge_sort(arr, l, m)
            self.merge_sort(arr, m + 1, r)
            self.merge(arr, l, m, r)


def main():
    solution = MergeSort()
    arr = [12, 11, 13, 5, 6, 7]
    solution.merge_sort(arr, 0, len(arr) - 1)
    print(arr)  # Expected output: [5, 6, 7, 11, 12, 13]


if __name__ == "__main__":
    main()
