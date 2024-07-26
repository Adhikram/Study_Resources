package Questions.Graph;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
https://leetcode.com/problems/find-if-path-exists-in-graph/description/
 There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 

Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:


Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
 

Constraints:

1 <= n <= 2 * 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
There are no duplicate edges.
There are no self edges.
Time complexity: O(n)
Space complexity: O(n)
 */
public class FindPathIfExists {
    public boolean dfs(int source, int destination, boolean[] visited, List<Integer>[] adj) {
        if (source == destination) {
            return true;
        }
        visited[source] = true;
        for (int neighbor : adj[source]) {
            if (!visited[neighbor] && source != neighbor && dfs(neighbor, destination, visited, adj)) {
                return true;
            }
        }
        return false;

    }

    public boolean validPath(int n, int[][] edges, int source, int destination) {
        boolean[] visited = new boolean[n];
        List<Integer>[] adj = new List[n];
        Arrays.setAll(adj, k -> new ArrayList());
        for (int[] edge : edges) {
            adj[edge[0]].add(edge[1]);
            adj[edge[1]].add(edge[0]);
        }
        return dfs(source, destination, visited, adj);
    }

    public static void main(String[] args) {
        FindPathIfExists findPathIfExists = new FindPathIfExists();
        int n = 3;
        int[][] edges = { { 0, 1 }, { 0, 2 }, { 1, 2 } };
        int source = 0;
        int destination = 2;
        System.out.println(findPathIfExists.validPath(n, edges, source, destination)); // true

        n = 3;
        edges = new int[][] { { 0, 1 }, { 0, 2 }, { 1, 2 } };
        source = 0;
        destination = 3;
        System.out.println(findPathIfExists.validPath(n, edges, source, destination)); // false
    }
}
