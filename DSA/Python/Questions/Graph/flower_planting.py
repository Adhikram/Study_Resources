"""
# Question: Flower Planting With No Adjacent
# Link: https://leetcode.com/problems/flower-planting-with-no-adjacent/

# Problem Statement:
# You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional path between garden xi to garden yi.
# In each garden, you want to plant one of 4 types of flowers. There are no restrictions on the type of flower planted in each garden except that no two adjacent gardens have the same type of flower.
# Return any such a choice as an array answer where answer[i] is the type of flower planted in the (i+1)th garden. The flower types are denoted 1, 2, 3, or 4.

# Example:
# Input: n = 3, paths = [[1,2],[2,3],[3,1]]
# Output: [1,2,3]
"""

from typing import List
from collections import defaultdict

# Solution using graph coloring
"""
Algorithm:
1. Build an adjacency list from the paths.
2. Initialize an array to store the flower type for each garden.
3. For each garden, choose a flower type that is not used by its adjacent gardens.
4. Return the array of flower types.

Time Complexity: O(N + E) where N is the number of gardens and E is the number of paths.
Space Complexity: O(N + E) for the adjacency list and flower type array.
"""


def garden_no_adj(n: int, paths: List[List[int]]) -> List[int]:
    adj_list = defaultdict(list)
    for x, y in paths:
        adj_list[x].append(y)
        adj_list[y].append(x)

    flowers = [0] * n

    for garden in range(1, n + 1):
        used_flowers = {flowers[neighbor - 1] for neighbor in adj_list[garden]}
        for flower in range(1, 5):
            if flower not in used_flowers:
                flowers[garden - 1] = flower
                break

    return flowers


def main():
    test_cases = [
        {"n": 3, "paths": [[1, 2], [2, 3], [3, 1]], "expected": [1, 2, 3]},
        {"n": 4, "paths": [[1, 2], [3, 4]], "expected": [1, 2, 1, 2]},
        {
            "n": 4,
            "paths": [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]],
            "expected": [1, 2, 3, 4],
        },
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"n: {test['n']}, paths: {test['paths']}")
        result = garden_no_adj(test["n"], test["paths"])
        print(f"Result: {result}, Expected: {test['expected']}")
        # Note: The expected results may vary in order, so sorting might be necessary for comparison
        assert sorted(result) == sorted(test["expected"]), f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
