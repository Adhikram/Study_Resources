package Questions.Array;

import java.util.ArrayList;
import java.util.List;

public class RectangleIntersections {
    static class Rectangle {
        int[] bottomLeft;
        int[] topRight;

        Rectangle(int[] bottomLeft, int[] topRight) {
            this.bottomLeft = bottomLeft;
            this.topRight = topRight;
        }
    }

    public static int countIntersectionPoints(int[] linesX, int[] linesY, List<Rectangle> rectangles) {
        int intersectionCount = 0;

        // Iterate through lines parallel to X-axis
        for (int lineX : linesX) {
            for (Rectangle rectangle : rectangles) {
                if (rectangle.bottomLeft[1] <= lineX && lineX <= rectangle.topRight[1]) {
                    intersectionCount++;
                }
            }
        }

        // Iterate through lines parallel to Y-axis
        for (int lineY : linesY) {
            for (Rectangle rectangle : rectangles) {
                if (rectangle.bottomLeft[0] <= lineY && lineY <= rectangle.topRight[0]) {
                    intersectionCount++;
                }
            }
        }

        return intersectionCount;
    }

    public static void main(String[] args) {
        int[] linesX = {1, 2, 4, 19};
        int[] linesY = {2, 5, 9};
        List<Rectangle> rectangles = new ArrayList<>();
        rectangles.add(new Rectangle(new int[]{1, 3}, new int[]{3, 6}));

        // Count intersection points
        int totalIntersectionPoints = countIntersectionPoints(linesX, linesY, rectangles);
        System.out.println("Total intersection points: " + totalIntersectionPoints);
    }

}
