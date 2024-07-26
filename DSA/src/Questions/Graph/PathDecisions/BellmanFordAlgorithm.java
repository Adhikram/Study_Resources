package Questions.Graph.PathDecisions;

import java.util.ArrayList;
import java.util.Arrays;

public class BellmanFordAlgorithm {
    public static int[] bellmanFord(int V, ArrayList<ArrayList<Integer>> edges, int S) {
        // Initialize distance array with a large value for all vertices
        int[] dist = new int[V];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[S] = 0; // Distance from source to itself is 0

        // Relax edges V-1 times
        for (int i = 0; i < V - 1; i++) {
            for (ArrayList<Integer> edge : edges) {
                int u = edge.get(0);
                int v = edge.get(1);
                int wt = edge.get(2);

                // If there's a shorter path to vertex v through vertex u, update the distance
                if (dist[u] != Integer.MAX_VALUE && dist[u] + wt < dist[v]) {
                    dist[v] = dist[u] + wt;
                }
            }
        }

        // Check for negative cycles
        for (ArrayList<Integer> edge : edges) {
            int u = edge.get(0);
            int v = edge.get(1);
            int wt = edge.get(2);

            // If there's a shorter path to vertex v through vertex u, then there's a
            // negative cycle
            if (dist[u] != Integer.MAX_VALUE && dist[u] + wt < dist[v]) {
                // Return an array with a single element (-1) to indicate the presence of a
                // negative cycle
                return new int[] { -1 };
            }
        }

        return dist; // Return the distance array
    }
    // Time complexity: O(V * E), where V is the number of vertices and E is the number of edges in the graph
    // Space complexity: O(V), where V is the number of vertices in the graph

    public static void main(String[] args) {
        // Example usage
        int V = 5; // Number of vertices
        int S = 0; // Source vertex

        // Constructing the graph with edges represented as (source, destination,
        // weight)
        ArrayList<ArrayList<Integer>> edges = new ArrayList<>();
        edges.add(new ArrayList<>(Arrays.asList(0, 1, 5)));
        edges.add(new ArrayList<>(Arrays.asList(0, 2, 4)));
        edges.add(new ArrayList<>(Arrays.asList(1, 3, 3)));
        // edges.add(new ArrayList<>(Arrays.asList(2, 1, -6)));
        edges.add(new ArrayList<>(Arrays.asList(3, 2, 2)));
        edges.add(new ArrayList<>(Arrays.asList(4, 3, 1)));

        int[] shortestDistances = bellmanFord(V, edges, S);

        // Printing the shortest distances from source vertex
        System.out.println("Shortest distances from source vertex " + S + ":");
        for (int i = 0; i < shortestDistances.length; i++) {
            if (shortestDistances[i] == Integer.MAX_VALUE) {
                System.out.println("Vertex " + i + ": INF");
            } else {
                System.out.println("Vertex " + i + ": " + shortestDistances[i]);
            }
        }
    }
}
