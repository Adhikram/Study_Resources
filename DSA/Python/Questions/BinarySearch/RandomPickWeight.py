"""
# Question: Random Pick with Weight
# Link: https://leetcode.com/problems/random-pick-with-weight/

# Time Complexity: 
# - Constructor: O(n)
# - PickIndex: O(log n)
# Space Complexity: O(n)

# Algorithm:
# 1. Create cumulative sum array
# 2. Binary search for random value
# 3. Return weighted random index
"""

import random


class RandomPickWeight:
    def __init__(self, w: list[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pick_index(self) -> int:
        target = random.random() * self.total_sum
        left, right = 0, len(self.prefix_sums) - 1

        while left < right:
            mid = (left + right) >> 1
            if self.prefix_sums[mid] > target:
                right = mid
            else:
                left = mid + 1

        return left


def main():
    solution = RandomPickWeight([1, 3, 2, 4])
    print(solution.pick_index())  # Random output based on weights


if __name__ == "__main__":
    main()
