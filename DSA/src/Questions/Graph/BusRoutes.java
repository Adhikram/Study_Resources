package Questions.Graph;

import java.util.Arrays;

public class BusRoutes {
    public int numBusesToDestination(int[][] routes, int source, int target) {
        if (source == target) {
            return 0;
        }
        int maxStop = -1;
        for (int[] route : routes) {
            for (int stop : route) {
                maxStop = Math.max(maxStop, stop);
            }
        }
        if (maxStop < target || maxStop < source) {
            return -1;
        }
        int n = routes.length;
        int[] minBusesToReach = new int[maxStop + 1];
        Arrays.fill(minBusesToReach, n + 1);
        minBusesToReach[source] = 0;
        boolean flag = true;
        while (flag) {
            flag = false;
            for (int[] route : routes) {
                int min = n + 1;
                for (int stop : route) {
                    min = Math.min(min, minBusesToReach[stop]);
                }
                min++;
                for (int stop : route) {
                    if (minBusesToReach[stop] > min) {
                        minBusesToReach[stop] = min;
                        flag = true;
                    }
                }
            }

        }
        return (minBusesToReach[target] < n + 1 ? minBusesToReach[target] : -1);
    }

    public static void main(String[] args) {
        BusRoutes busRoutes = new BusRoutes();
        System.out.println(busRoutes.numBusesToDestination(new int[][] { { 1, 2, 7 }, { 3, 6, 7 } }, 1, 6));
        System.out.println(busRoutes.numBusesToDestination(new int[][] { { 7, 12 }, { 4, 5, 15 }, { 6 }, { 15, 19 }, { 9, 12, 13 } }, 15, 12));
    }
}
