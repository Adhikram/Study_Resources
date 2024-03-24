package Questions.Graph;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;

public class ShortestPathDag {
    // Function to perform Topological Sort using Depth-First Search (DFS)
    private void topoSort(int node, ArrayList<ArrayList<Pair>> adj, int[] vis, Stack<Integer> st) {
        vis[node] = 1; // Mark the current node as visited
        // Visit all adjacent nodes
        for (int i = 0; i < adj.get(node).size(); i++) {
            int v = adj.get(node).get(i).first;
            // If the adjacent node hasn't been visited yet, perform DFS on it
            if (vis[v] == 0) {
                topoSort(v, adj, vis, st);
            }
        }
        // After visiting all adjacent nodes, push the current node to the stack
        st.add(node);
    }

    // Function to find the shortest path from the source vertex to all other vertices
    public int[] shortestPath(int N, int M, int[][] edges) {
        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();
        // Initialize the adjacency list
        for (int i = 0; i < N; i++) {
            adj.add(new ArrayList<Pair>());
        }
        // Populate the adjacency list with the given edges
        for (int i = 0; i < M; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            int wt = edges[i][2];
            adj.get(u).add(new Pair(v, wt));
        }
        int[] vis = new int[N]; // Array to track visited nodes
        Stack<Integer> st = new Stack<>(); // Stack to store nodes in topological order
        // Perform Topological Sort
        for (int i = 0; i < N; i++) {
            if (vis[i] == 0) {
                topoSort(i, adj, vis, st);
            }
        }
        int[] dist = new int[N]; // Array to store shortest distances from the source vertex
        Arrays.fill(dist, Integer.MAX_VALUE); // Initialize distances to a large value
        dist[0] = 0; // Distance from source to itself is 0
        // Process vertices in topological order and update shortest distances
        while (!st.isEmpty()) {
            int node = st.pop();
            // Update distances to all adjacent nodes of the current node
            for (int i = 0; i < adj.get(node).size(); i++) {
                int v = adj.get(node).get(i).first;
                int wt = adj.get(node).get(i).second;
                if (dist[node] != Integer.MAX_VALUE && dist[node] + wt < dist[v]) {
                    dist[v] = wt + dist[node];
                }
            }
        }
        // Convert unreachable vertices (dist = Integer.MAX_VALUE) to -1
        for (int i = 0; i < N; i++) {
            if (dist[i] == Integer.MAX_VALUE) {
                dist[i] = -1;
            }
        }
        return dist; // Return the array of shortest distances
    }

    // Pair class for representing edges with weight
    class Pair {
        int first; // Vertex
        int second; // Weight

        Pair(int first, int second) {
            this.first = first;
            this.second = second;
        }
    }

    // Main method for testing
    public static void main(String[] args) {
        ShortestPathDag sp = new ShortestPathDag();
        int N = 5; // Number of vertices
        int M = 7; // Number of edges
        int[][] edges = {{0, 1, 4}, {0, 2, 1}, {1, 3, 1}, {1, 4, 3}, {2, 1, 2}, {2, 3, 5}, {3, 4, 3}}; // Edges
        int[] shortestDistances = sp.shortestPath(N, M, edges);
        System.out.println("Shortest distances from source vertex:");
        for (int i = 0; i < N; i++) {
            System.out.println(i + ": " + shortestDistances[i]);
        }
    }
}
