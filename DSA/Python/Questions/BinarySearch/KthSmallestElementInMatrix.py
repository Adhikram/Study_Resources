"""
# Question: Kth Smallest Element in a Sorted Matrix
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Problem Statement:
# Given an n x n matrix where each row and column is sorted in ascending order,
# find the kth smallest element in the matrix.

# Example:
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in sorted order are [1,5,9,10,11,12,13,13,15]
"""

from typing import List
import heapq


class KthSmallestElementInMatrix:
    def kth_smallest_binary(self, matrix: List[List[int]], k: int) -> int:
        """
        Binary search approach using count of elements less than mid
        Time Complexity: O(n * log(max-min))
        Space Complexity: O(1)
        """
        n = len(matrix)
        left, right = matrix[0][0], matrix[n - 1][n - 1]

        while left < right:
            mid = (left + right) >> 1
            count = self.count_less_equal(matrix, mid)

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left

    def count_less_equal(self, matrix: List[List[int]], target: int) -> int:
        """Helper function to count elements less than or equal to target"""
        count = 0
        n = len(matrix)
        col = n - 1

        for row in range(n):
            while col >= 0 and matrix[row][col] > target:
                col -= 1
            count += col + 1

        return count

    def kth_smallest_heap(self, matrix: List[List[int]], k: int) -> int:
        """
        Min-heap approach
        Time Complexity: O(k * log(n))
        Space Complexity: O(n)
        """
        n = len(matrix)
        heap = [(matrix[0][0], 0, 0)]
        visited = {(0, 0)}

        for _ in range(k - 1):
            val, row, col = heapq.heappop(heap)

            for new_row, new_col in [(row + 1, col), (row, col + 1)]:
                if new_row < n and new_col < n and (new_row, new_col) not in visited:
                    heapq.heappush(heap, (matrix[new_row][new_col], new_row, new_col))
                    visited.add((new_row, new_col))

        return heapq.heappop(heap)[0]

    def kth_smallest_flatten(self, matrix: List[List[int]], k: int) -> int:
        """
        Flatten and sort approach (less efficient but simple)
        Time Complexity: O(n^2 * log(n^2))
        Space Complexity: O(n^2)
        """
        flattened = []
        for row in matrix:
            flattened.extend(row)
        return sorted(flattened)[k - 1]


def main():
    test_cases = [
        {"matrix": [[1, 5, 9], [10, 11, 13], [12, 13, 15]], "k": 8, "expected": 13},
        {"matrix": [[1, 2], [1, 3]], "k": 2, "expected": 1},
        {"matrix": [[-5]], "k": 1, "expected": -5},
    ]

    solution = KthSmallestElementInMatrix()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Matrix: {test['matrix']}")
        print(f"k: {test['k']}")

        result_binary = solution.kth_smallest_binary(test["matrix"], test["k"])
        result_heap = solution.kth_smallest_heap(test["matrix"], test["k"])
        result_flatten = solution.kth_smallest_flatten(test["matrix"], test["k"])

        print(f"Binary Search Result: {result_binary}")
        print(f"Heap Result: {result_heap}")
        print(f"Flatten Result: {result_flatten}")
        print(f"Expected: {test['expected']}")

        assert result_binary == result_heap == result_flatten == test["expected"]


if __name__ == "__main__":
    main()
