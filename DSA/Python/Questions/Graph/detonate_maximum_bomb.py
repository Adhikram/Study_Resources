"""
# Question: Detonate the Maximum Bombs
# Link: https://leetcode.com/problems/detonate-the-maximum-bombs/

# Problem Statement:
# You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt.
# This area is in the shape of a circle with the center as the location of the bomb.
# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri].
# xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.
# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range.
# These bombs will further detonate the bombs that lie in their ranges.
# Return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

# Example:
# Input: bombs = [[2,1,3],[6,1,4]]
# Output: 2
# Explanation: If we detonate the right bomb, both bombs will be detonated.
"""

from typing import List
from collections import deque

# 1. BFS Solution
"""
Algorithm:
1. Build a graph where each bomb is a node and an edge exists if one bomb can detonate another.
2. For each bomb, perform a BFS to count the number of bombs that can be detonated.
3. Track the maximum number of bombs detonated from any starting bomb.

Time Complexity: O(N^2) where N is the number of bombs.
Space Complexity: O(N^2) for the adjacency list.
"""


def maximum_detonation(bombs: List[List[int]]) -> int:
    def is_in_range(bomb1, bomb2) -> bool:
        x1, y1, r1 = bomb1
        x2, y2, _ = bomb2
        return (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r1**2

    n = len(bombs)
    graph = [[] for _ in range(n)]

    # Build the graph
    for i in range(n):
        for j in range(n):
            if i != j and is_in_range(bombs[i], bombs[j]):
                graph[i].append(j)

    def bfs(start: int) -> int:
        queue = deque([start])
        visited = [False] * n
        visited[start] = True
        count = 1

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    count += 1
        return count

    max_detonated = 0
    for i in range(n):
        max_detonated = max(max_detonated, bfs(i))

    return max_detonated


def main():
    test_cases = [
        {"bombs": [[2, 1, 3], [6, 1, 4]], "expected": 2},
        {"bombs": [[1, 1, 5], [10, 10, 5]], "expected": 1},
        {
            "bombs": [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]],
            "expected": 5,
        },
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Bombs: {test['bombs']}")
        result = maximum_detonation(test["bombs"])
        print(f"Result: {result}, Expected: {test['expected']}")
        assert result == test["expected"], f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
