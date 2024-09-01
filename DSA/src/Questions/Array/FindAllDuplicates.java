package Questions.Array;

import java.util.ArrayList;
import java.util.List;

/*
 https://leetcode.com/problems/find-all-duplicates-in-an-array/
 Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
Time Complexity: O(n) because we traverse the array once.
Space Complexity: O(1) for the extra space used, excluding the space required for the output list.
 */
public class FindAllDuplicates {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> result = new ArrayList<>();

        // Traverse each element in the array
        for (int i = 0; i < nums.length; i++) {
            // Get the index corresponding to the current element's value
            int index = Math.abs(nums[i]) - 1;

            // If the value at that index is already negative, it means we've seen this
            // number before
            if (nums[index] < 0) {
                result.add(Math.abs(nums[i])); // Add the duplicate number to the result list
            } else {
                // Mark the value at that index as visited by negating it
                nums[index] = -nums[index];
            }
        }

        return result;
    }

    public static void main(String[] args) {
        FindAllDuplicates findAllDuplicates = new FindAllDuplicates();
        int[] nums = { 4, 3, 2, 7, 8, 2, 3, 1 };
        System.out.println(findAllDuplicates.findDuplicates(nums)); // Output: [2, 3]
    }
}
