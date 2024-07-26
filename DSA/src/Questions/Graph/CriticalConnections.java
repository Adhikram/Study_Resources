package Questions.Graph;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
https://leetcode.com/problems/critical-connections-in-a-network/description/
 There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
Time complexity: O(V+E)
Space complexity: O(V+E)
 */
public class CriticalConnections {
    private int time = 0; // used to store discovery times of visited vertices
    private List<List<Integer>> graph;
    private List<List<Integer>> result;

    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        graph = new ArrayList<>();
        result = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        // Build the graph
        for (List<Integer> connection : connections) {
            int u = connection.get(0);
            int v = connection.get(1);
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        // Initialize discovery and low arrays
        int[] discovery = new int[n];
        int[] low = new int[n];
        Arrays.fill(discovery, -1); // -1 means not visited

        // Start DFS from node 0 (could be any node)
        dfs(0, -1, discovery, low);

        return result;
    }

    private void dfs(int u, int parent, int[] discovery, int[] low) {
        discovery[u] = low[u] = ++time; // Initialize discovery time and low value
        for (int v : graph.get(u)) {
            if (v == parent)
                continue; // If parent vertex, ignore

            if (discovery[v] == -1) { // If v is not visited
                dfs(v, u, discovery, low);

                // Check if the subtree rooted at v has a connection back to one of u's
                // ancestors
                low[u] = Math.min(low[u], low[v]);

                // If the lowest vertex reachable from subtree under v is below u in DFS tree,
                // then u-v is a bridge
                if (low[v] > discovery[u]) {
                    result.add(Arrays.asList(u, v));
                }
            } else { // Update low value of u for parent function calls
                low[u] = Math.min(low[u], discovery[v]);
            }
        }
    }

    public static void main(String[] args) {
        int n = 4;
        List<List<Integer>> connections = new ArrayList<>();
        connections.add(Arrays.asList(0, 1));
        connections.add(Arrays.asList(1, 2));
        connections.add(Arrays.asList(2, 0));
        connections.add(Arrays.asList(1, 3));
        CriticalConnections criticalConnections = new CriticalConnections();
        List<List<Integer>> result = criticalConnections.criticalConnections(n, connections);
        System.out.println("Critical Connections: " + result);
    }
}