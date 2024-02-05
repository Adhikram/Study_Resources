package Questions.Array;

public class RemoveDuplicate {

    public int removeDuplicates(int[] nums) {
        int start = 0;
        int result = 0;
        int prev = 101;
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
        RemoveDuplicate removeDuplicate = new RemoveDuplicate();
        int[] nums = { 1, 1, 2 };
        System.out.println(removeDuplicate.removeDuplicates(nums));
    }
}
