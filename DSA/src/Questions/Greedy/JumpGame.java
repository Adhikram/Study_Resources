package Questions.Greedy;

/*
https://leetcode.com/problems/jump-game/description/
 You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
Time Complexity: O(n) because we iterate through the array once.
Space Complexity: O(1) because we use a constant amount of extra space.
 */
public class JumpGame {
    public boolean canJump(int[] nums) {
        int maxReach = 0;
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            // If the current index is beyond the maximum reachable index, return false
            if (i > maxReach) {
                return false;
            }
            // Update the maximum reachable index
            maxReach = Math.max(maxReach, i + nums[i]);
            // If we can reach or exceed the last index, return true
            if (maxReach >= n - 1) {
                return true;
            }
        }

        // If the loop ends, check if we can reach the last index
        return maxReach >= n - 1;
    }

    public static void main(String[] args) {
        JumpGame jumpGame = new JumpGame();
        int[] nums = { 2, 3, 1, 1, 4 };
        System.out.println(jumpGame.canJump(nums)); // Output: true

        nums = new int[] { 3, 2, 1, 0, 4 };
        System.out.println(jumpGame.canJump(nums)); // Output: false
    }
}
