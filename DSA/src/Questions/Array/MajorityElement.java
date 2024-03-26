package Questions.Array;

public class MajorityElement {
    public static int majorityElement(int[] nums) {
        int count = 0;
        int elem = nums[0];
        for (int num : nums) {
            if (elem == num) {
                count++;
            } else {
                count--;
                if (count <= 0) {
                    count = 1;
                    elem = num;
                }

            }
        }
        return elem;

    }
    /*
     * Time complexity: O(n) Space complexity: O(1)
     
     */

    public static void main(String[] args) {
        int[] nums = new int[] { 3, 2, 3 };
        System.out.println(majorityElement(nums));
    }
}
