package Questions.DP;

public class MaxProductSubArray {
    // Problem:- Given an array that contains both negative and positive integers,
    // find the maximum product subarray.

    static int maxProductSubArrayOptimal(int arr[]) {
        int prod1 = arr[0], prod2 = arr[0], result = arr[0];
        // prod1 stores the Maximum value of the subarray ending at the current index
        // prod2 stores the Minimum value of the subarray ending at the current index

        for (int i = 1; i < arr.length; i++) {
            // prod1 will store the maximum value of the subarray ending at the current
            // index
            int temp = Math.max(arr[i], Math.max(prod1 * arr[i], prod2 * arr[i]));
            // prod2 will store the minimum value of the subarray ending at the current
            // index
            prod2 = Math.min(arr[i], Math.min(prod1 * arr[i], prod2 * arr[i]));
            prod1 = temp;

            // result will store the maximum value of the subarray ending at any index
            result = Math.max(result, prod1);
        }
        return result;
    }
    // Time Complexity: O(N)

    // Reason: A single iteration is used.

    // Space Complexity: O(1)
    public static void main(String[] args) {
        int[] arr = { 6, -3, -10, 0, 2 };
        System.out.println(maxProductSubArrayOptimal(arr)); // 180
    }
}
