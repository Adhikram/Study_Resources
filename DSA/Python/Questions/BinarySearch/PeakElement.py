"""
# Question: Find Peak Element
# Link: https://leetcode.com/problems/find-peak-element/

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search for peak
# 2. Compare with neighbors
# 3. Move towards higher neighbor
"""


class PeakElement:
    def find_peak_element(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) >> 1

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left


def main():
    solution = PeakElement()
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(solution.find_peak_element(nums))  # Expected: 5 (6 is a peak element)


if __name__ == "__main__":
    main()
