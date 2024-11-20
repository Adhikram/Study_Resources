"""
# Question: Two Sum in Rotated Sorted Array
# Find pair of numbers that sum to target in rotated sorted array

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Find pivot point
# 2. Use two pointers
# 3. Handle rotation while searching
"""


class TwoSumRotated:
    def find_pair(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        pivot = self.find_pivot(nums)
        left = pivot
        right = (pivot - 1) % n

        while left != right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return [nums[left], nums[right]]
            elif current_sum < target:
                left = (left + 1) % n
            else:
                right = (right - 1 + n) % n

        return []

    def find_pivot(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return left


def main():
    solution = TwoSumRotated()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 6
    print(solution.find_pair(nums, target))  # Expected: [4, 2] or similar valid pair


if __name__ == "__main__":
    main()
