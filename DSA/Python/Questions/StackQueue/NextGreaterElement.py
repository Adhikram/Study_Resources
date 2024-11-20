"""
# Question: Next Greater Element
# Link: https://leetcode.com/problems/next-greater-element-i/

# Find next greater element for each number in array

# Time Complexity: O(n)
# Space Complexity: O(n)

# Algorithm:
# 1. Use stack to track potential next greater elements
# 2. Process array from right to left
# 3. Map numbers to their next greater elements
# 4. Return result array

# Key Components:
# - solve(): Main implementation
# - Stack for element tracking
# - HashMap for result mapping
"""

from typing import List


class NextGreaterElement:
    def solve(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [-1]
        num_map = {}

        # Process nums2 from right to left
        for i in range(len(nums2) - 1, -1, -1):
            while stack[-1] != -1 and stack[-1] < nums2[i]:
                stack.pop()

            num_map[nums2[i]] = stack[-1]
            stack.append(nums2[i])

        # Build result array using the map
        for i in range(len(nums1)):
            nums1[i] = num_map.get(nums1[i], -1)

        return nums1


def main():
    solution = NextGreaterElement()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    result = solution.solve(nums1, nums2)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
