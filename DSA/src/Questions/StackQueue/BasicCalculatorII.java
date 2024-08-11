package Questions.StackQueue;

/*
https://leetcode.com/problems/basic-calculator-ii/description/
 Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
Time Complexity: O(n)
Space Complexity: O(1)

Explanation:
Reduction in Stack Operations: Instead of pushing and popping from a stack, we keep track of the lastNumber directly and update it as necessary.
This reduces the overhead of stack operations.

On-the-fly Calculation: Multiplication and division are handled immediately when encountered,
 rather than storing the numbers first and then processing them later. This makes the algorithm more direct and reduces unnecessary operations.

Result Accumulation: The result is updated as we parse the string, and the lastNumber is added to the result only when necessary.
This eliminates the need to traverse a stack at the end.

Time Complexity:
The time complexity remains O(n), where n is the length of the string, as we still process each character exactly once.
 However, by reducing stack operations, the constant factors in the execution time may be improved.

 */
public class BasicCalculatorII {
    public boolean isDigit(char currentChar) {
        return '0' <= currentChar && currentChar <= '9';
    }

    public int calculate(String s) {
        int result = 0;
        int currentNumber = 0;
        int lastNumber = 0;
        char operation = '+';

        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);

            if (isDigit(currentChar)) {
                currentNumber = currentNumber * 10 + (currentChar - '0');
            }

            if (!isDigit(currentChar) && currentChar != ' ' || i == s.length() - 1) {
                if (operation == '+' || operation == '-') {
                    result += lastNumber; // Add the last number to the result
                    lastNumber = (operation == '+') ? currentNumber : -currentNumber;
                } else if (operation == '*') {
                    lastNumber = lastNumber * currentNumber;
                } else if (operation == '/') {
                    lastNumber = lastNumber / currentNumber;
                }
                operation = currentChar;
                currentNumber = 0;
            }
        }

        result += lastNumber; // Add the last number after the loop ends
        return result;
    }

    public static void main(String[] args) {
        BasicCalculatorII basicCalculatorII = new BasicCalculatorII();
        System.out.println(basicCalculatorII.calculate("3+2*2")); // Output: 7
        System.out.println(basicCalculatorII.calculate(" 3/2 ")); // Output: 1
        System.out.println(basicCalculatorII.calculate(" 3+5 / 2 ")); // Output: 5
    }
}
