package Questions.Array;

import java.util.Arrays;

/*
https://leetcode.com/problems/first-missing-positive/description/
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
Time Complexity: O(n)
Space Complexity: O(1)
 */
public class FirstMissingPositive {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        int index = 0;

        while (index < n) {

            int cur = nums[index] - 1;

            if (cur >= 0 && cur < n && nums[cur] != nums[index]) {
                int temp = nums[cur];
                nums[cur] = nums[index];
                nums[index] = temp;
            } else {
                index++;
            }
        }
        Arrays.stream(nums).forEach(System.out::println);
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }

        return nums.length + 1;
    }

    public static void main(String[] args) {
        FirstMissingPositive obj = new FirstMissingPositive();
        int[] nums = { 3, 4, -1, 1 };
        System.out.println(obj.firstMissingPositive(nums));
    }
}
