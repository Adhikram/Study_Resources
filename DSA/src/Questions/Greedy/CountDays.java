package Questions.Greedy;

import java.util.Arrays;

public class CountDays {
    public int countDays(int days, int[][] meetings) {
        int diff = meetings[0][0] - 1;
        Arrays.sort(meetings,  (a, b) -> {
            if (a[0] == b[0]) {
                return a[1] - b[1];
            }
            return a[0] - b[0];
        });
        Arrays.stream(meetings).forEach(meeting -> System.out.println(Arrays.toString(meeting)));
        int[] lastInterval = meetings[0];
        for(int i = 1; i < meetings.length; i++){
            System.out.println("Diff: " + diff);
            System.out.println("Last Interval: " + Arrays.toString(lastInterval));
            System.out.println("Current Interval: " + Arrays.toString(meetings[i]));
            if (lastInterval[1] < meetings[i][0]){
                // get the diffs
                diff += (meetings[i][0] - lastInterval[1]);
            }
        }
        diff += ( days - lastInterval[1]) ;
        return diff;
    }

    public static void main(String[] args) {
        int[][] meetings = new int[][] { { 1, 3 }, { 2, 6 }, { 8, 10 }, { 15, 18 } };
        CountDays countDays = new CountDays();
        System.out.println(countDays.countDays(20, meetings));
    }

}
