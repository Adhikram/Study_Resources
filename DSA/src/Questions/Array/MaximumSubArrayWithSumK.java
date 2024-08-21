package Questions.Array;

import java.util.HashMap;

public class MaximumSubArrayWithSumK {
    public static int getLongestSubArray(int[] nums, int k) {
        HashMap<Integer, Integer> hash = new HashMap<>();
        hash.put(0, -1);
        int prefixSum = 0;
        int result = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            // System.out.println(nums[i] + " Pre- " + prefixSum);
            prefixSum += nums[i];
            if (prefixSum == k) {
                result = i + 1;
            }
            if (hash.containsKey(prefixSum - k)) {
                // System.out.println(" PrefixSum: " + prefixSum + " " + (prefixSum - k) + " " +
                // i + " " + hash.get(prefixSum - k));
                int index = hash.get(prefixSum - k);
                result = Math.max(result, i - index);
                // System.out.println(" Result: " + result);
            }
            if (!hash.containsKey(prefixSum)) {
                hash.put(prefixSum, i);
            }

        }
        return result;

    }

    /*
     * Time complexity: O(n) Space complexity: O(n)
     *
     */
    public static int getLongestSubArrayOptimized(int[] nums, int k) {
        int maxLength = 0;
        int sum = 0;
        int start = 0;

        for (int end = 0; end < nums.length; end++) {
            sum += nums[end];

            // Shrink the window as long as the sum is greater than k
            while (sum > k) {
                sum -= nums[start];
                start++;
            }

            // Check if the current window's sum is equal to k
            if (sum == k) {
                maxLength = Math.max(maxLength, end - start + 1);
            }
        }

        return maxLength;
    }

    public static void main(String[] args) {
        int[] nums = new int[] { 1, -1, 1, 0, 2, -10 };
        System.out.println(getLongestSubArray(nums, 3));
        System.out.println(getLongestSubArrayOptimized(nums, 3));
    }
}
