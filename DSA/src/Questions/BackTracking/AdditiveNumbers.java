package Questions.BackTracking;
/*
https://leetcode.com/problems/additive-number/
 An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

Example 1:

Input: "112358"
Output: true
Explanation: 
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation:
The additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199


Constraints:

1 <= num.length <= 35
num consists only of digits.


Follow up: How would you handle overflow for very large input integers?
Time Complexity: O(n^3)
Space Complexity: O(1)


Base Case for Recursion
if (cur >= num.length()): If the current index is beyond the length of the string, check if at least three numbers have been used.
If so, return true. This ensures that the sequence has at least three numbers.

if (num.charAt(cur) == '0' && number1 + number2 != 0):
If the current character is '0' and the sum of the last two numbers is not zero, return false to avoid invalid sequences with leading zeros.

Loop for Generating Numbers
The loop inside the solve function generates the next number in the sequence by iterating through the remaining part of the string.
for (int i = cur; i < num.length(); i++):
number = number * 10 + num.charAt(i) - '0': Construct the next number by appending the current digit.
if (number == target && solve(number2, target, i + 1, num, count + 1)): If the constructed number matches the target (sum of the previous two numbers), recursively check the next part of the string.
else if (number > target): If the constructed number exceeds the target, break the loop as further digits will only increase the number.
 */
public class AdditiveNumbers {
    public boolean isAdditiveNumber(String num) {
        long number1 = 0;
        for (int i = 0; i < num.length() - 1; i++) {
            number1 = number1 * 10 + num.charAt(i) - '0';
            long number2 = 0;
            for (int j = i + 1; j < num.length(); j++) {
                number2 = number2 * 10 + num.charAt(j) - '0';
                if (solve(number1, number2, j + 1, num, 2))
                    return true;
                if (number2 == 0)
                    break;
            }
            if (number1 == 0)
                break;
        }
        return false;
    }

    boolean solve(long number1, long number2, int cur, String num, int count) {
        if (cur >= num.length()) {
            if (count >= 3)
                return true;
            return false;
        }
        if (num.charAt(cur) == '0' && number1 + number2 != 0)
            return false;

        long number = 0;
        long target = number1 + number2;
        for (int i = cur; i < num.length(); i++) {
            number = number * 10 + num.charAt(i) - '0';
            if (number == target && solve(number2, target, i + 1, num, count + 1))
                return true;
            else if (number > target)
                break;
        }
        return false;
    }
    public static void main(String[] args) {
        AdditiveNumbers additiveNumbers = new AdditiveNumbers();
        System.out.println(additiveNumbers.isAdditiveNumber("112358"));
        System.out.println(additiveNumbers.isAdditiveNumber("199100199"));
    }
}
