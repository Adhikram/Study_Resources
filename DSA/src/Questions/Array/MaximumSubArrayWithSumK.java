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
            if(prefixSum == k){
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
     
     */
    public static int getLongestSubArrayOptimized(int[] nums, int k) {
        HashMap<Integer, Integer> hash = new HashMap<>();
        hash.put(0, -1);
        int prefixSum = 0;
        int result = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            // System.out.println(nums[i] + " Pre- " + prefixSum);
            prefixSum += nums[i];
            if(prefixSum == k){
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

    public static void main(String[] args) {
        int[] nums = new int[] { -1, 1, 1 };
        System.out.println(getLongestSubArray(nums, 1));
    }
}
