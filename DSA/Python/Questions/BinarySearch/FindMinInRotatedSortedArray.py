"""
# Question: Find Minimum in Rotated Sorted Array
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search to find pivot point
# 2. Compare with right neighbor
# 3. Handle rotation cases
"""


class FindMinInRotatedSortedArray:
    def find_min(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) >> 1

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


def main():
    solution = FindMinInRotatedSortedArray()
    nums = [3, 4, 5, 1, 2]
    print(solution.find_min(nums))  # Expected: 1


if __name__ == "__main__":
    main()
