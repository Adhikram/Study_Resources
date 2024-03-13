package Questions.Greedy;

import java.util.Arrays;

public class MinimumPlatform {
    public static int calculateMinPlatforms(int at[], int dt[], int n) {
        // Write your code here.
        Arrays.sort(at);
        Arrays.sort(dt);
        int pt = 1;
        int result = 1;
        int atI = 1;
        int dtI = 0;
        while (atI < n) {
            if (at[atI] > dt[dtI]) {
                // Free a Platform
                pt--;
                dtI++;
            } else {
                // Need a Platform
                pt++;
                atI++;
            }
            result = Math.max(result, pt);
        }
        return result;
    }

    public static void main(String[] args) {
        int[] at = { 900, 940, 950, 1100, 1500, 1800 };
        int[] dt = { 910, 1200, 1120, 1130, 1900, 2000 };
        System.out.println(calculateMinPlatforms(at, dt, at.length));
    }
}
