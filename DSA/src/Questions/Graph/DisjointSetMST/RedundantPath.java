package Questions.Graph.DisjointSetMST;

import java.util.HashMap;

/*
https://leetcode.com/problems/redundant-connection/description/
 In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.

Time complexity: O(n)
Space complexity: O(n)
 */
public class RedundantPath {

    public int findParent(HashMap<Integer, Integer> parents, int elem) {
        if (parents.getOrDefault(elem, -1) == -1) {
            return elem;
        }
        return findParent(parents, parents.get(elem));
    }

    public int[] findRedundantConnection(int[][] edges) {
        HashMap<Integer, Integer> parents = new HashMap();

        for (int[] edge : edges) {
            int from = findParent(parents, edge[1]);
            int to = findParent(parents, edge[0]);
            if (from == to) {
                return edge;
            }

            parents.put(from, to);
        }
        return new int[0];
    }

    public static void main(String[] args) {
        RedundantPath redundantPath = new RedundantPath();
        int[][] edges = { { 1, 2 }, { 1, 3 }, { 2, 3 } };
        int[] result = redundantPath.findRedundantConnection(edges);
        System.out.println("Redundant Connection: " + result[0] + " " + result[1]);
    }
}
