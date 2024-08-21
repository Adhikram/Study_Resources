package Questions.String;

import java.util.HashMap;

public class LongestSubsequentSequence {
    public int traverse(HashMap<Integer, Boolean> hash, int num, int op) {
        // System.out.println(num + " " + op);
        // hash.forEach( (k, v) -> System.out.print(k + " " + v + " || "));
        // System.out.println("");
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
            int curResult = traverse(hash, num + 1, 1) + traverse(hash, num, -1);
            // System.out.println(curResult + " " + num   + " " + result);
            result = Math.max(result, curResult);
        }
        return result;
    }

    public int longestConsecutiveOptimized(int[] nums) {
        HashMap<Integer, Boolean> hash = new HashMap<>();
        for (int num : nums) {
            hash.put(num, true);
        }

        int result = 0;
        for (int num : nums) {
            if (!hash.getOrDefault(num - 1, false)) {
                int curResult = traverse(hash, num + 1, 1);
                result = Math.max(result, curResult + 1);
            }
        }
        return result;
    }
    /*
     * Time complexity: O(n) Space complexity: O(n)
     */

    public static void main(String[] args) {
        int[] nums = new int[] { 100, 4, 200, 1, 3, 2 };
        LongestSubsequentSequence longestSubsequentSequence = new LongestSubsequentSequence();
        System.out.println(longestSubsequentSequence.longestConsecutive(nums));
        System.out.println(longestSubsequentSequence.longestConsecutiveOptimized(nums));
    }
}
