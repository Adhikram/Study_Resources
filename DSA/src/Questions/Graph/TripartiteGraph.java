package Questions.Graph;

public class TripartiteGraph {

    // Depth First Search (DFS) function to check if the graph is tripartite
    public static boolean dfs(int node, int c, int[] color, int[][] graph) {
        // If the color of the current node is not 0 (unvisited), check if it matches
        // the expected color 'c'
        if (color[node] != 0) {
            return color[node] == c;
        }
        // Color the current node with the given color 'c'
        color[node] = c;
        // Traverse all neighbors of the current node
        for (int neighbor : graph[node]) {
            // Recursively check if the neighbors can be colored with the opposite color
            // (-c)
            if (!dfs(neighbor, -c, color, graph)) {
                return false; // If not, return false
            }
        }
        return true; // If all neighbors can be colored properly, return true
    }

    // Function to check if the graph is tripartite
    public static boolean isTripartite(int n, int[][] graph) {
        int[] color = new int[n]; // Array to store the color of each node (0 for unvisited)
        // Traverse all nodes in the graph
        for (int i = 0; i < n; i++) {
            // If the current node is unvisited and cannot be colored properly, return false
            if (color[i] == 0 && !dfs(i, 1, color, graph)) {
                return false;
            }
        }
        return true; // If all nodes can be colored properly, return true
    }

    public static void main(String[] args) {
        int n = 4; // Number of nodes in the graph
        int[][] graph = { { 0, 1 }, { 1, 1 }, { 2, 0 } }; // Adjacency list representation of the graph
        int[][] graph1 = { { 0, 1 }, { 1, 2 }, { 2, 3 }, { 3, 0 } }; // Adjacency list representation of the graph
        System.out.println("Is the graph tripartite? " + isTripartite(n, graph1));
        System.out.println("Is the graph tripartite? " + isTripartite(n, graph));
    }
}
