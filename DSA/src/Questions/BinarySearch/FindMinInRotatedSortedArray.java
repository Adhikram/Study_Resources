package Questions.BinarySearch;

/*
 https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
 Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [1,3,5]
Output: 1
Example 2:

Input: nums = [2,2,2,0,1]
Output: 0
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.
 Time Complexity: O(logN)
 Space Complexity: O(1)
 */
public class FindMinInRotatedSortedArray {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = (right + left) >> 1;

            if (nums[mid] < nums[right]) {
                right = mid;
            } else if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right--; // nums[mid] == nums[right], reduce the search space
            }
        }

        return nums[left];
    }

    public int findMax(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = (right + left) >> 1;

            if (nums[mid] < nums[right]) {
                right = mid - 1;
            } else if (nums[mid] > nums[right]) {
                left = mid;
            } else {
                right--; // nums[mid] == nums[right], reduce the search space
            }
        }

        return nums[left];
    }

    public static void main(String[] args) {
        FindMinInRotatedSortedArray findMinInRotatedSortedArray = new FindMinInRotatedSortedArray();
        int[] nums = { 3, 4, 5, 6, 1, 2 };
        System.out.println(findMinInRotatedSortedArray.findMin(nums)); // 1
        System.out.println(findMinInRotatedSortedArray.findMax(nums)); // 5
    }
}
