"""
# Question: Split Array Largest Sum
# Link: https://leetcode.com/problems/split-array-largest-sum/

# Time Complexity: O(n * log(sum(nums)))
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search on sum range
# 2. Check if split is possible
# 3. Find minimum largest sum
"""


class SplitArrayLargestSum:
    def split_array(self, nums: list[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) >> 1

            if self.can_split(nums, m, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def can_split(self, nums: list[int], m: int, target: int) -> bool:
        count = 1
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum > target:
                count += 1
                current_sum = num
                if count > m:
                    return False

        return True


def main():
    solution = SplitArrayLargestSum()
    nums = [7, 2, 5, 10, 8]
    m = 2
    print(solution.split_array(nums, m))  # Expected: 18


if __name__ == "__main__":
    main()
