"""
# Question: Minimum Time to Complete Trips
# Link: https://leetcode.com/problems/minimum-time-to-complete-trips/

# Time Complexity: O(n * log(max_time))
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search on time range
# 2. Calculate total trips possible
# 3. Find minimum time needed
"""


class MinTrips:
    def minimum_time(self, time: list[int], total_trips: int) -> int:
        left = 1
        right = min(time) * total_trips

        while left < right:
            mid = (left + right) >> 1
            trips = sum(mid // t for t in time)

            if trips >= total_trips:
                right = mid
            else:
                left = mid + 1

        return left


def main():
    solution = MinTrips()
    time = [1, 2, 3]
    total_trips = 5
    print(solution.minimum_time(time, total_trips))  # Expected: 3


if __name__ == "__main__":
    main()
