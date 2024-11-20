"""
# Question: Course Schedule II
# Link: https://leetcode.com/problems/course-schedule-ii/

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

# Algorithm:
# 1. Build adjacency list from prerequisites
# 2. Perform topological sort using DFS
# 3. Return course order or empty if cycle exists
"""

from collections import defaultdict


class CourseSchedule2:
    def find_order(self, num_courses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = set()
        path = set()
        order = []

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
            order.append(course)
            return True

        for course in range(num_courses):
            if not dfs(course):
                return []

        return order


def main():
    solution = CourseSchedule2()
    prerequisites = [[1, 0]]
    print(solution.find_order(2, prerequisites))


if __name__ == "__main__":
    main()
