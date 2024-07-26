package Questions.Graph;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

/*
https://leetcode.com/problems/flower-planting-with-no-adjacent/description/
 You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional path between garden xi to garden yi. In each garden, you want to plant one of 4 types of flowers.

All gardens have at most 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.

 

Example 1:

Input: n = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Explanation:
Gardens 1 and 2 have different types.
Gardens 2 and 3 have different types.
Gardens 3 and 1 have different types.
Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].
Example 2:

Input: n = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 

Constraints:

1 <= n <= 104
0 <= paths.length <= 2 * 104
paths[i].length == 2
1 <= xi, yi <= n
xi != yi
Every garden has at most 3 paths coming into or leaving it.
Time complexity: O(n)
Space complexity: O(n)
 */
public class FlowerPlanting {
    class Garden {
        public final int[] FLOWER_TYPES = { 1, 2, 3, 4 };
        int flowerType;
        List<Garden> connectedGardens;

        public Garden() {
            flowerType = -1;
            connectedGardens = new ArrayList<Garden>();
        }

        // This method would iterate through connected garden and add the flower type
        // that is taken by connected garden into HashSet. Now, we know which flower is
        // taken, we can assign proper flower type to the current garden that we are in!
        public void setUniqueFlowerType() {
            HashSet<Integer> takenByConnectedGarden = new HashSet();
            for (Garden garden : connectedGardens) {
                if (garden.flowerType != -1) {
                    takenByConnectedGarden.add(garden.flowerType);
                }
            }
            // This method would iterate through connected garden and add the flower type
            // that is taken by connected garden into HashSet. Now, we know which flower is
            // taken, we can assign proper flower type to the current garden that we are in!
            for (int flowerType : FLOWER_TYPES) {
                if (!takenByConnectedGarden.contains(flowerType)) {
                    this.flowerType = flowerType;
                    break;
                }
            }
        }
    }

    public int[] gardenNoAdj(int N, int[][] paths) {
        /*
         * instansiate N garden
         * connect the path
         * setUniqueFlowerType for each node
         * return int[] array of each garden's flower type
         */

        Garden[] graph = new Garden[N];// array of gardens
        for (int i = 0; i < N; i++) {
            graph[i] = new Garden();
        }

        // connect path
        for (int[] path : paths) {
            // -1 because of 0-based index
            int p1 = path[0] - 1;
            int p2 = path[1] - 1;
            Garden garden1 = graph[p1];
            Garden garden2 = graph[p2];
            // when garden1's neighbor is garden2, then garden2's neighbor should also be
            // garden1
            garden1.connectedGardens.add(garden2);
            garden2.connectedGardens.add(garden1);
        }

        int idx = 0;
        int[] res = new int[N];
        for (Garden garden : graph) {
            garden.setUniqueFlowerType();
            res[idx++] = garden.flowerType;
        }

        return res;
    }
}
