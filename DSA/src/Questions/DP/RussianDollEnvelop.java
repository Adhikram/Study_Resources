package Questions.DP;

import java.util.Arrays;
/*
https://leetcode.com/problems/russian-doll-envelopes/description/
 You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

 

Example 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Example 2:

Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
 

Constraints:

1 <= envelopes.length <= 105
envelopes[i].length == 2
1 <= wi, hi <= 105
Time Complexity: O(NlogN)
Space Complexity: O(N)
 */
public class RussianDollEnvelop {
    public int binarySearch(int[] dp, int val) {
        int lo = 0, hi = dp.length - 1, res = 0;
        while (lo <= hi) {
            int mid = (lo + hi) >> 1;
            if (dp[mid] < val) {
                res = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return res + 1;
    }

    public int maxEnvelopes(int[][] envelopes) {
        Arrays.sort(envelopes, (a, b) -> (a[0] == b[0]) ? (b[1] - a[1]) : (a[0] - b[0]));
        int[] LIS = new int[envelopes.length + 1];
        Arrays.fill(LIS, Integer.MAX_VALUE);
        LIS[0] = Integer.MIN_VALUE;
        int ans = 0;
        for (int i = 0; i < envelopes.length; i++) {
            int val = envelopes[i][1];
            int insertIndex = binarySearch(LIS, val);
            System.out.println("VAL: " + val);
            System.out.println("Insert Index :" + insertIndex);
            ans = Math.max(ans, insertIndex);
            if (LIS[insertIndex] >= val) {
                LIS[insertIndex] = val;
            }
            System.out.println();
            for (int j = 0; j < LIS.length; j++) {
                System.out.print(LIS[j] + " ");
            }
            System.out.println();
        }
        return ans;
    }
    public static void main(String[] args) {
        RussianDollEnvelop russianDollEnvelop = new RussianDollEnvelop();
        int[][] envelopes = {{5, 4}, {6, 4}, {6, 7}, {2, 3}, {1, 2}};
        System.out.println(russianDollEnvelop.maxEnvelopes(envelopes));
    }
}
