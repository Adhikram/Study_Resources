package Questions.BinarySearch;

import java.util.ArrayList;
import java.util.Arrays;
/*
 https://leetcode.com/problems/find-peak-element/description/

If arr[mid] is greater than both its neighbors (or if it is at the boundary and greater than its single neighbor),
 it is a peak element. 
 if ((mid == 0 || arr.get(mid - 1) < arr.get(mid)) && (mid == n - 1 || arr.get(mid) > arr.get(mid + 1))) {
                return mid;
            }

If arr[mid] is less than its left neighbor, move the search range to the left half.

If arr[mid] is less than its right neighbor, move the search range to the right half.

 */
public class PeakElement {

    public static int findPeakElement(ArrayList<Integer> arr) {
        int n = arr.size(); // Size of the array

        int low = 0, high = n - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;

            // Check if arr[mid] is the peak:
            if ((mid == 0 || arr.get(mid - 1) < arr.get(mid)) && (mid == n - 1 || arr.get(mid) > arr.get(mid + 1))) {
                return mid;
            }

            // If we are in the left and arr[mid] is decreasing, move right:
            if (mid > 0 && arr.get(mid) < arr.get(mid - 1)) {
                high = mid - 1;
            } else {
                // If we are in the right or arr[mid] is increasing, move left:
                low = mid + 1;
            }
        }
        // If no peak is found, return -1:
        return -1;
    }

    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 5, 1));
        int ans = findPeakElement(arr);
        if (ans != -1) {
            System.out.println("The peak is at index: " + ans);
        } else {
            System.out.println("No peak found in the array.");
        }
    }
}
