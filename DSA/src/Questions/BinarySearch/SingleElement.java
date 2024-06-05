package Questions.BinarySearch;

public class SingleElement {

    public static int singleNonDuplicate(int[] arr) {
        int n = arr.length; // Size of the array.

        int low = 0, high = n - 1;
        while (low <= high) {
            int mid = (high + low) >> 1;

            // If arr[mid] is the single element:
            if ((mid == 0 || arr[mid] != arr[mid - 1]) && (mid == n - 1 || arr[mid] != arr[mid + 1])) {
                return arr[mid];
            }

            // Check if we are in the left part of the pair.
            if (mid % 2 == 0) {
                // If the mid is at an even index, and the next element is the same,
                // then the single element is on the right side.
                if (mid + 1 < n && arr[mid] == arr[mid + 1]) {
                    low = mid + 1;
                } else {
                    // If the mid is at an even index and the next element is different,
                    // then the single element is on the left side.
                    high = mid - 1;
                }
            } else {
                // Check if we are in the right part of the pair.
                // Similar logic as above but in reverse for odd indices.
                if (arr[mid] == arr[mid - 1]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }

        // Dummy return statement:
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8 };
        int ans = singleNonDuplicate(arr);
        System.out.println("The single element is: " + ans);
    }
}
