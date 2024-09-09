package Questions.BinarySearch;

import java.util.Arrays;
/*
https://leetcode.com/problems/minimum-time-to-complete-trips/
 Time Complexity: O(n * log(m)) where n is the length of the time array and m is the maximum possible time (min(time) * totalTrips). This is because we perform binary search on the range [1, min(time) * totalTrips] and for each mid-point, we calculate the number of trips in O(n).
Space Complexity: O(1) as we use a constant amount of extra space.

Binary Search:
    left = 1, right = min(time) * totalTrips
    while left < right:
        mid = (left + right) / 2
        if numTrips(time, mid) >= totalTrips:
            right = mid
        else:
            left = mid + 1
    return left
numTrips:
    totalTrips = 0
    for t in time:
        totalTrips += mid / t
    return totalTrips
 */
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
