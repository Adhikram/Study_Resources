"""
# Question: Kth Element of Two Sorted Arrays
# Problem Statement:
# Given two sorted arrays arr1 and arr2 of size m and n respectively, find the kth element of the merged sorted array.

# Example:
# Input: arr1 = [2,3,6,7,9], arr2 = [1,4,8,10], k = 5
# Output: 6
# Explanation: Merged array is [1,2,3,4,6,7,8,9,10], 5th element is 6
"""

from typing import List
import heapq


class KthElement:
    def find_kth_binary(self, arr1: List[int], arr2: List[int], k: int) -> int:
        """
        Binary search approach
        Time Complexity: O(log(min(m,n)))
        Space Complexity: O(1)
        """
        if len(arr1) > len(arr2):
            return self.find_kth_binary(arr2, arr1, k)

        n1, n2 = len(arr1), len(arr2)
        left, right = max(0, k - n2), min(k, n1)

        while left <= right:
            cut1 = (left + right) >> 1
            cut2 = k - cut1

            left1 = float("-inf") if cut1 == 0 else arr1[cut1 - 1]
            left2 = float("-inf") if cut2 == 0 else arr2[cut2 - 1]
            right1 = float("inf") if cut1 == n1 else arr1[cut1]
            right2 = float("inf") if cut2 == n2 else arr2[cut2]

            if left1 <= right2 and left2 <= right1:
                return max(left1, left2)
            elif left1 > right2:
                right = cut1 - 1
            else:
                left = cut1 + 1

        return -1

    def find_kth_heap(self, arr1: List[int], arr2: List[int], k: int) -> int:
        """
        Heap-based approach
        Time Complexity: O(k * log(2))
        Space Complexity: O(1)
        """
        heap = []
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2) and k > 0:
            if arr1[i] < arr2[j]:
                heapq.heappush(heap, arr1[i])
                i += 1
            else:
                heapq.heappush(heap, arr2[j])
                j += 1
            k -= 1

        while i < len(arr1) and k > 0:
            heapq.heappush(heap, arr1[i])
            i += 1
            k -= 1

        while j < len(arr2) and k > 0:
            heapq.heappush(heap, arr2[j])
            j += 1
            k -= 1

        return heap[-1]

    def find_kth_merge(self, arr1: List[int], arr2: List[int], k: int) -> int:
        """
        Two-pointer merge approach
        Time Complexity: O(k)
        Space Complexity: O(1)
        """
        i, j = 0, 0
        count = 0
        result = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result = arr1[i]
                i += 1
            else:
                result = arr2[j]
                j += 1
            count += 1
            if count == k:
                return result

        while i < len(arr1) and count < k:
            result = arr1[i]
            i += 1
            count += 1

        while j < len(arr2) and count < k:
            result = arr2[j]
            j += 1
            count += 1

        return result


def main():
    test_cases = [
        {"arr1": [2, 3, 6, 7, 9], "arr2": [1, 4, 8, 10], "k": 5, "expected": 6},
        {"arr1": [1, 3, 5, 7], "arr2": [2, 4, 6, 8], "k": 4, "expected": 4},
        {"arr1": [1, 2, 3, 4, 5], "arr2": [6, 7, 8, 9, 10], "k": 7, "expected": 7},
    ]

    solution = KthElement()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Array1: {test['arr1']}")
        print(f"Array2: {test['arr2']}")
        print(f"k: {test['k']}")

        result_binary = solution.find_kth_binary(test["arr1"], test["arr2"], test["k"])
        result_heap = solution.find_kth_heap(test["arr1"], test["arr2"], test["k"])
        result_merge = solution.find_kth_merge(test["arr1"], test["arr2"], test["k"])

        print(f"Binary Search Result: {result_binary}")
        print(f"Heap Result: {result_heap}")
        print(f"Merge Result: {result_merge}")
        print(f"Expected: {test['expected']}")

        assert result_binary == result_heap == result_merge == test["expected"]


if __name__ == "__main__":
    main()
