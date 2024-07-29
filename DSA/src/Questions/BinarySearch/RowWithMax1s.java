package Questions.BinarySearch;

import java.util.ArrayList;
import java.util.Arrays;

public class RowWithMax1s {
    // Method to find the first occurrence of x in a sorted array
    public static int lowerBound(ArrayList<Integer> arr, int n, int x) {
        int low = 0, high = n - 1;

        while (low <= high) {
            int mid = (low + high) >> 1;
            // If the current element is greater than or equal to x, update ans and look for
            // smaller index on the left
            if (arr.get(mid) >= x) {
                high = mid - 1;
            }
            // If the current element is less than x, look on the right
            else {
                low = mid + 1;
            }
        }
        // Return the first occurrence of x
        return high + 1;
    }

    // Method to find the row with the maximum number of 1's in a binary matrix
    public static int rowWithMax1s(ArrayList<ArrayList<Integer>> matrix, int n, int m) {
        int cnt_max = 0;
        int index = -1;

        // Traverse the rows
        for (int i = 0; i < n; i++) {
            // Get the number of 1's in the current row
            int cnt_ones = m - lowerBound(matrix.get(i), m, 1);
            // If the number of 1's in the current row is greater than the maximum so far,
            // update cnt_max and index
            if (cnt_ones > cnt_max) {
                cnt_max = cnt_ones;
                index = i;
            }
        }
        // Return the index of the row with the maximum number of 1's
        return index;
    }

    // Main method
    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> matrix = new ArrayList<>();
        matrix.add(new ArrayList<>(Arrays.asList(0, 1, 1)));
        matrix.add(new ArrayList<>(Arrays.asList(0, 0, 1)));
        matrix.add(new ArrayList<>(Arrays.asList(0, 1, 1)));
        matrix.add(new ArrayList<>(Arrays.asList(0, 0, 0)));
        matrix.add(new ArrayList<>(Arrays.asList(0, 0, 0)));

        int n = 5, m = 3;
        // Find the row with the maximum number of 1's in the binary matrix
        System.out.println("The row with the maximum number of 1's is: " +
                rowWithMax1s(matrix, n, m));
    }
}