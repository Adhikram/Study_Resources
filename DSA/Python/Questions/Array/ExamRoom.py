"""
# Question: Exam Room
# Link: https://leetcode.com/problems/exam-room/

# Design a system to seat students in an exam room with following rules:
# - Students sit as far as possible from each other
# - When multiple positions have same distance, use lower numbered seat
# - Distance is calculated from nearest student or walls

# Time Complexity: 
# - seat(): O(n) where n is number of seated students
# - leave(): O(n) for list operations

# Space Complexity: O(n) where n is the number of seated students

# Algorithm:
# 1. seat():
#    - If room empty, place at position 0
#    - Calculate maximum distance between consecutive seats
#    - Consider distance from start (0) and end (n-1)
#    - Place student at position that maximizes distance
# 2. leave():
#    - Remove student from given position
"""

class ExamRoom:
    def __init__(self, n: int):
        self.capacity = n
        self.seats = []

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0

        max_distance = self.seats[0]  # Distance from start
        seat_number = 0

        for i in range(1, len(self.seats)):
            distance = (self.seats[i] - self.seats[i-1]) // 2
            if distance > max_distance:
                max_distance = distance
                seat_number = self.seats[i-1] + distance

        # Check distance from end
        if self.capacity - 1 - self.seats[-1] > max_distance:
            seat_number = self.capacity - 1

        # Insert at correct position to maintain order
        insert_pos = 0
        while insert_pos < len(self.seats) and self.seats[insert_pos] < seat_number:
            insert_pos += 1
        self.seats.insert(insert_pos, seat_number)
        return seat_number

    def leave(self, p: int) -> None:
        self.seats.remove(p)


def main():
    exam_room = ExamRoom(10)
    print(exam_room.seat())  # 0
    print(exam_room.seat())  # 9
    print(exam_room.seat())  # 4
    print(exam_room.seat())  # 2
    exam_room.leave(4)
    print(exam_room.seat())  # 5


if __name__ == "__main__":
    main()
