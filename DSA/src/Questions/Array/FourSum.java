package Questions.Array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
 https://leetcode.com/problems/4sum/description/
 Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
Time Complexity: O(n^3) because we iterate through the array with two nested loops and use two pointers for each pair.
Space Complexity: O(1) for the extra space used, excluding the space required for the output list.

 */
public class FourSum {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        
        // Sort the array
        Arrays.sort(nums);
        
        int n = nums.length;
        
        // First two nested loops to fix the first two numbers
        for (int i = 0; i < n - 3; i++) {
            // Skip duplicates for the first element
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            for (int j = i + 1; j < n - 2; j++) {
                // Skip duplicates for the second element
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                
                int left = j + 1, right = n - 1;
                long targetSum = (long)target - nums[i] - nums[j]; // Prevent overflow
                
                while (left < right) {
                    long sum = (long)nums[left] + nums[right];
                    
                    if (sum == targetSum) {
                        // Found a quadruplet
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        
                        // Skip duplicates for the third and fourth elements
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;
                        
                        // Move the pointers
                        left++;
                        right--;
                    } else if (sum < targetSum) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }
        
        return result;
    }

    public static void main(String[] args) {
        FourSum fourSum = new FourSum();
        int[] nums = { 1, 0, -1, 0, -2, 2 };
        int target = 0;
        System.out.println(fourSum.fourSum(nums, target));
    }
}
