"""
# Question: Parallel Courses
# Link: https://leetcode.com/problems/parallel-courses/

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

# Algorithm:
# 1. Build graph from course dependencies
# 2. Use BFS for level-wise traversal
# 3. Return minimum semesters needed
"""

from collections import defaultdict, deque


class ParallelCourses:
    def minimum_semesters(self, n: int, relations: list[list[int]]) -> int:
        # Build graph and calculate in-degree
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)

        for prev, next_course in relations:
            graph[prev].append(next_course)
            in_degree[next_course] += 1

        # Start with courses having no prerequisites
        queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
        semesters = 0
        courses_taken = 0

        while queue:
            size = len(queue)
            semesters += 1

            for _ in range(size):
                course = queue.popleft()
                courses_taken += 1

                for next_course in graph[course]:
                    in_degree[next_course] -= 1
                    if in_degree[next_course] == 0:
                        queue.append(next_course)

        return semesters if courses_taken == n else -1


def main():
    solution = ParallelCourses()
    relations = [[1, 2], [2, 3], [3, 1]]
    print(solution.minimum_semesters(3, relations))


if __name__ == "__main__":
    main()
