package Questions.Array;

public class FindDuplicated {
    public static int findDuplicate(int[] nums) {
        int slowPointer = nums[nums[0]];
        int fastPointer = nums[nums[nums[0]]];
        while(fastPointer != slowPointer){
            slowPointer = nums[slowPointer];
            fastPointer = nums[nums[fastPointer]];
        }
        slowPointer = nums[0];
        while(fastPointer != slowPointer){
            slowPointer = nums[slowPointer];
            fastPointer = nums[fastPointer];
        }
        return slowPointer;

    }
    public static void main(String[] args) {
        int[] nums = new int[]{1,3,4,2,2};
        System.out.println(findDuplicate(nums));
    }
}
