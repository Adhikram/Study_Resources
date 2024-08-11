package Questions.StackQueue;

import java.util.Stack;

/*
 Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
Time Complexity: O(n)
Space Complexity: O(1)
 */
public class BasicCalculator {
    public boolean isDigit(char currentChar) {
        return '0' <= currentChar && currentChar <= '9';
    }

    public int calculate(String s) {
        Stack<Integer> stack = new Stack<>();
        int result = 0;
        int sign = 1;
        int i = 0;

        while (i < s.length()) {
            char c = s.charAt(i);

            if (isDigit(c)) {
                int num = 0;
                while (i < s.length() && isDigit(s.charAt(i))) {
                    num = num * 10 + (s.charAt(i) - '0');
                    i++;
                }
                result += sign * num;
                i--; // Step back to process the next character correctly
            } else if (c == '+') {
                sign = 1;
            } else if (c == '-') {
                sign = -1;
            } else if (c == '(') {
                // Push the current result and sign onto the stack
                stack.push(result);
                stack.push(sign);
                // Reset result and sign for new sub-expression
                result = 0;
                sign = 1;
            } else if (c == ')') {
                // Pop the sign and result before the parenthesis
                result = stack.pop() * result + stack.pop();
            }
            i++;
        }

        return result;
    }

    int i = 0;

    public int calculateOP(String s) {
        return calc(s);
    }

    private int calc(String s) {
        int num = 0, ans = 0;
        int sign = 1;
        while (i < s.length()) {
            char ch = s.charAt(i++);
            if (ch >= '0' && ch <= '9') {
                num = num * 10 + ch - '0';
            } else if (ch == '(') {
                num = calc(s);
            } else if (ch == ')') {
                return ans += num * sign;
            } else if (ch == '+' || ch == '-') {
                ans += num * sign;
                num = 0;
                sign = (ch == '-') ? -1 : 1;
            }
        }
        ans += num * sign;
        return ans;
    }

    public static void main(String[] args) {
        BasicCalculator basicCalculator = new BasicCalculator();
        System.out.println(basicCalculator.calculate("1 + 1")); // Output: 2
        System.out.println(basicCalculator.calculate(" 2-1 + 2 ")); // Output: 3
        System.out.println(basicCalculator.calculate("(1+(4+5+2)-3)+(6+8)")); // Output: 23
    }
}
