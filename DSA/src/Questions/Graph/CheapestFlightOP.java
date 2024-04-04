package Questions.Graph;

import java.util.Arrays;

public class CheapestFlightOP {
    public static int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
         int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[src] = 0;
        for (int i = 0; i <= k; i++) {
            if (isRoutePossible(distance, flights)) {
                break;
            }
        }
        return distance[dst] == Integer.MAX_VALUE ? -1 : distance[dst];
    }
    private static boolean isRoutePossible(int[] dist, int[][] flights) {
        int[] copy = Arrays.copyOf(dist, dist.length);
        boolean result = true;

        for (int[] flight : flights) {
            int src = flight[0];
            int dst = flight[1];
            int  cost = flight[2];

            if (copy[src] != Integer.MAX_VALUE && dist[dst] > copy[src] + cost) {
                dist[dst] = cost + copy[src];
                result = false;
            }
        }
        return result;
    }

    // Time Complexity: O(k * E) where E is the number of flights
    // Space Complexity: O(n)
    public static void main(String[] args) {
        int n = 3;
        int[][] flights = {{0, 1, 100}, {1, 2, 100}, {0, 2, 500}};
        int src = 0;
        int dst = 2;
        int k = 1;
        System.out.println(findCheapestPrice(n, flights, src, dst, k));
    }
}
