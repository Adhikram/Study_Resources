package Questions.Trie;

import java.util.ArrayList;
import java.util.Collections;

public class PowerSet {
    static ArrayList<String> AllPossibleStrings(String s) {
        int n = s.length();
        ArrayList<String> ans = new ArrayList<>();
        for (int num = 0; num < (1 << n); num++) {
            String sub = "";
            for (int i = 0; i < n; i++) {
                // check if the ith bit is set or not
                if ((num & (1 << i)) != 0) {
                    sub += s.charAt(i);
                }
            }
            if (sub.length() > 0) {
                ans.add(sub);
            }
        }
        Collections.sort(ans);
        return ans;
    }
    // Time Complexity: O(2^n * n)

    // Reason: O(2^n) for the outer for loop and O(n) for the inner for loop.

    // Space Complexity: O(1)

    static void solveBackTracking(int i, String s, String f) {
        if (i == s.length()) {
            System.out.print(f + " ");
            return;
        }
        // picking
        // f = f + s.charAt(i);
        solveBackTracking(i + 1, s, f + s.charAt(i));
        // poping out while backtracking
        // f.pop_back();
        solveBackTracking(i + 1, s, f);
    }

    public static void main(String args[]) {

        String s = "abc";
        ArrayList<String> ans = AllPossibleStrings(s);
        // print all the subsequence.
        System.out.println("All possible subsequences are ");
        solveBackTracking(0, s, "");
        System.out.println();
        for (String it : ans) {
            System.out.print(it + " ");
        }

    }
}
