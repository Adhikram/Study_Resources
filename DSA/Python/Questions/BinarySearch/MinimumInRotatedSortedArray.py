"""
# Question: Find Minimum in Rotated Sorted Array II
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

# Time Complexity: O(log n) average, O(n) worst case
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search with duplicates handling
# 2. Compare with right neighbor
# 3. Handle rotation and duplicate cases
"""


class MinimumInRotatedSortedArray:
    def find_min(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) >> 1

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]


def main():
    solution = MinimumInRotatedSortedArray()
    nums = [2, 2, 2, 0, 1]
    print(solution.find_min(nums))  # Expected: 0


if __name__ == "__main__":
    main()
