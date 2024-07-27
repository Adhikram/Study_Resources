package Questions.BackTracking;

import java.util.ArrayList;

/*
https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/
 Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.

Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.

 

Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Constraints:

2 <= n <= 9
0 <= k <= 9
Time Complexity: O(2^n)
Space Complexity: O(2^n)
 */
public class NumberWithSameConsecutiveDiff {
    public void backtrack(int val, int length, int k, ArrayList<Integer> result) {
        if (length == 0) {
            result.add(val);
            return;
        }
        if (k + val % 10 < 10) {
            backtrack((val * 10) + (k + val % 10), length - 1, k, result);
        }
        if ((val % 10 - k) > -1 && k != 0) {
            backtrack((val * 10) + (val % 10 - k), length - 1, k, result);
        }

    }

    public int[] numsSameConsecDiff(int n, int k) {
        ArrayList<Integer> result = new ArrayList();

        for (int i = 1; i <= 9; i++) {
            backtrack(i, n - 1, k, result);
        }
        System.out.println(result);
        return result.stream().mapToInt(i -> i).toArray();
    }

    public static void main(String[] args) {
        NumberWithSameConsecutiveDiff numberWithSameConsecutiveDiff = new NumberWithSameConsecutiveDiff();
        numberWithSameConsecutiveDiff.numsSameConsecDiff(3, 7);
    }
}
