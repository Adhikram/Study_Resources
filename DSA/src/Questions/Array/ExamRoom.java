package Questions.Array;

import java.util.TreeSet;

class ExamRoom {
    TreeSet<Integer> seats;
    int capacity;

    public ExamRoom(int n) {
        this.capacity = n;
        this.seats = new TreeSet<>();
    }

    public int seat() {
        if (seats.isEmpty()) {
            seats.add(0);
            return 0;
        }

        int maxDistance = seats.first(); // Distance from the start
        int seatNumber = 0;
        Integer prev = null;

        for (int currentSeat : seats) {
            if (prev != null) {
                int distance = (currentSeat - prev) / 2;
                if (distance > maxDistance) {
                    maxDistance = distance;
                    seatNumber = prev + distance;
                }
            }
            prev = currentSeat;
        }

        // Check distance from the end
        if (capacity - 1 - seats.last() > maxDistance) {
            seatNumber = capacity - 1;
        }

        seats.add(seatNumber);
        return seatNumber;
    }

    public void leave(int p) {
        seats.remove(p);
    }

    public static void main(String[] args) {
        ExamRoom examRoom = new ExamRoom(10);
        System.out.println(examRoom.seat()); // 0
        System.out.println(examRoom.seat()); // 9
        System.out.println(examRoom.seat()); // 4
        System.out.println(examRoom.seat()); // 2
        examRoom.leave(4);
        System.out.println(examRoom.seat()); // 5
    }
}

