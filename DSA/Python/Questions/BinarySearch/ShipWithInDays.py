"""
# Question: Capacity To Ship Packages Within D Days
# Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

# Time Complexity: O(n * log(sum(weights)))
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search on capacity range
# 2. Check if capacity is sufficient
# 3. Find minimum valid capacity
"""


class ShipWithInDays:
    def ship_within_days(self, weights: list[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) >> 1

            if self.can_ship(weights, days, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def can_ship(self, weights: list[int], days: int, capacity: int) -> bool:
        required_days = 1
        current_load = 0

        for weight in weights:
            if current_load + weight > capacity:
                required_days += 1
                current_load = weight
            else:
                current_load += weight

        return required_days <= days


def main():
    solution = ShipWithInDays()
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5
    print(solution.ship_within_days(weights, days))  # Expected: 15


if __name__ == "__main__":
    main()
