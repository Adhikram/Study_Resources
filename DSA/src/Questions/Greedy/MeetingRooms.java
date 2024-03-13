package Questions.Greedy;

import java.util.Arrays;


public class MeetingRooms {
    public static int maximumMeetings(int[] start, int[] end) {
        // Write your code here.
        int n = start.length;
        int[][] meetings = new int[n][2];
        for (int i = 0; i < n; i++) {
            meetings[i][0] = start[i];
            meetings[i][1] = end[i];
        }
        Arrays.sort(meetings, (a, b) -> (a[1] - b[1]));

        int lastMeeting = meetings[0][1];
        int maxMeetings = 1;
        for (int[] meeting : meetings) {
            if (meeting[0] > lastMeeting) {
                maxMeetings++;
                lastMeeting = meeting[1];
            }
        }
        return maxMeetings;

    }

    public static void main(String[] args) {
        int[] start = { 1, 3, 0, 5, 8, 5 };
        int[] end = { 2, 4, 6, 7, 9, 9 };
        System.out.println(maximumMeetings(start, end));
    }
}
