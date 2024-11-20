"""
# Question: Course Schedule
# Link: https://leetcode.com/problems/course-schedule/

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

# Algorithm:
# 1. Build adjacency list from prerequisites
# 2. DFS to detect cycles
# 3. Return whether all courses can be completed
"""

from collections import defaultdict


class CourseSchedule:
    def can_finish(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = set()
        path = set()

        def dfs(course: int) -> bool:
            if course in path:
                return False
            if course in visited:
                return True

            path.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            path.remove(course)
            visited.add(course)
            return True

        for course in range(num_courses):
            if not dfs(course):
                return False

        return True


def main():
    solution = CourseSchedule()
    prerequisites = [[1, 0], [0, 1]]
    print(solution.can_finish(2, prerequisites))


if __name__ == "__main__":
    main()
