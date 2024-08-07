package Questions.Graph.DisjointSetMST;

/*
 * https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/
 Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 

Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 

 

Constraints:

1 <= n <= 105
1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
edges[i].length == 3
1 <= typei <= 3
1 <= ui < vi <= n
All tuples (typei, ui, vi) are distinct.
Time complexity: O(ElogE)
Space complexity: O(E)
 */
public class MaximumEdgesToRemove {
    public int maxNumEdgesToRemove(int n, int[][] edges) {
        UnionFind alice = new UnionFind(n);
        UnionFind bob = new UnionFind(n);

        int edgesRequired = 0;
        for (int[] edge : edges) {
            if (edge[0] == 3) {
                edgesRequired += (alice.preformUnion(edge[1], edge[2]) | bob.preformUnion(edge[1], edge[2]));
            }
        }

        for (int[] edge : edges) {
            if (edge[0] == 2) {
                edgesRequired += bob.preformUnion(edge[1], edge[2]);
            } else if (edge[0] == 1) {
                edgesRequired += alice.preformUnion(edge[1], edge[2]);
            }
        }

        if (alice.isConnected() && bob.isConnected()) {
            return edges.length - edgesRequired;
        }

        return -1;

    }

    class UnionFind {

        int[] representative;
        int[] componentSize;
        int components;

        UnionFind(int n) {
            components = n;
            representative = new int[n + 1];
            componentSize = new int[n + 1];

            for (int i = 0; i <= n; i++) {
                representative[i] = i;
                componentSize[i] = i;
            }
        }

        int findRepresentative(int x) {
            if (representative[x] == x) {
                return x;
            }

            return representative[x] = findRepresentative(representative[x]);
        }

        int preformUnion(int x, int y) {
            x = findRepresentative(x);
            y = findRepresentative(y);

            if (x == y) {
                return 0;
            }

            if (componentSize[x] > componentSize[y]) {
                componentSize[x] += componentSize[y];
                representative[y] = x;
            } else {
                componentSize[y] += componentSize[x];
                representative[x] = y;
            }

            components--;
            return 1;
        }

        boolean isConnected() {
            return components == 1;
        }
    }

    public static void main(String[] args) {
        int n = 4;
        int[][] edges = { { 3, 1, 2 }, { 3, 2, 3 }, { 1, 1, 3 }, { 1, 2, 4 }, { 1, 1, 2 }, { 2, 3, 4 } };
        MaximumEdgesToRemove maximumEdgesToRemove = new MaximumEdgesToRemove();
        System.out.println(maximumEdgesToRemove.maxNumEdgesToRemove(n, edges));
    }
}
