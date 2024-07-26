package Questions.Graph;

/*
https://leetcode.com/problems/sum-of-distances-in-tree/description/
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

Example 1:
Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

Example 2:
Input: n = 1, edges = []
Output: [0]

Example 3:
Input: n = 2, edges = [[1,0]]
Output: [1,1]

Constraints:
1 <= n <= 3 * 10^4
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
The given input represents a valid tree
Time complexity: O(n)
Space complexity: O(n)
*/

public class SumOfDistanceTree {
    int[][] graph; // Adjacency list representation of the tree
    int[] count;   // Count of nodes in the subtree rooted at each node
    int[] res;     // Result array to store the sum of distances for each node
    int N;         // Number of nodes in the tree

    public int[] sumOfDistancesInTree(int N, int[][] edges) {
        this.N = N;
        this.res = new int[N];
        this.graph = new int[N][];
        this.count = new int[N];

        // Initialize the count array to store the degree of each node
        for (int[] e : edges) {
            ++count[e[0]];
            ++count[e[1]];
        }

        // Initialize the adjacency list for each node
        for (int i = 0; i < N; i++) {
            graph[i] = new int[count[i]];
        }

        // Fill the adjacency list with the edges
        for (int[] e : edges) {
            graph[e[0]][--count[e[0]]] = e[1];
            graph[e[1]][--count[e[1]]] = e[0];
        }

        // First DFS to calculate the count of nodes and initial result for each node
        dfs1(0, -1);

        // Second DFS to update the result for each node based on its parent's result
        dfs2(0, -1);

        return res;
    }

    // First DFS to calculate the count of nodes in the subtree and initial result for each node
    public void dfs1(int cur, int parent) {
        count[cur] = 1; // Each node counts itself
        for (int child : graph[cur]) {
            if (child != parent) {
                dfs1(child, cur);
                count[cur] += count[child]; // Add the count of child nodes
                res[cur] += res[child] + count[child]; // Add the distances from the child nodes
            }
        }
    }

    // Second DFS to update the result for each node based on its parent's result
    public void dfs2(int cur, int parent) {
        for (int child : graph[cur]) {
            if (child != parent) {
                res[child] = res[cur] + N - 2 * count[child]; // Update the result for the child node
                dfs2(child, cur);
            }
        }
    }

    public static void main(String[] args) {
        int n = 6;
        int[][] edges = { { 0, 1 }, { 0, 2 }, { 2, 3 }, { 2, 4 }, { 2, 5 } };
        SumOfDistanceTree sumOfDistanceTree = new SumOfDistanceTree();
        int[] result = sumOfDistanceTree.sumOfDistancesInTree(n, edges);
        for (int i : result) {
            System.out.print(i + " ");
        }
    }
}