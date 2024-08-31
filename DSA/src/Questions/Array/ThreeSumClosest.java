package Questions.Array;

import java.util.Arrays;
/*
 https://leetcode.com/problems/3sum-closest/
 Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
 */
public class ThreeSumClosest {
public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int closestSum = nums[0] + nums[1] + nums[2]; 

        for (int i = 0; i < nums.length - 2; i++) {
            int start = i + 1;
            int end = nums.length - 1;

            while (start < end) {
                int sum = nums[i] + nums[start] + nums[end];

                if (Math.abs(target - sum) < Math.abs(target - closestSum)) {
                    closestSum = sum; 
                }

                if (sum < target) {
                    start++; 
                } else {
                    end--; // Decrement k to decrease the sum
                }
            }
        }

        return closestSum;
    }

    public static void main(String[] args) {
        ThreeSumClosest threeSumClosest = new ThreeSumClosest();
        int[] nums = {1, 2, 4, 8, 16, 32, 64, 128};
        int target = 82;
        System.out.println(threeSumClosest.threeSumClosest(nums, target));
    }
}
