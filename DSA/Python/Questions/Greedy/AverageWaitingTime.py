"""
# Question: Average Waiting Time
# Link: https://leetcode.com/problems/average-waiting-time/

# Calculate average waiting time for customers in a restaurant

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Track current time and total waiting time
# 2. Process each customer order
# 3. Calculate waiting time based on arrival and preparation
# 4. Return average waiting time
"""


class AverageWaitingTime:
    def average_waiting_time(self, customers: list[list[int]]) -> float:
        curr_time = 0
        total_wait = 0

        for arrival, prep in customers:
            # Update current time
            curr_time = max(curr_time, arrival)

            # Calculate finish time
            finish_time = curr_time + prep

            # Calculate waiting time
            wait_time = finish_time - arrival
            total_wait += wait_time

            # Update current time
            curr_time = finish_time

        return total_wait / len(customers)


def main():
    solution = AverageWaitingTime()
    customers = [[1, 2], [2, 5], [4, 3]]
    print(solution.average_waiting_time(customers))  # Expected: 5.00000


if __name__ == "__main__":
    main()
