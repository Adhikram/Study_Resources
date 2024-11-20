"""
# Question: Search in Rotated Sorted Array
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Algorithm:
# 1. Find pivot using binary search
# 2. Determine which half to search
# 3. Binary search in chosen half
"""


class SearchInRotatedSortedArray:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


def main():
    solution = SearchInRotatedSortedArray()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(solution.search(nums, target))  # Expected: 4


if __name__ == "__main__":
    main()
