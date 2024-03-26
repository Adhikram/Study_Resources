package Questions.Array;

import java.util.Arrays;

public class RemoveDuplicate {

    public static int removeDuplicates(int[] nums) {
        int start = 0;
        int result = 0;
        int prev = Integer.MAX_VALUE;
        int n = nums.length;
        while (start < n) {
            if (nums[start] != prev) {
                prev = nums[start];
                int temp = nums[start];
                nums[start] = nums[result];
                nums[result] = temp;
                result++;
            }
            start++;
        }
        return result;
    }

    public static void main(String[] args) {
        int[] nums = { 1, 1, 2 };
        System.out.println(removeDuplicates(nums));
        System.out.println("Array after removing duplicates: " + Arrays.toString(nums));
    }
}
