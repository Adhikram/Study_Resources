"""
# Question: Minimum Platforms
# Find minimum number of platforms needed for a railway station

# Time Complexity: O(n log n)
# Space Complexity: O(1)

# Algorithm:
# 1. Sort arrival and departure times separately
# 2. Use two pointers to track trains
# 3. Count overlapping schedules
# 4. Return maximum platforms needed
"""


class MinimumPlatform:
    def find_platform(self, arrival: list[int], departure: list[int]) -> int:
        arrival.sort()
        departure.sort()

        platforms = 0
        max_platforms = 0
        i = 0  # arrival pointer
        j = 0  # departure pointer

        while i < len(arrival):
            if arrival[i] <= departure[j]:
                platforms += 1
                i += 1
            else:
                platforms -= 1
                j += 1
            max_platforms = max(max_platforms, platforms)

        return max_platforms


def main():
    solution = MinimumPlatform()
    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]
    print(solution.find_platform(arrival, departure))  # Expected: 3


if __name__ == "__main__":
    main()
