"""
# Question: Parallel Courses II
# Link: https://leetcode.com/problems/parallel-courses-ii/

# Problem Statement:
# You are given an integer n, which indicates that there are n courses labeled from 1 to n.
# You are also given an array relations where relations[i] = [prevCoursei, nextCoursei],
# representing a prerequisite relationship between courses: course prevCoursei has to be
# taken before course nextCoursei. Also, you are given the integer k.
# Return the minimum number of semesters needed to take all courses. If there is no way
# to take all the courses, return -1.

# Example:
# Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
# Output: 3
# Explanation: The figure above represents the given graph.
# In the first semester, you can take courses 2 and 3.
# In the second semester, you can take course 1.
# In the third semester, you can take course 4.
"""

from typing import List
from collections import defaultdict, deque

# 1. BFS with State Compression
"""
Algorithm:
1. Build adjacency list and calculate in-degrees
2. Use BFS to process courses level by level
3. For each level, try all possible combinations of k courses
4. Track taken courses using bitmask
5. Return minimum number of semesters needed

Time Complexity: O(2^n * n)
Space Complexity: O(2^n)
"""


def min_number_of_semesters(n: int, relations: List[List[int]], k: int) -> int:
    # Build prerequisites graph
    prereq = defaultdict(list)
    in_degree = [0] * (n + 1)

    for prev, next in relations:
        prereq[prev].append(next)
        in_degree[next] += 1

    # Initialize queue with courses having no prerequisites
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    semesters = 0
    courses_taken = 0

    while queue:
        size = len(queue)
        if size > k:
            # Take k courses with maximum outgoing edges
            courses = list(queue)
            courses.sort(key=lambda x: len(prereq[x]), reverse=True)
            courses = courses[:k]
            queue = deque(courses)
            size = k

        # Process current semester
        for _ in range(size):
            course = queue.popleft()
            courses_taken += 1

            # Update prerequisites for dependent courses
            for next_course in prereq[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        semesters += 1

    return semesters if courses_taken == n else -1


# 2. Dynamic Programming with Bitmask
"""
Algorithm:
1. Use bitmask to represent taken courses
2. For each state, try all possible combinations of k courses
3. Memoize results for each state
4. Check prerequisites before taking courses
5. Return minimum semesters needed

Time Complexity: O(2^n * nCk)
Space Complexity: O(2^n)
"""


def min_number_of_semesters_dp(n: int, relations: List[List[int]], k: int) -> int:
    # Create prerequisite mask for each course
    prereq = [0] * n
    for prev, next in relations:
        prereq[next - 1] |= 1 << (prev - 1)

    dp = [-1] * (1 << n)
    dp[0] = 0

    def solve(mask: int) -> int:
        if dp[mask] != -1:
            return dp[mask]

        # Find available courses
        available = 0
        for i in range(n):
            if not (mask & (1 << i)) and (prereq[i] & mask) == prereq[i]:
                available |= 1 << i

        if not available:
            return float("inf")

        # Try all combinations of k courses
        result = float("inf")
        curr = available
        while curr:
            if bin(curr).count("1") <= k:
                result = min(result, 1 + solve(mask | curr))
            curr = (curr - 1) & available

        dp[mask] = result
        return result

    result = solve(0)
    return result if result != float("inf") else -1


def main():
    test_cases = [
        {"n": 4, "relations": [[2, 1], [3, 1], [1, 4]], "k": 2, "expected": 3},
        {"n": 5, "relations": [[2, 1], [3, 1], [4, 1], [1, 5]], "k": 2, "expected": 4},
        {"n": 3, "relations": [[1, 2], [2, 3], [3, 1]], "k": 1, "expected": -1},
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"n: {test['n']}")
        print(f"Relations: {test['relations']}")
        print(f"k: {test['k']}")
        print(f"Expected: {test['expected']}")
        print(
            f"BFS Solution: {min_number_of_semesters(test['n'], test['relations'], test['k'])}"
        )
        print(
            f"DP Solution: {min_number_of_semesters_dp(test['n'], test['relations'], test['k'])}"
        )


if __name__ == "__main__":
    main()
