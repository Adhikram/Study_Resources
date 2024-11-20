"""
# Question: Kth Smallest Element in a Sorted Matrix
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Time Complexity: O(n * log(max-min))
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search on value range
# 2. Count elements less than mid
# 3. Find kth smallest element
"""


class KthSmallestElementInMatrix:
    def kth_smallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n - 1][n - 1]

        while left < right:
            mid = (left + right) >> 1
            count = self.count_less_equal(matrix, mid)

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left

    def count_less_equal(self, matrix: list[list[int]], target: int) -> int:
        n = len(matrix)
        count = 0
        col = n - 1

        for row in range(n):
            while col >= 0 and matrix[row][col] > target:
                col -= 1
            count += col + 1

        return count


def main():
    solution = KthSmallestElementInMatrix()
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(solution.kth_smallest(matrix, k))  # Expected: 13


if __name__ == "__main__":
    main()
