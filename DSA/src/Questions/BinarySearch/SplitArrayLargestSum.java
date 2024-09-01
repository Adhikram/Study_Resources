package Questions.BinarySearch;

import java.util.Arrays;
/*
 https://leetcode.com/problems/split-array-largest-sum/description/
 Time Complexity: O(N * log(sum(nums))) where N is the length of the nums array. This is because we perform binary search on the range [max(nums), sum(nums)] and for each mid-point, we check the feasibility in O(N).
Space Complexity: O(1) as we use a constant amount of extra space.

 */
public class SplitArrayLargestSum {

    // Method to count the number of students needed to read the given number of
    // pages
    public static int countStudents(int[] nums, int pages) {
        int students = 1;

        long sumPages = 0;
        // Loop through the array and add the pages read by each student
        for (int i = 0; i < nums.length; i++) {
            if (sumPages + nums[i] <= pages) {
                sumPages += nums[i];
            } else {
                // If the current student cannot read more pages, increment the student count
                // and assign the current pages to the new student
                students++;
                sumPages = nums[i];
            }
        }
        return students;
    }

    // Method to split the array into m sub-arrays such that the maximum sum of the
    // sub-arrays is minimized
    public static int splitArray(int[] nums, int m) {
        int low = 0, high = 0;
        // Calculate the lower and upper bounds for binary search
        // for (int num : nums) {
        //     low = Math.max(low, num); // The maximum element in the array
        //     high += num; // The sum of all elements in the array
        // }
        low = Arrays.stream(nums).max().getAsInt();
        high = Arrays.stream(nums).sum();
        System.out.println("Low: " + low + " High: " + high);
        // Apply binary search
        while (low <= high) {
            int mid = (low + high) / 2;
            int students = countStudents(nums, mid);
            // If the number of students needed is less than or equal to m, search in the
            // lower half
            if (students <= m) {
                high = mid - 1;
            } else {
                // Else, search in the upper half
                low = mid + 1;
            }
        }
        return low;
    }

    /*
     * Time Complexity: O(N * log(sum of array elements))
     */

    // Main method
    public static void main(String[] args) {
        int[] nums = { 10, 20, 30, 40 };
        int m = 2;
        // Find the minimum possible maximum sum of m sub-arrays
        System.out.println(splitArray(nums, m));
    }
}