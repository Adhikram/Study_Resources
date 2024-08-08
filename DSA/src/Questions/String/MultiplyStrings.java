package Questions.String;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/*
https://leetcode.com/problems/multiply-strings/description/
 Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
Time Complexity: O(M*N)
Space Complexity: O(M + N + 1)
 */
public class MultiplyStrings {
    public static String multiply(String num1, String num2) {
        if ("0".equals(num1) || "0".equals(num2)) {
            return "0";
        }
        int m = num1.length(), n = num2.length();
        List<Integer> res = new ArrayList<>(Collections.nCopies(
                m + n, 0)); // Initialize the result list with zeros

        // Reverse iterate through num1 and num2
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int mul = (num1.charAt(i) - '0') *
                        (num2.charAt(j) - '0'); // Multiply digits
                int p1 = i + j, p2 = i + j + 1; // Position in the result list
                int sum = mul + res.get(p2); // Add to the current position

                res.set(p1, res.get(p1) + sum / 10); // Carry
                res.set(p2, sum % 10); // Remainder
            }
        }

        // Build the result string
        StringBuilder sb = new StringBuilder();
        for (int p : res) {
            if (!(sb.length() == 0 && p == 0)) { // Skip leading zeros
                sb.append(p);
            }
        }

        return sb.length() == 0
                ? "0"
                : sb.toString(); // Return result or "0" if empty
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(multiply("123", "456")); // Expected output: "56088"
    }
}
