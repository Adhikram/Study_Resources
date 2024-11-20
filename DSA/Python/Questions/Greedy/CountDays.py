"""
# Question: Count Days
# Count days needed to complete tasks with given time constraints

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Track current time
# 2. Process each task duration
# 3. Handle daily time limit
# 4. Return total days needed
"""


class CountDays:
    def count_days(self, tasks: list[int], daily_limit: int) -> int:
        days = 1
        current_time = 0

        for task in tasks:
            # Check if task fits in current day
            if current_time + task <= daily_limit:
                current_time += task
            else:
                # Start new day
                days += 1
                current_time = task

        return days


def main():
    solution = CountDays()
    tasks = [1, 2, 3, 4, 2]
    daily_limit = 8
    print(
        solution.count_days(tasks, daily_limit)
    )  # Expected output depends on test case


if __name__ == "__main__":
    main()
