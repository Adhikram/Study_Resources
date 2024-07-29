package Questions.Array;

import java.util.HashSet;
import java.util.Set;

/*
https://leetcode.com/problems/minimum-area-rectangle/description
You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes.
If there is not any such rectangle, return 0.


Example 1:


Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:


Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

Constraints:

1 <= points.length <= 500
points[i].length == 2
0 <= xi, yi <= 4 * 104
All the given points are unique.
 */
public class MinimumAreaRect {
    public static double minAreaFreeRect(int[][] points) {
        int n = points.length;
        double area = Double.MAX_VALUE;
        Set<String> pointSet = new HashSet<>();
        for (int[] point : points) {
            pointSet.add(point[0] + "," + point[1]);
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    // Check if the points are diagonals of a rectangle
                    int dx1 = points[k][0] - points[i][0];
                    int dy1 = points[k][1] - points[i][1];
                    int dx2 = points[j][0] - points[i][0];
                    int dy2 = points[j][1] - points[i][1];
                    // Dot product of the edges are 0 when perpendicular
                    /*
                     * If the dot product of the two edges is 0, then the two edges are
                     * perpendicular to each other.
                     */
                    if (dy1 * dy2 + dx1 * dx2 == 0) {
                        int xl = points[j][0] + dx1;
                        int yl = points[j][1] + dy1;
                        if (pointSet.contains(xl + "," + yl)) {
                            area = Math.min(area, Math.sqrt(dx1 * dx1 + dy1 * dy1) * Math.sqrt(dx2 * dx2 + dy2 * dy2));
                        }
                    }
                }
            }
        }
        return area == Double.MAX_VALUE ? 0 : area;
    }


    public static void main(String[] args) {
        int[][] points = { { 1, 1 }, { 1, 3 }, { 3, 1 }, { 3, 3 }, { 2, 2 } };
        System.out.println(minAreaFreeRect(points));
    }
}
