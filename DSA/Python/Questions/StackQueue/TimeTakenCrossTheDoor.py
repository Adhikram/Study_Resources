"""
# Question: Time Taken to Cross the Door
# Link: https://leetcode.com/problems/time-taken-to-cross-the-door/

# Calculate time for each person to cross the door

# Time Complexity: O(n)
# Space Complexity: O(n)

# Algorithm:
# 1. Use two queues for enter and exit requests
# 2. Track previous door usage
# 3. Handle door crossing rules
# 4. Return crossing times array

# Key Components:
# - time_taken(): Main implementation
# - Queue management for enter/exit
# - Door state tracking
"""

from collections import deque
from typing import List


class TimeTakenCrossTheDoor:
    def time_taken(self, arrival: List[int], state: List[int]) -> List[int]:
        ans = [0] * len(arrival)
        time = 0

        # Build queues for enter and exit
        enter_q = deque()
        exit_q = deque()

        for i in range(len(state)):
            if state[i] == 0:
                enter_q.append(i)
            else:
                exit_q.append(i)

        prev = 1  # Handle first rule at time = 0

        while enter_q and exit_q:
            # Two or more persons at door
            if arrival[enter_q[0]] <= time and arrival[exit_q[0]] <= time:
                if prev == 0:
                    idx = enter_q.popleft()
                    ans[idx] = time
                else:
                    idx = exit_q.popleft()
                    ans[idx] = time
            # Only person to enter
            elif arrival[enter_q[0]] <= time:
                idx = enter_q.popleft()
                ans[idx] = time
                prev = 0
            # Only person to exit
            elif arrival[exit_q[0]] <= time:
                idx = exit_q.popleft()
                ans[idx] = time
                prev = 1
            # No one at door
            else:
                prev = 1
                time = min(arrival[enter_q[0]], arrival[exit_q[0]]) - 1
            time += 1

        # Clear remaining queues
        while enter_q:
            idx = enter_q.popleft()
            ans[idx] = max(arrival[idx], time)
            time = max(arrival[idx], time) + 1

        while exit_q:
            idx = exit_q.popleft()
            ans[idx] = max(arrival[idx], time)
            time = max(arrival[idx], time) + 1

        return ans


def main():
    solution = TimeTakenCrossTheDoor()
    arrival = [0, 1, 1, 2, 4]
    state = [0, 1, 0, 0, 1]
    print(solution.time_taken(arrival, state))


if __name__ == "__main__":
    main()
