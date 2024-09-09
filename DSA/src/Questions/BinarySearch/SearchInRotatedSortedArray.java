package Questions.BinarySearch;
/*
 https://leetcode.com/problems/search-in-rotated-sorted-array/

start = 0, end = n - 1
    mid = (start + end) / 2
    if nums[mid] == target, return mid
    We need to find the sorted half because BS can only runs on the Sorted part
    if nums[mid] >= nums[start]:
        // Left part is sorted
        if nums[start] <= target && target < nums[mid]:
            // If target lies between the sorted range
            end = mid - 1
        else:
            start = mid + 1
    else:
        // Right part is sorted
        if nums[mid] < target && target <= nums[end]:
            // If target lies between the sorted range
            start = mid + 1
        else:
            end = mid - 1

 */
public class SearchInRotatedSortedArray {
    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        while (start <= end) {
            int mid = (start + end) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            // We need to find the sorted half because BS can only runs on the Sorted part
            if (nums[mid] >= nums[start]) {
                // Left part is sorted
                if (nums[start] <= target && target < nums[mid]) {
                    // If target lies between the sorted range
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            } else {
                // Right part is sorted
                if (nums[mid] < target && target <= nums[end]) {
                    // If target lies between the sorted range
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }

        }
        return -1;
    }
    public static void main(String[] args) {
        SearchInRotatedSortedArray searchInRotatedSortedArray = new SearchInRotatedSortedArray();
        int[] nums = {4,5,6,7,0,1,2};
        int target = 0;
        int result = searchInRotatedSortedArray.search(nums, target);
        System.out.println("Index of the target: " + result);
    }
}
