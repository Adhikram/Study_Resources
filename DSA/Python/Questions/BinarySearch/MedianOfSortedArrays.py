"""
# Question: Median of Two Sorted Arrays
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

# Time Complexity: O(log(min(m,n)))
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search on smaller array
# 2. Find partition points
# 3. Calculate median
"""


class MedianOfSortedArrays:
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            return self.find_median_sorted_arrays(nums2, nums1)

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


def main():
    solution = MedianOfSortedArrays()
    nums1 = [1, 3]
    nums2 = [2]
    print(solution.find_median_sorted_arrays(nums1, nums2))  # Expected: 2.0


if __name__ == "__main__":
    main()
