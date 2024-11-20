"""
# Question: Single Element in a Sorted Array
# Link: https://leetcode.com/problems/single-element-in-a-sorted-array/

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search with pair checking
# 2. Find pattern break
# 3. Return single element
"""


class SingleElement:
    def single_non_duplicate(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) >> 1

            # Ensure mid is even
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]


def main():
    solution = SingleElement()
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    print(solution.single_non_duplicate(nums))  # Expected: 2


if __name__ == "__main__":
    main()
