"""
# Question: Koko Eating Bananas
# Link: https://leetcode.com/problems/koko-eating-bananas/

# Problem Statement:
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
# The guards have gone and will come back in h hours.
# Find the minimum integer k such that Koko can eat all the bananas within h hours.

# Example:
# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Explanation: Koko can eat 4 bananas per hour to finish all bananas in 8 hours.
"""

from typing import List
import math


class EatingBananas:
    def min_eating_speed_binary(self, piles: List[int], h: int) -> int:
        """
        Binary search approach to find minimum eating speed
        Time Complexity: O(n * log(max(piles)))
        Space Complexity: O(1)
        """
        left, right = 1, max(piles)

        while left < right:
            k = (left + right) >> 1
            hours = sum(math.ceil(pile / k) for pile in piles)

            if hours <= h:
                right = k
            else:
                left = k + 1

        return left

    def min_eating_speed_linear(self, piles: List[int], h: int) -> int:
        """
        Linear search approach (less efficient but demonstrates concept)
        Time Complexity: O(n * max(piles))
        Space Complexity: O(1)
        """
        k = 1
        while True:
            hours = sum(math.ceil(pile / k) for pile in piles)
            if hours <= h:
                return k
            k += 1

    def calculate_hours(self, piles: List[int], k: int) -> int:
        """
        Helper function to calculate total hours needed for given speed
        """
        return sum(math.ceil(pile / k) for pile in piles)


def main():
    test_cases = [
        {"piles": [3, 6, 7, 11], "h": 8, "expected": 4},
        {"piles": [30, 11, 23, 4, 20], "h": 5, "expected": 30},
        {"piles": [30, 11, 23, 4, 20], "h": 6, "expected": 23},
    ]

    solution = EatingBananas()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Piles: {test['piles']}")
        print(f"Hours: {test['h']}")
        result_binary = solution.min_eating_speed_binary(test["piles"], test["h"])
        print(f"Binary Search Result: {result_binary}")
        print(f"Expected: {test['expected']}")
        assert result_binary == test["expected"], f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
