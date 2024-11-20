"""
# Question: Task Scheduler
# Link: https://leetcode.com/problems/task-scheduler/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Count frequency of each task
# 2. Find maximum frequency task
# 3. Calculate idle slots needed
# 4. Return minimum time required
"""

from collections import Counter


class TaskSchedule:
    def least_interval(self, tasks: list[str], n: int) -> int:
        # Count task frequencies
        frequencies = Counter(tasks)
        max_freq = max(frequencies.values())
        max_count = sum(1 for freq in frequencies.values() if freq == max_freq)

        # Calculate minimum intervals needed
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)


def main():
    solution = TaskSchedule()
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(solution.least_interval(tasks, n))  # Expected: 8


if __name__ == "__main__":
    main()
