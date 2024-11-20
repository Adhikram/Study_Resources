"""
# Question: Maximum Subsequence Score
# Link: https://leetcode.com/problems/maximum-subsequence-score/

# Find maximum score from subsequence combinations

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# Algorithm:
# 1. Sort by efficiency in descending order
# 2. Use min heap for speed values
# 3. Track running sum of speeds
# 4. Calculate maximum score

# Key Components:
# - max_score(): Main implementation
# - Priority queue for speed tracking
# - Sorting for efficiency optimization
"""

import heapq
from typing import List


class MaximumSubsequentScore:
    def max_score(self, speed: List[int], efficiency: List[int], k: int) -> int:
        # Create pairs of efficiency and speed
        ess = sorted(zip(efficiency, speed), reverse=True)

        pq = []  # min heap
        sum_s = 0
        res = 0

        for eff, spd in ess:
            heapq.heappush(pq, spd)
            sum_s += spd

            if len(pq) > k:
                sum_s -= heapq.heappop(pq)

            if len(pq) == k:
                res = max(res, sum_s * eff)

        return res


def main():
    solution = MaximumSubsequentScore()
    speed = [1, 3, 3, 2]
    efficiency = [2, 1, 3, 4]
    k = 3
    print(solution.max_score(speed, efficiency, k))


if __name__ == "__main__":
    main()
