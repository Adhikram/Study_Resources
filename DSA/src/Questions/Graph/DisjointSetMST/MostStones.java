package Questions.Graph.DisjointSetMST;

import java.util.Arrays;
import java.util.HashMap;

/*
 On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.


Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.

Constraints:

1 <= stones.length <= 1000
0 <= xi, yi <= 104
No two stones are at the same coordinate point.
Time Complexity: O(N)
Space Complexity: O(N)
 */
public class MostStones {
    // Method to calculate the maximum number of stones that can be removed
    static int maxRemove(int[][] stones, int n) {
        // Find maximum row and column indices among the stones
        int maxRow = Arrays.stream(stones).mapToInt(stone -> stone[0]).max().getAsInt();
        int maxCol = Arrays.stream(stones).mapToInt(stone -> stone[1]).max().getAsInt();
        // for (int i = 0; i < n; i++) {
        // maxRow = Math.max(maxRow, stones[i][0]);
        // maxCol = Math.max(maxCol, stones[i][1]);
        // }

        // Create a DisjointSet with a size enough to accommodate both rows and columns
        DisjointSet ds = new DisjointSet(maxRow + maxCol + 1);

        // HashMap to store stone nodes
        HashMap<Integer, Integer> stoneNodes = new HashMap<>();

        // Process stones
        for (int i = 0; i < n; i++) {
            int nodeRow = stones[i][0];
            int nodeCol = stones[i][1] + maxRow + 1; // Adding maxRow + 1 to differentiate column nodes
            ds.unionBySize(nodeRow, nodeCol); // Union rows and columns
            stoneNodes.put(nodeRow, 1); // Mark row node as seen
            stoneNodes.put(nodeCol, 1); // Mark column node as seen
        }

        // Return the maximum number of stones that can be removed
        return n - ds.components;
    }

    public int numOfIslands = 0;

    public int removeStones(int[][] stones) {
        int[] parent = new int[20003];
        for (int[] stone : stones) {
            unionSets(stone[0] + 1, stone[1] + 10002, parent);
        }
        return stones.length - numOfIslands;
    }

    public void unionSets(int a, int b, int[] parent) {
        int parA = findParent(a, parent), parB = findParent(b, parent);
        if (parA != parB) {
            parent[parB] = parA;
            numOfIslands--;
        }
        return;
    }

    public int findParent(int node, int[] parent) {
        if (parent[node] == 0) {
            parent[node] = node;
            numOfIslands++;
        }
        if (parent[node] == node) {
            return node;
        }
        int par = findParent(parent[node], parent);
        parent[node] = par;
        return par;
    }

    public static void main(String[] args) {
        int n = 6;
        int[][] stones = {
                { 0, 0 }, { 0, 2 },
                { 1, 3 }, { 3, 1 },
                { 3, 2 }, { 4, 3 }
        };

        int ans = maxRemove(stones, n);

        System.out.println("The maximum number of stones we can remove is: " + ans);
        System.out.println("The maximum number of stones we can remove is: " + new MostStones().removeStones(stones));
    }
}
