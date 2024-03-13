package Questions.StackQueue;

import java.util.Stack;

public class CalculateExpression {
    public long resolve(long a, long b, char Operator) {
        if (Operator == '+')
            return a + b;
        else if (Operator == '-')
            return a - b;
        else if (Operator == '*')
            return a * b;
        else
            return a / b;
    }

    public int evalRPN(String[] tokens) {
        Stack<Long> s = new Stack<>();
        for (String token : tokens) {
            if (token.length() == 1 && token.charAt(0) < '0') {
                long integer2 = s.pop();
                long integer1 = s.pop();
                char operator = token.charAt(0);
                long result = resolve(integer1, integer2, operator);
                // System.out.println(result);
                s.push(result);
            } else {
                s.push(Long.parseLong(token));
            }
        }
        return s.pop().intValue();
    }
    public static void main(String[] args) {
        CalculateExpression calculateExpression = new CalculateExpression();
        String[] tokens = {"2", "1", "+", "3", "*"};
        int result = calculateExpression.evalRPN(tokens);
        System.out.println("Result: " + result);
    }
}
