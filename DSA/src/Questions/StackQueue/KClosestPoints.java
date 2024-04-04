package Questions.StackQueue;

import java.util.PriorityQueue;

public class KClosestPoints {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> q = new PriorityQueue<int[]>((a, b) -> {
            double distance_a = Math.sqrt((a[0] * a[0]) + (a[1] * a[1]));
            double distance_b = Math.sqrt((b[0] * b[0]) + (b[1] * b[1]));
            return Double.compare(distance_b, distance_a);
        });

        for (int i = 0; i < points.length; i++) {
            int[] cur = points[i];
            q.add(cur);
            if (q.size() > k) {
                q.poll();
            }
        }

        int[][] result = new int[k][2];

        while (k-- > 0) {
            int[] cur = q.poll();
            result[k] = cur;
        }
        return result;
    }

    public static void main(String[] args) {
        KClosestPoints kClosestPoints = new KClosestPoints();
        int[][] points = { { 1, 3 }, { -2, 2 } };
        int k = 1;
        int[][] result = kClosestPoints.kClosest(points, k);
        for (int[] point : result) {
            System.out.println(point[0] + " " + point[1]);
        }
    }
}
