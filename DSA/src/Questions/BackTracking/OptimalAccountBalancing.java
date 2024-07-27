package Questions.BackTracking;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

/*
https://leetcode.com/problems/optimal-account-balancing/description/
 You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

Return the minimum number of transactions required to settle the debt.

 

Example 1:

Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
Example 2:

Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
Output: 1
Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, and all debt is settled.
 

Constraints:

1 <= transactions.length <= 8
transactions[i].length == 3
0 <= fromi, toi < 12
fromi != toi
1 <= amounti <= 100
Time Complexity: O(2^n * N)
Space Complexity: O(2^n)
 */
public class OptimalAccountBalancing {
    public int minTransfers(int[][] transactions) {
        Map<Integer, Integer> m = new HashMap<>();
        for (int[] t : transactions) {
            m.put(t[0], m.getOrDefault(t[0], 0) - t[2]);
            m.put(t[1], m.getOrDefault(t[1], 0) + t[2]);
        }
        ArrayList<Integer> debt = new ArrayList();
        int i = 0;
        for (int d : m.values()) {
            if (d != 0) {
                debt.add(d);
            }
        }
        return settle(0, debt);
    }

    int settle(int start, ArrayList<Integer> debt) {
        if (start == debt.size()) {
            return 0;
        }
        int cur = debt.get(start);
        if (cur == 0) {
            return settle(start + 1, debt);
        }
        int min = Integer.MAX_VALUE;
        for (int i = start + 1; i < debt.size(); i++) {
            int next = debt.get(i);
            if (cur * next < 0) {
                debt.set(i, cur + next);
                min = Math.min(min, 1 + settle(start + 1, debt));
                debt.set(i, next);

                if (cur + next == 0) {
                    break;
                }
            }
        }
        return min;
    }
    public static void main(String[] args) {
        OptimalAccountBalancing optimalAccountBalancing = new OptimalAccountBalancing();
        System.out.println(optimalAccountBalancing.minTransfers(new int[][]{{0,1,10},{2,0,5}}));
        System.out.println(optimalAccountBalancing.minTransfers(new int[][]{{0,1,10},{1,0,1},{1,2,5},{2,0,5}}));
    }

}
