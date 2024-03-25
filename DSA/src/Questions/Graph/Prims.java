package Questions.Graph;

import java.util.*;

import Questions.Graph.Dijkstra.Pair;

class Prims {

    // Function to find the sum of weights of edges of the Minimum Spanning Tree.
    static int spanningTree(int V, ArrayList<ArrayList<ArrayList<Integer>>> adj) {
        // Priority queue to store nodes based on their distance
        PriorityQueue<Pair> pq = new PriorityQueue<Pair>((x, y) -> x.distance - y.distance);

        // Array to keep track of visited nodes
        int[] vis = new int[V];

        // Add the starting node (node 0) to the priority queue with distance 0
        pq.add(new Pair(0, 0));

        // Variable to store the sum of edge weights
        int sum = 0;

        // Iterate until priority queue is empty
        while (!pq.isEmpty()) {
            // Extract the node with minimum distance
            int wt = pq.peek().distance;
            int node = pq.peek().node;
            pq.remove();

            // If the node is already visited, continue
            if (vis[node] == 1)
                continue;

            // Mark the node as visited and add its distance to the sum
            vis[node] = 1;
            sum += wt;

            // Traverse through the adjacent nodes
            for (int i = 0; i < adj.get(node).size(); i++) {
                int edW = adj.get(node).get(i).get(1);
                int adjNode = adj.get(node).get(i).get(0);

                // If the adjacent node is not visited, add it to the priority queue
                if (vis[adjNode] == 0) {
                    pq.add(new Pair(edW, adjNode));
                }
            }
        }
        return sum; // Return the sum of all the edge weights
    }

    /*
     * Time Complexity: O(E*logE) + O(E*logE)~ O(E*logE), where E = no. of given
     * edges.
     * The maximum size of the priority queue can be E so after at most E iterations
     * the priority queue will be empty and the loop will end. Inside the loop,
     * there is a pop operation that will take logE time. This will result in the
     * first O(E*logE) time complexity. Now, inside that loop, for every node, we
     * need to traverse all its adjacent nodes where the number of nodes can be at
     * most E. If we find any node unvisited, we will perform a push operation and
     * for that, we need a logE time complexity. So this will result in the second
     * O(E*logE).
     * 
     * Space Complexity: O(E) + O(V), where E = no. of edges and V = no. of
     * vertices. O(E) occurs due to the size of the priority queue and O(V) due to
     * the visited array. If we wish to get the mst, we need an extra O(V-1) space
     * to store the edges of the most.
     */

    public static void main(String[] args) {
        int V = 5; // Number of vertices
        ArrayList<ArrayList<ArrayList<Integer>>> adj = new ArrayList<ArrayList<ArrayList<Integer>>>();
        int[][] edges = { { 0, 1, 2 }, { 0, 2, 1 }, { 1, 2, 1 }, { 2, 3, 2 }, { 3, 4, 1 }, { 4, 2, 2 } };

        // Initialize adjacency list
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<ArrayList<Integer>>());
        }

        // Add edges to the adjacency list
        for (int i = 0; i < 6; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            int w = edges[i][2];

            ArrayList<Integer> tmp1 = new ArrayList<Integer>();
            ArrayList<Integer> tmp2 = new ArrayList<Integer>();
            tmp1.add(v);
            tmp1.add(w);

            tmp2.add(u);
            tmp2.add(w);

            adj.get(u).add(tmp1);
            adj.get(v).add(tmp2);
        }

        int sum = spanningTree(V, adj);
        // Print the sum of all the edge weights
        System.out.println("The sum of all the edge weights: " + sum);
    }
}
