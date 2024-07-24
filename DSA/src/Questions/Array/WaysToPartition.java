package Questions.Array;

import java.util.HashMap;
import java.util.Map;
/*
https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/description/
 You are given a 0-indexed integer array nums of length n. The number of ways to partition nums is the number of pivot indices that satisfy both conditions:

1 <= pivot < n
nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]
You are also given an integer k. You can choose to change the value of one element of nums to k, or to leave the array unchanged.

Return the maximum possible number of ways to partition nums to satisfy both conditions after changing at most one element.

 

Example 1:

Input: nums = [2,-1,2], k = 3
Output: 1
Explanation: One optimal approach is to change nums[0] to k. The array becomes [3,-1,2].
There is one way to partition the array:
- For pivot = 2, we have the partition [3,-1 | 2]: 3 + -1 == 2.
Example 2:

Input: nums = [0,0,0], k = 1
Output: 2
Explanation: The optimal approach is to leave the array unchanged.
There are two ways to partition the array:
- For pivot = 1, we have the partition [0 | 0,0]: 0 == 0 + 0.
- For pivot = 2, we have the partition [0,0 | 0]: 0 + 0 == 0.
Example 3:

Input: nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33
Output: 4
Explanation: One optimal approach is to change nums[2] to k. The array becomes [22,4,-33,-20,-15,15,-16,7,19,-10,0,-13,-14].
There are four ways to partition the array.
 

Constraints:

n == nums.length
2 <= n <= 105
-105 <= k, nums[i] <= 105
 */
public class WaysToPartition {
    public int waysToPartition(int[] nums, int k) {

        long s = 0;
        for (int n : nums)
            s += n;
        Map<Long, Integer> map = new HashMap<Long, Integer>();
        long r = 0;
        for (int i = nums.length - 1; i > 0; i--) {
            r += nums[i]; // sufix sum from i
            long t = s - r * 2 + k; // this suffix sum (r) would qualify as pivot if in the corresponding prefix an
                                    // element of value t was changed to k
            map.put(t, map.getOrDefault(t, 0) + 1);
        }

        long l = 0;
        int resp = map.getOrDefault((long) nums[0], 0);
        int none = 0; // count of pivots for unchanged array
        for (int i = 1; i < nums.length; i++) {
            l += nums[i - 1]; // prefix sum up to i-1
            if (l * 2 == s)
                none++; // i is a pivot for unchanged array
            long t = s - l * 2;
            map.put(t + k, map.getOrDefault(t + k, 0) + 1); // this prefix sum (l) would qualify as pivot if in the
                                                            // corresponding suffix an element of value t+k was changed
                                                            // to k
            map.put(-t + k, map.get(-t + k) - 1); // remove the suffix contribution
            resp = Math.max(resp, map.getOrDefault((long) nums[i], 0)); // check the
        }
        return Math.max(resp, none);
    }

    public static void main(String[] args) {
        WaysToPartition obj = new WaysToPartition();
        int[] nums = { 2, -1, 2 };
        int k = 3;
        System.out.println(obj.waysToPartition(nums, k));
    }
}
