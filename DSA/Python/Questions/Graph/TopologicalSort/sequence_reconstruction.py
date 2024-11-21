"""
# Question: Sequence Reconstruction
# Link: https://leetcode.com/problems/sequence-reconstruction/

# Problem Statement:
# You are given an integer array nums of length n where nums is a permutation of the integers in the range [1, n].
# You are also given a 2D integer array sequences where sequences[i] is a subsequence of nums.
# Check if nums is the shortest possible and the only supersequence. The shortest supersequence is a sequence
# with the shortest length and has all sequences[i] as subsequences. There could be multiple valid supersequences
# for the given array sequences.

# Example:
# Input: nums = [1,2,3], sequences = [[1,2],[1,3]]
# Output: False
# Explanation: There are two possible supersequences: [1,2,3] and [1,3,2].
"""

from typing import List
from collections import defaultdict, deque

# 1. Topological Sort Solution
"""
Algorithm:
1. Build a graph from the sequences with edges representing order constraints.
2. Calculate in-degrees for each node.
3. Use a queue to perform topological sorting.
4. Check if there is exactly one valid topological order that matches nums.

Time Complexity: O(V + E) where V is the number of nodes and E is the number of edges.
Space Complexity: O(V + E)
"""


def sequence_reconstruction(nums: List[int], sequences: List[List[int]]) -> bool:
    # Build graph and calculate in-degrees
    graph = defaultdict(list)
    in_degree = {i: 0 for i in nums}

    for seq in sequences:
        for i in range(len(seq) - 1):
            u, v = seq[i], seq[i + 1]
            graph[u].append(v)
            in_degree[v] += 1

    # Initialize queue with nodes having zero in-degree
    queue = deque([node for node in nums if in_degree[node] == 0])

    index = 0
    while queue:
        if len(queue) > 1:
            return False  # More than one way to reconstruct

        current = queue.popleft()
        if nums[index] != current:
            return False  # Order does not match nums

        index += 1
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return index == len(nums)


def main():
    test_cases = [
        {"nums": [1, 2, 3], "sequences": [[1, 2], [1, 3]], "expected": False},
        {"nums": [1, 2, 3], "sequences": [[1, 2]], "expected": False},
        {"nums": [1, 2, 3], "sequences": [[1, 2], [1, 3], [2, 3]], "expected": True},
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"nums: {test['nums']}")
        print(f"sequences: {test['sequences']}")
        result = sequence_reconstruction(test["nums"], test["sequences"])
        print(f"Result: {result}, Expected: {test['expected']}")
        assert result == test["expected"], f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
