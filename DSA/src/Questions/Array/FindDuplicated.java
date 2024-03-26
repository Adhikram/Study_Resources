package Questions.Array;

// This is the solution for the problem in which we have to find the duplicate number in an array of n+1 integers where each integer is between 1 and n (inclusive).
public class FindDuplicated {
    public static int findDuplicate(int[] nums) {
        // Floyd's Tortoise and Hare (Cycle Detection)
        // Time complexity: O(n)
        int slowPointer = nums[0];
        int fastPointer = nums[0];
        while (fastPointer < nums.length && nums[fastPointer] < nums.length) {
            slowPointer = nums[slowPointer];
            fastPointer = nums[nums[fastPointer]];
            if (slowPointer == fastPointer) {
                break;
            }
        }
        slowPointer = nums[0];
        if(fastPointer >= nums.length) {
            return -1;
        }
        while (fastPointer != slowPointer) {
            slowPointer = nums[slowPointer];
            fastPointer = nums[fastPointer];
        }
        return slowPointer;

    }

    public static void main(String[] args) {
        int[] nums = new int[] { 1, 3, 4, 2, 2 };
        System.out.println(findDuplicate(nums));
    }
}
