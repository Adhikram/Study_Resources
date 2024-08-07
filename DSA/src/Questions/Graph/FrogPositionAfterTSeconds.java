package Questions.Graph;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
/*
https://leetcode.com/problems/frog-position-after-t-seconds/description/
 Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices, it jumps randomly to one of them with the same probability. Otherwise, when the frog can not jump to any unvisited vertex, it jumps forever on the same vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.

Return the probability that after t seconds the frog is on the vertex target. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:


Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
Output: 0.16666666666666666 
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after second 1 and then jumping with 1/2 probability to vertex 4 after second 2. Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666. 
Example 2:


Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
Output: 0.3333333333333333
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1. 
 

Constraints:

1 <= n <= 100
edges.length == n - 1
edges[i].length == 2
1 <= ai, bi <= n
1 <= t <= 50
1 <= target <= n
Time complexity: O(n)
Space complexity: O(n)
 */
public class FrogPositionAfterTSeconds {
    List<Integer>[] g;

    public double frogPosition(int n, int[][] edges, int t, int target) {
        if (n == 1) {
            return 1.0;
        }
        g = new ArrayList[n + 1];
        boolean[] visited = new boolean[n + 1];
        Arrays.setAll(g, k -> new ArrayList<>());
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        return helper(1, t, target, visited);
    }

    public double helper(int node, int t, int target, boolean[] visited) {
        if (node != 1 && g[node].size() == 1 || t == 0) {
            if (node == target) {
                return 1.0;
            }
            return 0.0;
        }
        visited[node] = true;
        double res = 0.0;
        for (int next : g[node]) {
            if (visited[next]) {
                continue;
            }
            res += helper(next, t - 1, target, visited);
            if (res > 0) {
                if (node != 1) {
                    return res / (g[node].size() - 1);
                } else {
                    return res / g[node].size();
                }
            }
        }
        return 0.0;
    }
}
