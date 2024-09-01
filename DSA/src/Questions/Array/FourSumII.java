package Questions.Array;

import java.util.HashMap;
import java.util.Map;

/*
 https://leetcode.com/problems/4sum-ii/description/
 Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
 

Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
Time Complexity: O(n^2) because we compute all possible pairs from two arrays twice.
Space Complexity: O(n^2) for storing the sums and their counts in the HashMap.
 */
public class FourSumII {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        Map<Integer, Integer> sumCountMap = new HashMap<>();
        int count = 0;

        // Compute all possible sums of pairs from nums1 and nums2
        for (int num1 : nums1) {
            for (int num2 : nums2) {
                int sum = num1 + num2;
                sumCountMap.put(sum, sumCountMap.getOrDefault(sum, 0) + 1);
            }
        }

        // Compute all possible sums of pairs from nums3 and nums4
        for (int num3 : nums3) {
            for (int num4 : nums4) {
                int sum = num3 + num4;
                // Check if the negation of the current sum is in the map
                if (sumCountMap.containsKey(-sum)) {
                    count += sumCountMap.get(-sum);
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        FourSumII obj = new FourSumII();
        int[] nums1 = { 1, 2 };
        int[] nums2 = { -2, -1 };
        int[] nums3 = { -1, 2 };
        int[] nums4 = { 0, 2 };
        System.out.println(obj.fourSumCount(nums1, nums2, nums3, nums4)); // Output: 2
    }
}
