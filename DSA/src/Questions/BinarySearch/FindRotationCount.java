package Questions.BinarySearch;

public class FindRotationCount {
    public static int findKRotation(int[] arr) {
        int low = 0, high = arr.length - 1;
        int ans = Integer.MAX_VALUE;
        int index = -1;
        while (low <= high) {
            int mid = (low + high) / 2;
            // search space is already sorted
            // then arr[low] will always be
            // the minimum in that search space:
            System.out.println("low: " + low + " mid: " + mid + " high: " + high);
            if (arr[low] <= arr[high]) {
                System.out.println("FOUND " + arr[low] + " " + arr[high]);
                if (arr[low] < ans) {
                    index = low;
                    ans = arr[low];
                }
                break;
            }

            // If left part is sorted:
            if (arr[low] <= arr[mid]) {
                System.out.println("LEFT " + arr[low] + " " + arr[mid]);
                // keep the minimum:
                if (arr[low] < ans) {
                    index = low;
                    ans = arr[low];
                }

                // Eliminate left half:
                low = mid + 1;
            } else { // If right part is sorted:
                System.out.println("RIGHT " + arr[mid] + " " + arr[high]);
                // Keep the minimum:
                if (arr[mid] < ans) {
                    index = mid;
                    ans = arr[mid];
                }

                // Eliminate right half:
                high = mid - 1;
            }
            System.out.println("low: " + low + " mid: " + mid + " high: " + high);
        }
        return index;
    }

    public int findMin(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        while (start < end) {

            int mid = (start + end) / 2;
            System.out.println("start: " + start + " mid: " + mid + " end: " + end);
            if (nums[end] > nums[mid]) {
                System.out.println("RIGHT " + nums[mid] + " " + nums[end]);
                end = mid;
            } else {
                System.out.println("LEFT " + nums[start] + " " + nums[mid]);
                start = mid + 1;
            }
        }
        return nums[start];
    }

    /*
     * Time Complexity: O(logN)
     */
    public static void main(String[] args) {
        int[] arr = {4, 5, 6, 7, 0, 1, 2, 3};
        int ans = findKRotation(arr);
        System.out.println("The array is rotated " + ans + " times.");
        int[] arr2 = {4, 5, 6, 7, 0, 1, 2, 3};
        int ans2 = findKRotation(arr2);
        System.out.println("The array is rotated " + ans2 + " times.");
    }
}
