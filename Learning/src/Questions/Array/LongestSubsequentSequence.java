package Questions.Array;

import java.util.HashMap;

public class LongestSubsequentSequence {
    public int traverse(HashMap<Integer, Boolean> hash, int num, int op) {
        System.out.println(num + " " + op);
        hash.forEach( (k, v) -> System.out.print(k + " " + v + " || "));
        System.out.println("");
        int count = 0;
        while (hash.getOrDefault(num, false)) {
            hash.put(num, false);
            num = num + op;
            count++;
        }
        return count;
    }

    public int longestConsecutive(int[] nums) {
        HashMap<Integer, Boolean> hash = new HashMap<>();

        for (int num : nums) {
            hash.put(num, true);
        }

        int result = 0;
        for (int num : nums) {
            int currResult = traverse(hash, num + 1, 1) + traverse(hash, num, -1);
            System.out.println(currResult + " " + num   + " " + result);
            result = Math.max(result, currResult);
        }
        return result;
    }

    public static void main(String[] args) {
        int[] nums = new int[] { 100, 4, 200, 1, 3, 2 };
        LongestSubsequentSequence longestSubsequentSequence = new LongestSubsequentSequence();
        System.out.println(longestSubsequentSequence.longestConsecutive(nums));
    }
}
