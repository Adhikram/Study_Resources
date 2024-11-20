"""
# Question: Search in Rotated Sorted Array II
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

# Time Complexity: O(log n) average, O(n) worst case
# Space Complexity: O(1)

# Algorithm:
# 1. Handle duplicates by shrinking search space
# 2. Find pivot with duplicates
# 3. Binary search with duplicates
"""


class SearchInRotatedSortedArray2:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1

            if nums[mid] == target:
                return True

            # Handle duplicates
            if nums[left] == nums[mid]:
                left += 1
                continue

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

        return False


def main():
    solution = SearchInRotatedSortedArray2()
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    print(solution.search(nums, target))  # Expected: True


if __name__ == "__main__":
    main()
