package Questions.Graph.DisjointSetMST;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class MostStones {
    public int removeStones(int[][] stones) {
        int count = 0;

        Arrays.sort(stones, (a, b) -> {
            if (a[0] == b[0]) {
                return a[1] - b[1];
            }
            return a[0] - b[0];
        });
        HashSet<String> seen = new HashSet<>();
        for (int[] stone : stones) {
            System.out.println("Stone: " + stone[0] + " " + stone[1]);
            boolean row = seen.add("A stone in row " + stone[0]);
            boolean column = seen.add("A stone in column " + stone[1]);
            if (!row || !column) {
                count++;
            }
            seen.forEach(System.out::println);
            System.out.println("Count: " + count);
        }
        return count;
    }

    // Method to calculate the maximum number of stones that can be removed
    static int maxRemove(int[][] stones, int n) {
        // Find maximum row and column indices among the stones
        int maxRow = Arrays.stream(stones).mapToInt(stone -> stone[0]).max().getAsInt();
        int maxCol = Arrays.stream(stones).mapToInt(stone -> stone[1]).max().getAsInt();
        // for (int i = 0; i < n; i++) {
        //     maxRow = Math.max(maxRow, stones[i][0]);
        //     maxCol = Math.max(maxCol, stones[i][1]);
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

        // Count the number of unique sets (represents maximum removable stones)
        int cnt = 0;
        for (Map.Entry<Integer, Integer> it : stoneNodes.entrySet()) {
            if (ds.findUPar(it.getKey()) == it.getKey()) {
                cnt++;
            }
        }

        // Return the maximum number of stones that can be removed
        return n - cnt;
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
    }
}
