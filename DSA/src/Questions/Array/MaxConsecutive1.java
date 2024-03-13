package Questions.Array;

public class MaxConsecutive1 {
    public int findMaxConsecutiveOnes(int[] nums) {
        int result = 0;
        int count = 0;
        for (int num : nums) {
            if (num == 0) {
                result = Math.max(result, count);
                count = 0;
            } else {
                count++;
            }
        }
        return Math.max(result, count);
    }

    public static void main(String[] args) {
        MaxConsecutive1 maxConsecutive1 = new MaxConsecutive1();
        int[] nums = { 1, 1, 0, 1, 1, 1 };
        System.out.println(maxConsecutive1.findMaxConsecutiveOnes(nums));
    }
}
