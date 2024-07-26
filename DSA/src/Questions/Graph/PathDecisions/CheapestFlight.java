package Questions.Graph.PathDecisions;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class CheapestFlight {
    static class Pair {
        int destination; // Destination airport
        int cost; // Cost of the flight

        Pair(int destination, int cost) {
            this.destination = destination;
            this.cost = cost;
        }
    }

    static class Tuple {
        int stops; // Number of stops
        int node; // Current node (airport)
        int cost; // Cost to reach the current node

        Tuple(int stops, int node, int cost) {
            this.stops = stops;
            this.node = node;
            this.cost = cost;
        }
    }

    public int cheapestFlight(int n, int[][] flights, int src, int dst, int K) {
        // Create the adjacency list to represent airports and flights in the form of a
        // graph
        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        // Populate the adjacency list with flight information
        for (int[] flight : flights) {
            int sourceAirport = flight[0];
            int destinationAirport = flight[1];
            int cost = flight[2];
            adj.get(sourceAirport).add(new Pair(destinationAirport, cost));
        }

        // Create a queue to store nodes and their distances from the source, along with
        // the number of stops
        Queue<Tuple> q = new LinkedList<>();
        q.add(new Tuple(0, src, 0));

        // Initialize distance array to store updated distances from the source
        int[] dist = new int[n];
        Arrays.fill(dist, (int) 1e9);
        dist[src] = 0;

        // Iterate through the graph using a queue similar to Dijkstra's algorithm,
        // popping out the element with the minimum number of stops first
        while (!q.isEmpty()) {
            Tuple it = q.poll();
            int stops = it.stops;
            int node = it.node;
            int cost = it.cost;

            // Stop the process if the limit for the number of stops is reached
            if (stops > K)
                continue;

            // Traverse through adjacent nodes and update the queue with shorter distances
            for (Pair adjacentFlight : adj.get(node)) {
                int adjNode = adjacentFlight.destination;
                int edgeWeight = adjacentFlight.cost;

                // Update the queue if the new calculated distance is less than the previous
                if (cost + edgeWeight < dist[adjNode] && stops <= K) {
                    dist[adjNode] = cost + edgeWeight;
                    q.add(new Tuple(stops + 1, adjNode, cost + edgeWeight));
                }
            }
        }

        // If the destination node is unreachable, return -1; otherwise, return the
        // calculated distance
        if (dist[dst] == (int) 1e9)
            return -1;
        return dist[dst];
    }
    // Time complexity: O(n * m), where n is the number of airports and m is the number of flights
    // Space complexity: O(n)

    // Example usage
    public static void main(String[] args) {
        CheapestFlight cheapestFlight = new CheapestFlight();
        int n = 5; // Number of airports
        int[][] flights = { { 0, 1, 100 }, { 1, 2, 100 }, { 0, 2, 500 } };
        int src = 0; // Source airport
        int dst = 2; // Destination airport
        int K = 1; // Maximum number of stops allowed

        int result = cheapestFlight.cheapestFlight(n, flights, src, dst, K);
        System.out.println("Cheapest flight cost: " + result);
    }
}
