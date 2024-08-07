package Questions.Graph.TopologicalSort;

/*
https://leetcode.com/problems/satisfiability-of-equality-equations/description/
 You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

 

Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
Example 2:

Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
 

Constraints:

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] is a lowercase letter.
equations[i][1] is either '=' or '!'.
equations[i][2] is '='.
equations[i][3] is a lowercase letter.
Time complexity: O(n)
Space complexity: O(n)
 */
public class QuestionsPossible {
    public boolean equationsPossible(String[] equations) {
        int[] parents = new int[26];
        for (int i = 0; i < 26; i++) {
            parents[i] = i;
        }

        for (String e : equations) {
            if (e.charAt(1) == '=') {
                int parentL = find(e.charAt(0) - 'a', parents);
                int parentR = find(e.charAt(3) - 'a', parents);

                parents[parentL] = parents[parentR];
            }
        }

        for (String e : equations) {
            if (e.charAt(1) == '!') {
                int parentL = find(e.charAt(0) - 'a', parents);
                int parentR = find(e.charAt(3) - 'a', parents);

                if (parents[parentL] == parents[parentR]) {
                    return false;
                }
            }
        }

        return true;

    }

    public int find(int x, int[] parents) {
        if (parents[x] == x) {
            return x;
        }
        // With Path Compression
        return parents[x] = find(parents[x], parents);
    }
    public static void main(String[] args) {
        QuestionsPossible questionsPossible = new QuestionsPossible();
        String[] equations = {"a==b","b!=a"};
        System.out.println(questionsPossible.equationsPossible(equations)); // false
    }
}
