package Questions.String;

import java.util.Collections;
import java.util.Set;
import java.util.TreeSet;

/*
https://leetcode.com/problems/next-closest-time/description/
 Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

 

Example 1:

Input: time = "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: time = "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
 

Constraints:

time.length == 5
time is a valid time in the form "HH:MM".
0 <= HH < 24
0 <= MM < 60
Time Complexity: 𝑂(4)
Space Complexity: 𝑂(1)
 */
public class NextClosestTime {
    public String nextClosestTime(String time) {
        // Set to store unique digits in sorted order
        Set<Character> sorted = new TreeSet<>();
        for (char c : time.toCharArray()) {
            if (c != ':') {
                sorted.add(c); // Insert digits into the set
            }
        }
        StringBuilder res = new StringBuilder(time); // Initialize result as the current time
        for (int i = time.length() - 1; i >= 0; i--) { // Iterate from the end of the time string
            if (time.charAt(i) == ':')
                continue; // Skip the colon

            Character current = time.charAt(i);
            // Find the next larger digit
            if (current != Collections.max(sorted)) {
                for (Character next : sorted) {
                    if (next > current) {
                        res.setCharAt(i, next); // Update the result with the next larger digit
                        // Check if the new time is valid
                        if ((i >= 3 && Integer.parseInt(res.substring(3, 5)) < 60) ||
                                (i < 2 && Integer.parseInt(res.substring(0, 2)) < 24)) {
                            return res.toString(); // Return the result if valid
                        }
                    }
                }
            }
            // If no larger digit was found, replace with the smallest digit
            res.setCharAt(i, Collections.min(sorted));
        }

        return res.toString(); // Return the modified time string

    }
    public static void main(String[] args) {
        NextClosestTime nextClosestTime = new NextClosestTime();
        String time = "19:34";
        System.out.println(nextClosestTime.nextClosestTime(time));
    }
}
