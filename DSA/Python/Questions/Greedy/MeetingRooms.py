"""
# Question: Meeting Rooms
# Link: https://leetcode.com/problems/meeting-rooms-ii/

# Time Complexity: O(n log n)
# Space Complexity: O(n)

# Algorithm:
# 1. Separate start and end times
# 2. Sort both arrays
# 3. Use two pointers to track overlaps
# 4. Return maximum rooms needed
"""


class MeetingRooms:
    def min_meeting_rooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # Separate and sort start/end times
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)

        rooms = 0
        max_rooms = 0
        s = 0  # start pointer
        e = 0  # end pointer

        while s < len(intervals):
            if start_times[s] < end_times[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            max_rooms = max(max_rooms, rooms)

        return max_rooms


def main():
    solution = MeetingRooms()
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(solution.min_meeting_rooms(intervals))  # Expected: 2


if __name__ == "__main__":
    main()
