"""
# Question: Koko Eating Bananas
# Link: https://leetcode.com/problems/koko-eating-bananas/

# Time Complexity: O(n * log(max(piles)))
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search on eating speed
# 2. Calculate hours needed for each speed
# 3. Find minimum valid speed
"""

import math


class EatingBananas:
    def min_eating_speed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            k = (left + right) >> 1
            hours = sum(math.ceil(pile / k) for pile in piles)

            if hours <= h:
                right = k
            else:
                left = k + 1

        return left


def main():
    solution = EatingBananas()
    piles = [3, 6, 7, 11]
    h = 8
    print(solution.min_eating_speed(piles, h))  # Expected: 4


if __name__ == "__main__":
    main()
