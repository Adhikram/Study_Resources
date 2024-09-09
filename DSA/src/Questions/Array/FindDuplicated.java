package Questions.Array;

/*
https://leetcode.com/problems/find-the-duplicate-number/description/
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 
Use Floyd's Tortoise and Hare (Cycle Detection) algorithm to find the duplicate number.

Initialize two pointers, slowPointer and fastPointer, both starting at the first element of the array.
Move slowPointer one step at a time and fastPointer two steps at a time until they meet. This indicates the presence of a cycle.

Find Entry Point of Cycle:
Reset slowPointer to the start of the array.
Move both slowPointer and fastPointer one step at a time until they meet again. The meeting point is the duplicate number.
 */
public class FindDuplicated {
    public static int findDuplicate(int[] nums) {
        // Floyd's Tortoise and Hare (Cycle Detection)
        // Time complexity: O(n)
        int slowPointer = nums[0];
        int fastPointer = nums[0];
        while (fastPointer < nums.length && nums[fastPointer] < nums.length) {
            slowPointer = nums[slowPointer];
            fastPointer = nums[nums[fastPointer]];
            if (slowPointer == fastPointer) {
                break;
            }
        }
        slowPointer = nums[0];
        if(fastPointer >= nums.length) {
            return -1;
        }
        while (fastPointer != slowPointer) {
            slowPointer = nums[slowPointer];
            fastPointer = nums[fastPointer];
        }
        return slowPointer;

    }

    public static void main(String[] args) {
        int[] nums = new int[] { 1, 3, 4, 2, 2 };
        System.out.println(findDuplicate(nums));
    }
}
