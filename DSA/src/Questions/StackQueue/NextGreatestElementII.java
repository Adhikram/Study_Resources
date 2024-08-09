package Questions.StackQueue;

import java.util.Stack;

/*
https://leetcode.com/problems/next-greater-element-ii/description/
 Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
 */
public class NextGreatestElementII {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>(); // stack to store indices

        // Initialize the result array with -1
        for (int i = 0; i < n; i++) {
            result[i] = -1;
        }

        // Iterate twice through the array to simulate circular behavior
        for (int i = 0; i < 2 * n; i++) {
            int num = nums[i % n];
            while (!stack.isEmpty() && nums[stack.peek()] < num) {
                result[stack.pop()] = num;
            }
            if (i < n) {
                stack.push(i);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        NextGreatestElementII obj = new NextGreatestElementII();
        int[] nums = { 1, 2, 1 };
        int[] result = obj.nextGreaterElements(nums);
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
