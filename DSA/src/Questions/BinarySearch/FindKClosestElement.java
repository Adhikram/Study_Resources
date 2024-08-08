package Questions.BinarySearch;

import java.util.ArrayList;
import java.util.List;
/*
https://leetcode.com/problems/find-k-closest-elements/description/
 Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
Time Complexity: O(log(N) + k)
Space Complexity: O(1)
 */
public class FindKClosestElement {
public static List<Integer> findClosestElements(int[] arr, int k, int x) {
        int left = 0, right = arr.length - k;

        // Binary search to find the start of the window
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (x - arr[mid] > arr[mid + k] - x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int i = left; i < left + k; i++) {
            result.add(arr[i]);
        }

        // Since the elements are already in the correct order
        return result;
    }
    public static void main(String[] args) {
        // Example usage
        int[] arr = {1, 2, 3, 4, 5};
        int k = 4, x = 3;
        System.out.println(findClosestElements(arr, k, x)); // Expected output: [1, 2, 3, 4]
    }
}
