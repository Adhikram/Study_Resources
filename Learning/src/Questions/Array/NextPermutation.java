package Questions.Array;

import java.util.Arrays;

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
        // After break1 every thing is in decending
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

        System.out.println(Arrays.toString(nums));
        // Reverse the Break1 to break2
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
        int[] array = new int[] { 1, 2, 3 };
        nextPermutation(array);
        for (int element : array) {
            System.out.println(element);
        }

    }
}
