package Questions.Graph.DisjointSetMST;

/*
https://leetcode.com/problems/redundant-connection-ii/description/
 In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed edge connecting nodes ui and vi, where ui is a parent of child vi.

Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
Output: [4,1]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
 */
public class RedundantPath2 {
    // Union-Find with path compression
    private int findParent(int[] parent, int x) {
        if (parent[x] != x) {
            parent[x] = findParent(parent, parent[x]);
        }
        return parent[x];
    }

    public int[] findRedundantDirectedConnection(int[][] edges) {
        int n = edges.length;
        int[] parent = new int[n + 1];
        int[] candidate1 = null;
        int[] candidate2 = null;

        // Initialize each node's parent to itself
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        // Step 1: Check whether there is a node with two parents
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            if (parent[v] != v) {
                // v has two parents
                candidate1 = new int[] { parent[v], v };
                candidate2 = new int[] { u, v };
                edge[1] = 0; // Temporarily remove the current edge
            } else {
                parent[v] = u;
            }
        }

        // Reset parent array for union-find
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        // Step 2: Use union-find to detect cycles
        for (int[] edge : edges) {
            if (edge[1] == 0)
                continue; // Skip the temporarily removed edge
            int u = edge[0];
            int v = edge[1];
            int pu = findParent(parent, u);
            int pv = findParent(parent, v);
            if (pu == pv) {
                if (candidate1 == null) {
                    return edge; // Case 1: No two parents scenario, return the edge causing cycle
                }
                // Case 2: There are two parents, return the first edge causing the cycle
                return candidate1;
            }
            parent[pv] = pu;
        }

        // Case 3: No cycle found, return the second edge causing two parents scenario
        return candidate2;
    }

    public static void main(String[] args) {
        RedundantPath2 redundantPath = new RedundantPath2();
        int[][] edges = { { 1, 2 }, { 1, 3 }, { 2, 3 } };
        int[] result = redundantPath.findRedundantDirectedConnection(edges);
        System.out.println("Redundant Connection: " + result[0] + " " + result[1]);
    }

}
