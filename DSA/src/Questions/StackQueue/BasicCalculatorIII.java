package Questions.StackQueue;

import java.util.Stack;

/*
https://leetcode.com/problems/basic-calculator-iii/description/
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1+1"
Output: 2
Example 2:

Input: s = "6-4/2"
Output: 4
Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
 

Constraints:

1 <= s <= 104
s consists of digits, '+', '-', '*', '/', '(', and ')'.
s is a valid expression.

Explanation:
Immediate Result Update: Instead of storing results in a stack, we immediately add or subtract the current number to the result based on the last sign (+ or -).

Multiplication and Division: These operations are handled as soon as they are encountered. We update currentNumber directly with the product or quotient.

Parentheses:

When encountering (, push the current result and sign to the stack and reset them for the sub-expression.
When encountering ), pop from the stack to restore the previous context and continue.
Final Result: After processing the entire string, any remaining currentNumber is added to the result.

Complexity:
Time Complexity: O(n) — each character in the string is processed exactly once.
Space Complexity: O(1) in terms of the calculation, but O(m) if counting the space used by the stack for handling parentheses (where m is the depth of nested parentheses).
 */
public class BasicCalculatorIII {
    public boolean isDigit(char currentChar) {
        return '0' <= currentChar && currentChar <= '9';
    }

    public int calculate(String s) {
        Stack<Integer> stack = new Stack<>();
        int currentNumber = 0;
        char operation = '+';
        int n = s.length();

        for (int i = 0; i < n; i++) {
            char currentChar = s.charAt(i);

            if (isDigit(currentChar)) {
                currentNumber = currentNumber * 10 + (currentChar - '0');
            }

            if (currentChar == '(') {
                // Find the matching ')' and evaluate the expression inside
                int j = i, count = 0;
                for (; i < n; i++) {
                    if (s.charAt(i) == '(')
                        count++;
                    if (s.charAt(i) == ')')
                        count--;
                    if (count == 0)
                        break;
                }
                currentNumber = calculate(s.substring(j + 1, i));
            }

            if (!isDigit(currentChar) && currentChar != ' ' || i == n - 1) {
                switch (operation) {
                    case '+':
                        stack.push(currentNumber);
                        break;
                    case '-':
                        stack.push(-currentNumber);
                        break;
                    case '*':
                        stack.push(stack.pop() * currentNumber);
                        break;
                    case '/':
                        stack.push(stack.pop() / currentNumber);
                        break;
                }
                operation = currentChar;
                currentNumber = 0;
            }
        }

        // Sum up the values in the stack
        int result = 0;
        while (!stack.isEmpty()) {
            result += stack.pop();
        }

        return result;
    }
    public static void main(String[] args) {
        BasicCalculatorIII basicCalculatorIII = new BasicCalculatorIII();
        System.out.println(basicCalculatorIII.calculate("1+1")); // Output: 2
        System.out.println(basicCalculatorIII.calculate("6-4/2")); // Output: 4
        System.out.println(basicCalculatorIII.calculate("2*(5+5*2)/3+(6/2+8)")); // Output: 21
    }
}
