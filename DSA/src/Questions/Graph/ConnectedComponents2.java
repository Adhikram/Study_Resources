package Questions.Graph;

import java.util.ArrayList;
import java.util.List;

/*
    https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
    You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

    Return the number of connected components in the graph.

    

    Example 1:


    Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2
    Example 2:


    Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    Output: 1
    

    Constraints:

    1 <= n <= 2000
    1 <= edges.length <= 5000
    edges[i].length == 2
    0 <= ai <= bi < n
    ai != bi
    There are no repeated edges.
    Union-Find Approach:

Time Complexity: O(n + m log n) where n is the number of nodes and m is the number of edges. This is because each union and find operation is nearly constant time due to path compression.
Space Complexity: O(n) for storing the parent array.
DFS Approach:

Time Complexity: O(n + m) where n is the number of nodes and m is the number of edges. This is because each node and edge is processed once.
Space Complexity: O(n + m) for storing the adjacency list and the recursion stack in the worst case.

 */
public class ConnectedComponents2 {
    public int countComponentsUF(int n, int[][] edges) {
        int[] parent = new int[n];
        for (int i = 0; i < n; i++)
            parent[i] = i;
        int components = n;
        for (int[] e : edges) {
            int p1 = findParent(parent, e[0]);
            int p2 = findParent(parent, e[1]);
            if (p1 != p2) {
                parent[p1] = p2; // Union 2 component
                components--;
            }
        }
        return components;
    }

    private int findParent(int[] parent, int i) {
        if (i == parent[i])
            return i;
        return parent[i] = findParent(parent, parent[i]); // Path compression
    }

    /*
     * Time: O(n+mlogn), where m is the number of connections, n is the number of
     * nodes.
     * By doing Path Compression, it has been proven to achieve in O(logN) in each
     * operations. Read more under
     * https://cp-algorithms.com/data_structures/disjoint_set_union.html#toc-tgt-2
     * Space: O(n)
     */
    public int countComponents(int n, int[][] edges) {
        List<Integer>[] graph = new List[n];
        for (int i = 0; i < n; i++)
            graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        int components = 0;
        boolean[] visited = new boolean[n];
        for (int v = 0; v < n; v++)
            components += dfs(v, graph, visited);
        return components;
    }

    int dfs(int u, List<Integer>[] graph, boolean[] visited) {
        if (visited[u])
            return 0;
        visited[u] = true;
        for (int v : graph[u])
            dfs(v, graph, visited);
        return 1;
    }

    /*
     * Time: O(n+m), where m is the number of connections, n is the number of nodes.
     * Space: O(n+m),
     */
    public static void main(String[] args) {
        int n = 5;
        int[][] edges = { { 0, 1 }, { 1, 2 }, { 3, 4 } };
        ConnectedComponents2 connectedComponents = new ConnectedComponents2();
        System.out.println(connectedComponents.countComponents(n, edges));
    }
}
