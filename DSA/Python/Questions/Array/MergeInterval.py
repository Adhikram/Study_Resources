"""
# Question: Merge Intervals
# Link: https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals and return the non-overlapping intervals.

# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for storing result

# Algorithm:
# 1. Sort intervals based on start time
# 2. Iterate through sorted intervals
# 3. Merge overlapping intervals by updating end time
# 4. Add non-overlapping intervals to result

# Key Components:
# - merge(): Main function implementing interval merging
# - Sorting with custom lambda for interval comparison
# - Dynamic result building with overlap checking
"""

from typing import List


class MergeInterval:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])
        result = []

        for interval in intervals:
            if not result:
                result.append(interval)
            else:
                last_interval = result[-1]

                if last_interval[1] >= interval[0]:
                    last_interval[1] = max(last_interval[1], interval[1])
                else:
                    result.append(interval)

        return result


def main():
    solution = MergeInterval()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = solution.merge(intervals)
    print(result)  # Expected output: [[1, 6], [8, 10], [15, 18]]


if __name__ == "__main__":
    main()
