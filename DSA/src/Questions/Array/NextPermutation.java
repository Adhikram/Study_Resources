package Questions.Array;

import java.util.Arrays;
/*
 https://leetcode.com/problems/next-permutation/description/
 A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
 */
public class NextPermutation {
    static void nextPermutation(int[] nums) {
        int n = nums.length;

        int break1 = -1;
        int break2 = -1;

        // Trying to find the increasing order index
        for (int idx = n - 1; idx > 0; idx--) {
            if (nums[idx - 1] < nums[idx]) {
                break1 = idx - 1;
                break;
            }
        }
        System.out.println("Break1: " + break1);

        if (break1 == -1) {
            // The list is reverse sorted
            Arrays.sort(nums);
            return;
            // Arrays.sort(nums, Comparator.reverseOrder());
        }
        // After break1 every thing is in descending
        // Trying to find the number just bigger then the break 1 number
        for (int idx = n - 1; idx > 0; idx--) {
            if (nums[break1] < nums[idx]) {
                break2 = idx;
                break;
            }
        }
        // Swapping the numbers
        int temp = nums[break1];
        nums[break1] = nums[break2];
        nums[break2] = temp;

        // System.out.println(Arrays.toString(nums));
        // Reverse the Break1 to n
        int left = break1 + 1;
        int right = n - 1;
        while (left < right) {
            temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }

    }

    public static void main(String[] args) {
        int[] array = new int[] { 1, 2, 3, 4 , 6, 5, 4, 3 };
        System.out.println(Arrays.toString(array));
        nextPermutation(array);
        System.out.println(Arrays.toString(array));
    }
}
