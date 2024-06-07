package Questions.DP;

public class MaxProductSubArray {
    // Problem:- Given an array that contains both negative and positive integers,
    // find the maximum product subarray.

    static int maxProductSubArrayOptimal(int[] arr) {
        int maxProd = arr[0], minProd = arr[0], result = arr[0];
        // maxProd stores the Maximum value of the subarray ending at the current index
        // minProd stores the Minimum value of the subarray ending at the current index

        for (int i = 1; i < arr.length; i++) {
            // maxProd will store the maximum value of the subarray ending at the current
            // index
            int temp = Math.max(arr[i], Math.max(maxProd * arr[i], minProd * arr[i]));
            // minProd will store the minimum value of the subarray ending at the current
            // index
            minProd = Math.min(arr[i], Math.min(maxProd * arr[i], minProd * arr[i]));
            maxProd = temp;

            // result will store the maximum value of the subarray ending at any index
            result = Math.max(result, maxProd);
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
