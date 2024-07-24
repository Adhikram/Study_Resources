package Questions.String;

/*
https://leetcode.com/problems/reverse-integer/description/?envType=company&envId=google&favoriteSlug=google-thirty-days&difficulty=EASY%2CMEDIUM
 * Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

Constraints:

-231 <= x <= 231 - 1
 */
public class ReverseInteger {
    public int reverse(int x) {
        int result = 0;

        while (x != 0) {
            int carry = x % 10;
            x = x / 10;

            // Check for overflow/underflow before updating result
            if (result > Integer.MAX_VALUE / 10) {
                return 0;
            }
            if (result < Integer.MIN_VALUE / 10) {
                return 0;
            }

            result = result * 10 + carry;
        }

        return result;
    }

    public static void main(String[] args) {
        ReverseInteger obj = new ReverseInteger();
        int x = 123;
        System.out.println(obj.reverse(x));
        System.out.println(obj.reverse(-123));
        System.out.println(obj.reverse(120));

    }

}
