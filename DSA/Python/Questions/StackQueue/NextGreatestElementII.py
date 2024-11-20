"""
# Question: Next Greater Element II
# Link: https://leetcode.com/problems/next-greater-element-ii/

# Find next greater element in circular array

# Time Complexity: O(n)
# Space Complexity: O(n)

# Algorithm:
# 1. Process array twice for circular property
# 2. Use stack to track indices
# 3. Handle circular array wrapping
# 4. Return array of next greater elements

# Key Components:
# - next_greater_elements(): Main implementation
# - Stack for index tracking
# - Circular array handling
"""

from typing import List


class NextGreatestElementII:
    def next_greater_elements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []  # stack to store indices

        # Process array twice to handle circular property
        for i in range(2 * n):
            num = nums[i % n]

            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num

            if i < n:
                stack.append(i)

        return result


def main():
    solution = NextGreatestElementII()
    nums = [1, 2, 1]
    result = solution.next_greater_elements(nums)
    print(" ".join(map(str, result)))  # Expected: [2, -1, 2]


if __name__ == "__main__":
    main()
