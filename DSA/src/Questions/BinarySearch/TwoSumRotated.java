package Questions.BinarySearch;

import java.util.Arrays;

public class TwoSumRotated {
    public static int[] twoSum(int[] nums, int target) {
        int pivot = findPivot(nums);
        System.out.println("Pivot: " + pivot); // Output: "Pivot: 4
        int left = pivot;
        int right = (pivot - 1) % nums.length;

        while (left != right) {
            System.out.println("Left: " + left + " Right: " + right); // Output: "Left: 4 Right: 3"
            int sum = nums[left] + nums[right];
            System.out.println("Sum: " + sum);
            if (sum == target) {
                return new int[] { nums[left], nums[right] };
            } else if (sum > target) {
                right = (right - 1) % nums.length;
            } else {
                left = (left + 1) % nums.length;
            }
        }

        return new int[0];
    }

    private static int findPivot(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }

    public static void main(String[] args) {
        int[] nums = { 4, 5, 6, 7, 8, 0, 1, 2 };
        int target = 9;
        int[] result = twoSum(nums, target);
        System.out.println(Arrays.toString(result)); // Output: [2, 7]
    }
}
