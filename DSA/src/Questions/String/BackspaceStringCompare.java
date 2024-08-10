package Questions.String;
/*
https://leetcode.com/problems/backspace-string-compare/description/
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?
Time Complexity: O(n)
Space Complexity: O(1)
 */
public class BackspaceStringCompare {
    public boolean backspaceCompare(String s, String t) {
        int i = s.length() - 1, j = t.length() - 1;

        while (i >= 0 || j >= 0) {
            i = getNextValidIndex(s, i);
            j = getNextValidIndex(t, j);

            if (i < 0 && j < 0) {
                return true; // Both pointers have reached the beginning of the string
            }
            if (i < 0 || j < 0) {
                return false; // One string is still left with characters
            }
            if (s.charAt(i) != t.charAt(j)) {
                return false; // Characters at both pointers don't match
            }

            i--;
            j--;
        }

        return true;
    }

    private int getNextValidIndex(String str, int index) {
        int skip = 0;
        while (index >= 0) {
            if (str.charAt(index) == '#') {
                skip++;
            } else if (skip > 0) {
                skip--;
            } else {
                break;
            }
            index--;
        }
        return index;
    }

    public static void main(String[] args) {
        BackspaceStringCompare backspaceStringCompare = new BackspaceStringCompare();
        String s = "ab#c";
        String t = "ad#c";
        System.out.println(backspaceStringCompare.backspaceCompare(s, t)); // true
    }
}
