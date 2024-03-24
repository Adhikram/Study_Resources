package Questions.Graph;

import java.util.*;

public class Dijkstra {

    static class Pair {
        int distance; // Distance from source
        int node; // Node index

        Pair(int distance, int node) {
            this.distance = distance;
            this.node = node;
        }
    }

    static int[] dijkstra(int V, ArrayList<ArrayList<ArrayList<Integer>>> adj, int S) {
        // Create a priority queue for storing nodes with their distances
        PriorityQueue<Pair> pq = new PriorityQueue<>((x, y) -> x.distance - y.distance);

        // Initialize distance array with a large value to indicate unvisited nodes
        int[] dist = new int[V];
        Arrays.fill(dist, (int) 1e9);

        // Set distance of source node to 0 and add it to the priority queue
        dist[S] = 0;
        pq.add(new Pair(0, S));

        // Process nodes in priority order
        while (!pq.isEmpty()) {
            int dis = pq.peek().distance;
            int node = pq.peek().node;
            pq.remove();

            // Traverse all adjacent nodes of the current node
            for (ArrayList<Integer> edge : adj.get(node)) {
                int adjNode = edge.get(0); // Adjacent node index
                int edgeWeight = edge.get(1); // Edge weight

                // If the current distance + edge weight is less than the stored distance,
                // update the distance and add the adjacent node to the priority queue
                if (dis + edgeWeight < dist[adjNode]) {
                    dist[adjNode] = dis + edgeWeight;
                    pq.add(new Pair(dist[adjNode], adjNode));
                }
            }
        }

        // Return the list containing shortest distances from the source to all nodes
        return dist;
    }

    // Time complexity: O(E * log(V)), where V is the number of vertices and E is the number of edges in the graph
    // Space complexity: O(V), where V is the number of vertices in the graph
    // Main method for testing
    public static void main(String[] args) {
        // Example usage
        int V = 5; // Number of vertices
        ArrayList<ArrayList<ArrayList<Integer>>> adj = new ArrayList<>(); // Adjacency list
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }
        adj.get(0).add(new ArrayList<>(Arrays.asList(1, 4))); // Edge from 0 to 1 with weight 4
        adj.get(0).add(new ArrayList<>(Arrays.asList(2, 1))); // Edge from 0 to 2 with weight 1
        adj.get(1).add(new ArrayList<>(Arrays.asList(3, 1))); // Edge from 1 to 3 with weight 1
        adj.get(1).add(new ArrayList<>(Arrays.asList(4, 3))); // Edge from 1 to 4 with weight 3
        adj.get(2).add(new ArrayList<>(Arrays.asList(1, 2))); // Edge from 2 to 1 with weight 2
        adj.get(2).add(new ArrayList<>(Arrays.asList(3, 5))); // Edge from 2 to 3 with weight 5
        // Add more edges as needed

        int[] shortestDistances = dijkstra(V, adj, 0); // Calculate shortest distances from source node 0
        System.out.println("Shortest distances from source vertex:");
        for (int i = 0; i < V; i++) {
            System.out.println(i + ": " + shortestDistances[i]);
        }
    }
}
