package Questions.Graph.PathDecisions;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

public class BusRoutes {
    public int numBusesToDestinationBFS(int[][] routes, int source, int target) {
        if (source == target) {
            return 0;
        }

        // Map each stop to the list of buses (routes) that go through it
        Map<Integer, List<Integer>> stopToBuses = new HashMap<>();
        for (int i = 0; i < routes.length; i++) {
            for (int stop : routes[i]) {
                stopToBuses.computeIfAbsent(stop, k -> new ArrayList<>()).add(i);
            }
        }

        // BFS initialization
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visitedStops = new HashSet<>();
        Set<Integer> visitedBuses = new HashSet<>();
        queue.offer(source);
        visitedStops.add(source);
        int buses = 0;

        // BFS loop
        while (!queue.isEmpty()) {
            int size = queue.size();
            buses++;
            for (int i = 0; i < size; i++) {
                int currentStop = queue.poll();
                for (int bus : stopToBuses.getOrDefault(currentStop, new ArrayList<>())) {
                    if (visitedBuses.contains(bus)) {
                        continue;
                    }
                    visitedBuses.add(bus);
                    for (int stop : routes[bus]) {
                        if (stop == target) {
                            return buses;
                        }
                        if (!visitedStops.contains(stop)) {
                            visitedStops.add(stop);
                            queue.offer(stop);
                        }
                    }
                }
            }
        }

        return -1;
    }
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
        // Bellman Ford Algorithm
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
        // Arrays.stream(minBusesToReach).forEach(System.out::println);
        return (minBusesToReach[target] < n + 1 ? minBusesToReach[target] : -1);
    }

    public static void main(String[] args) {
        BusRoutes busRoutes = new BusRoutes();
        System.out.println(busRoutes.numBusesToDestination(new int[][] { { 1, 2, 7 }, { 3, 6, 7 } }, 1, 6));
        System.out.println(busRoutes.numBusesToDestinationBFS(new int[][] { { 1, 2, 7 }, { 3, 6, 7 } }, 1, 6));
        System.out.println(busRoutes.numBusesToDestination(new int[][] { { 7, 12 }, { 4, 5, 15 }, { 6 }, { 15, 19 }, { 9, 12, 13 } }, 15, 12));
        System.out.println(busRoutes.numBusesToDestinationBFS(new int[][] { { 7, 12 }, { 4, 5, 15 }, { 6 }, { 15, 19 }, { 9, 12, 13 } }, 15, 12));
    }
}
