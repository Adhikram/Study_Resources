package Questions.Graph;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class ShortestPath {
    public int[] shortestPath(int[][] edges, int n, int m, int src) {
        // Create an adjacency list for storing the undirected graph
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        // Populate the adjacency list
        for (int i = 0; i < m; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        // Initialize an array to store distances from source node to all other nodes
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE); // Initially set distances to infinity
        dist[src] = 0; // Distance to source node is 0

        // Breadth-First Search (BFS) Implementation
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(src); // Add source node to the queue

        while (!queue.isEmpty()) {
            int node = queue.poll(); // Remove and process the front node from the queue

            // Traverse all adjacent nodes of the current node
            for (int neighbor : adj.get(node)) {
                // Update distance if a shorter path is found
                if (dist[node] + 1 < dist[neighbor]) {
                    dist[neighbor] = dist[node] + 1;
                    queue.offer(neighbor); // Add the neighbor to the queue for further traversal
                }
            }
        }

        // Mark unreachable nodes as -1 in the resultant array
        for (int i = 0; i < n; i++) {
            if (dist[i] == Integer.MAX_VALUE) {
                dist[i] = -1;
            }
        }

        return dist;
    }

    // Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph
    // Space complexity: O(V), where V is the number of vertices in the graph

    public static void main(String[] args) {
        // Example usage
        int n = 5; // Number of nodes
        int m = 4; // Number of edges
        int src = 0; // Source node

        int[][] edges = { { 0, 1 }, { 1, 2 }, { 1, 3 }, { 2, 4 } };

        ShortestPath sp = new ShortestPath();
        int[] shortestDistances = sp.shortestPath(edges, n, m, src);

        // Print the shortest distances from the source node
        System.out.println("Shortest distances from the source node:");
        for (int i = 0; i < n; i++) {
            System.out.println("Node " + i + ": " + shortestDistances[i]);
        }
    }
}
