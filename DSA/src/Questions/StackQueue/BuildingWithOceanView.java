package Questions.StackQueue;
import java.util.Arrays;

/*
https://leetcode.com/problems/buildings-with-an-ocean-view/description/
 There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.


Example 1:

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
Example 2:

Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.
Example 3:

Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.
Time Complexity: O(n)
Space Complexity: O(1)
 */
public class BuildingWithOceanView {
    public int[] findBuildings(int[] heights) {
        // List<Integer> result = new ArrayList<>();
        // int n = heights.length;
        // int maxHeight = 0;

        // // Traverse from right to left
        // for (int i = n - 1; i >= 0; i--) {
        // if (heights[i] > maxHeight) {
        // result.add(i);
        // maxHeight = heights[i];
        // }
        // }

        // // Reverse to get the indices in increasing order
        // Collections.reverse(result);
        // return result.stream().mapToInt(i -> i).toArray();
        int len = heights.length;

        int idx = len - 1;
        int max = heights[idx];
        heights[idx] = idx;
        idx--;

        for (int i = len - 2; i >= 0; i--) {
            if (heights[i] > max) {
                max = heights[i];
                heights[idx] = i;
                idx--;
            }
        }

        return Arrays.copyOfRange(heights, idx + 1, len);
    }

    public static void main(String[] args) {
        BuildingWithOceanView buildingWithOceanView = new BuildingWithOceanView();
        System.out.println(Arrays.toString(buildingWithOceanView.findBuildings(new int[] { 4, 2, 3, 1 })));
        System.out.println(Arrays.toString(buildingWithOceanView.findBuildings(new int[] { 4, 3, 2, 1 })));
        System.out.println(Arrays.toString(buildingWithOceanView.findBuildings(new int[] { 1, 3, 2, 4 })));
    }
}
