package Questions.StackQueue;

import java.util.HashMap;
import java.util.Stack;

public class NextGreaterElement {
    public static int[] solve(int[] nums1, int[] nums2) {
        Stack<Integer> st = new Stack<>();
        HashMap<Integer, Integer> hash = new HashMap<>();
        st.push(-1);
        for (int i = nums2.length - 1; i > -1; i--) {
            while (st.peek() != -1 && st.peek() < nums2[i]) {
                st.pop();
            }
            hash.put(nums2[i], st.peek());
            st.push(nums2[i]);
        }

        for (int i = 0; i < nums1.length; i++) {
            nums1[i] = hash.getOrDefault(nums1[i], -1);
        }
        return nums1;
    }

    public static void main(String[] args) {
        int[] nums1 = { 4, 1, 2 };
        int[] nums2 = { 1, 3, 4, 2 };
        int[] res = solve(nums1, nums2);
        for (int i = 0; i < res.length; i++) {
            System.out.print(res[i] + " ");
        }
    }
}
