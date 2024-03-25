package Questions.BinarySearch;

public class SearchInRotatedSortedArray2 {
    public static int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        while (start <= end) {
            int mid = (start + end) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            // Edge case:
            if (nums[start] == nums[mid] && nums[mid] == nums[end]) {
                start = start + 1;
                end = end - 1;
                continue;
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
    /*
     * Time Complexity: O(logN) for the best and average case. O(N/2) for the worst
     * case. Here, N = size of the given array.
     */
    public static void main(String[] args) {
        int[] nums = { 2, 5, 6, 0, 0, 1, 2 };
        int target = 0;
        int result = search(nums, target);
        System.out.println("Index of the target: " + result);
    }
}
