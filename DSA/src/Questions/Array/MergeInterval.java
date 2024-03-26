// File: questions/MergeInterval.java
package Questions.Array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeInterval {
    static int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1];
            }
            return a[0] - b[0];
        });
        List<int[]> result = new ArrayList<>();

        for (int[] interval : intervals) {
            if (result.isEmpty()) {
                result.add(interval);
            } else {
                // Pointing to the last interval from the result
                int[] lastInterval = result.get(result.size() - 1);

                if (lastInterval[1] >= interval[0]) {
                    lastInterval[1] = Math.max(lastInterval[1], interval[1]);
                } else {
                    result.add(interval);
                }
            }
        }
        return result.toArray(new int[result.size()][]);
    }

    public static void main(String[] args) {
        int[][] intervals = new int[][] { { 1, 3 }, { 2, 6 }, { 8, 10 }, { 15, 18 } };
        int[][] result = merge(intervals);
        for (int[] interval : result) {
            System.out.println(Arrays.toString(interval));
        }
    }
}
