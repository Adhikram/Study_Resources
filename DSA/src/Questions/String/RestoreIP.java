package Questions.String;

import java.util.ArrayList;
import java.util.List;
/*
 A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

1 <= s.length <= 20
s consists of digits only.
Time Complexity: For Backtracking O(3^4) = O(1)
Space Complexity: O(1)
 */
public class RestoreIP {
    public List<String> restoreIpAddressesOP(String s) {
        List<String> result = new ArrayList<>();
        backtrack(s, 0, 0, "", result);
        return result;
    }

    private void backtrack(String s, int start, int segmentCount, String currentIP, List<String> result) {
        // If we have 4 segments and we've used all characters in s, it's a valid IP address
        if (segmentCount == 4) {
            if (start == s.length()) {
                result.add(currentIP.substring(0, currentIP.length() - 1)); // Remove the trailing dot
            }
            return;
        }

        // Try segments of length 1, 2, and 3
        for (int len = 1; len <= 3; len++) {
            if (start + len > s.length()) break; // Out of bounds

            String segment = s.substring(start, start + len);
            if (isValidSegment(segment)) {
                // Include the segment and move to the next part of the string
                backtrack(s, start + len, segmentCount + 1, currentIP + segment + ".", result);
            }
        }
    }

    private boolean isValidSegment(String segment) {
        // Check if the segment is valid
        if (segment.length() > 1 && segment.charAt(0) == '0') {
            return false; // Leading zero not allowed
        }
        int num = Integer.parseInt(segment);
        return num >= 0 && num <= 255; // Valid range
    }
    List<String> ans;
    public List<String> restoreIpAddresses(String s) {
        ans = new ArrayList<>();
        ip(s, 0, 0, new int[4], s.length());
        return ans;
    }

    private void ip(String s, int start, int dots, int[] segments, int n){
        if(dots==4) {
            if (start == n) {
                StringBuilder str = new StringBuilder();
                for (int i = 0; i < 4; i++) {
                    str.append(segments[i]);
                    if (i != 3) {
                        str.append(".");
                    }
                }
                ans.add(str.toString());
            }
            return;
        }
        if(start==n){
            return;
        }
        if(s.charAt(start)=='0'){
            segments[dots] = 0;
            ip(s, start + 1, dots + 1, segments, n);
        }
        int num = 0;
        for(int i=start; i<n; i++){
            num = num * 10 + (s.charAt(i) - '0');
            if(num > 0 && num < 256){
                segments[dots] = num;
                ip(s, i + 1, dots + 1, segments, n);
            }
            else{
                break;
            }
        }
    }
    public List<String> restoreIpAddresses1(String s) {
        List<String> ret = new ArrayList<>();

        StringBuffer ip = new StringBuffer();
        for (int a = 1; a < 4; ++a)
            for (int b = 1; b < 4; ++b)
                for (int c = 1; c < 4; ++c)
                    for (int d = 1; d < 4; ++d) {
                        if (a + b + c + d == s.length()) {
                            int n1 = Integer.parseInt(s.substring(0, a));
                            int n2 = Integer.parseInt(s.substring(a, a + b));
                            int n3 = Integer.parseInt(s.substring(a + b, a + b + c));
                            int n4 = Integer.parseInt(s.substring(a + b + c));
                            if (n1 <= 255 && n2 <= 255 && n3 <= 255 && n4 <= 255) {
                                ip.append(n1).append('.').append(n2)
                                        .append('.').append(n3).append('.').append(n4);
                                if (ip.length() == s.length() + 3)
                                    ret.add(ip.toString());
                                ip.delete(0, ip.length());
                            }
                        }
                    }
        return ret;
    }
    public static void main(String[] args) {
        RestoreIP restoreIP = new RestoreIP();
        System.out.println(restoreIP.restoreIpAddresses("25525511135"));
        System.out.println(restoreIP.restoreIpAddresses("0000"));
        System.out.println(restoreIP.restoreIpAddresses("101023"));
    }

}
