package Questions.Greedy;

/*
 https://leetcode.com/problems/jump-game-ii/
 You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
Time Complexity: O(n) because we iterate through the array once.
Space Complexity: O(1) because we use a constant amount of extra space.

 */
public class JumpGameII {
    public int jump(int[] nums) {
        int jumps = 0;
        int currentEnd = 0;
        int farthest = 0;
        int n = nums.length;

        for (int i = 0; i < n - 1; i++) {
            // Update the farthest index we can reach
            farthest = Math.max(farthest, i + nums[i]);

            // If we have reached the end of the current jump range
            if (i == currentEnd) {
                jumps++;
                currentEnd = farthest;

                // If we have reached or exceeded the last index
                if (currentEnd >= n - 1) {
                    break;
                }
            }
        }

        return jumps;
    }

    public static void main(String[] args) {
        JumpGameII jumpGameII = new JumpGameII();
        int[] nums = { 2, 3, 1, 1, 4 };
        System.out.println(jumpGameII.jump(nums)); // Output: 2

        nums = new int[] { 2, 3, 0, 1, 4 };
        System.out.println(jumpGameII.jump(nums)); // Output: 2
    }
}
