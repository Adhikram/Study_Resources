package Questions.BinarySearch;

import java.util.Arrays;

public class MinTrips {
    // Time complexity: O(n * log(m)), where n = time.length, m = totalTrips
    public long minimumTime(int[] time, int totalTrips) {
        long l = 1;
        long r = Arrays.stream(time).min().getAsInt() * (long) totalTrips;

        while (l < r) {
            final long m = (l + r) / 2;
            if (numTrips(time, m) >= totalTrips)
                r = m;
            else
                l = m + 1;
        }

        return l;
    }

    private long numTrips(int[] time, long m) {
        long totalTrips = 0;
        for (int t : time) {
            totalTrips += m / t;
        }
        return totalTrips;
    }

    public static void main(String[] args) {
        MinTrips minTrips = new MinTrips();
        System.out.println(minTrips.minimumTime(new int[] { 1, 2, 3, 3 }, 12));
    }
}
