package Questions.Array;
/*
https://leetcode.com/problems/max-consecutive-ones-iii/description/
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
Explanation:
Initialization:

left and right pointers are initialized at the start of the array.
zeroCount keeps track of the number of zeros in the current window.
maxLen stores the maximum length of the subarray with at most k zeros.
Window Expansion:

Iterate through the array using the right pointer. If a zero is encountered, increment zeroCount.
Window Shrinking:

If zeroCount exceeds k, increment the left pointer until zeroCount is less than or equal to k.
Update Maximum Length:

For each valid window (where zeroCount ≤ k), update maxLen with the current window size (right - left + 1).
Time Complexity:
O(n): We only traverse the array once with the right pointer, and each element is processed at most twice (once by right and once by left).
Space Complexity:
O(1): We use only a few integer variables for counting and pointer manipulation, regardless of the input size.
 */
public class MaxConsecutiveOnesIII {
    public int longestOnes(int[] nums, int k) {
        int left = 0, right = 0;
        int maxLen = 0;
        int zeroCount = 0;

        while (right < nums.length) {
            if (nums[right] == 0) {
                zeroCount++;
            }

            // If the number of zeros exceeds k, shrink the window from the left
            while (zeroCount > k) {
                if (nums[left] == 0) {
                    zeroCount--;
                }
                left++;
            }

            // Calculate the maximum length of the window
            maxLen = Math.max(maxLen, right - left + 1);

            right++;
        }

        return maxLen;
    }
    public static void main(String[] args) {
        MaxConsecutiveOnesIII maxConsecutiveOnesIII = new MaxConsecutiveOnesIII();
        int[] nums = {1,1,1,0,0,0,1,1,1,1,0};
        int k = 2;
        System.out.println(maxConsecutiveOnesIII.longestOnes(nums, k)); // 6
    }
}
