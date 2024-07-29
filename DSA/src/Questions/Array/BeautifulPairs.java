package Questions.Array;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*

https://leetcode.com/problems/beautiful-pairs/description/
You are given two 0-indexed integer arrays nums1 and nums2 of the same length. A pair of indices (i,j) is called beautiful if|nums1[i] - nums1[j]| + |nums2[i] - nums2[j]| is the smallest amongst all possible indices pairs where i < j.

Return the beautiful pair. In the case that there are multiple beautiful pairs, return the lexicographically smallest pair.

Note that

|x| denotes the absolute value of x.
A pair of indices (i1, j1) is lexicographically smaller than (i2, j2) if i1 < i2 or i1 == i2 and j1 < j2.

Example 1:

Input: nums1 = [1,2,3,2,4], nums2 = [2,3,1,2,3]
Output: [0,3]
Explanation: Consider index 0 and index 3. The value of |nums1[i]-nums1[j]| + |nums2[i]-nums2[j]| is 1, which is the smallest value we can achieve.
Example 2:

Input: nums1 = [1,2,4,3,2,5], nums2 = [1,4,2,3,5,1]
Output: [1,4]
Explanation: Consider index 1 and index 4. The value of |nums1[i]-nums1[j]| + |nums2[i]-nums2[j]| is 1, which is the smallest value we can achieve.
 

Constraints:

2 <= nums1.length, nums2.length <= 105
nums1.length == nums2.length
0 <= nums1i <= nums1.length
0 <= nums2i <= nums2.length
Time Complexity: O(NlogN)
Space Complexity: O(N)
 */
public class BeautifulPairs {
    private List<int[]> points = new ArrayList<>();

    // Main method to find the beautiful pair of indices
    public int[] beautifulPair(int[] nums1, int[] nums2) {
        int n = nums1.length;
        // Map to group indices based on a unique key generated from nums1 and nums2
        // values
        Map<Long, List<Integer>> pl = new HashMap<>();

        // Populate the map with unique keys and corresponding indices
        for (int i = 0; i < n; ++i) {
            long z = f(nums1[i], nums2[i]);
            pl.computeIfAbsent(z, k -> new ArrayList<>()).add(i);
        }

        // Check if any key has more than one index
        for (int i = 0; i < n; ++i) {
            long z = f(nums1[i], nums2[i]);
            if (pl.get(z).size() > 1) {
                return new int[] { i, pl.get(z).get(1) };
            }
            points.add(new int[] { nums1[i], nums2[i], i });
        }

        // Sort points based on the first element (nums1 value)
        points.sort((a, b) -> a[0] - b[0]);

        // Perform a divide and conquer search to find the beautiful pair
        int[] ans = dfs(0, points.size() - 1);
        return new int[] { ans[1], ans[2] };
    }

    // Helper method to generate a unique key from nums1 and nums2 values
    private long f(int x, int y) {
        return x * 100000L + y;
    }

    // Calculate Manhattan distance between two points
    private int dist(int x1, int y1, int x2, int y2) {
        return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    }

    // Divide and conquer method to find the beautiful pair
    private int[] dfs(int l, int r) {
        // Base case: If only one element, return a large distance (infinity)
        if (l >= r) {
            return new int[] { 1 << 30, -1, -1 };
        }

        int m = (l + r) >> 1;
        int x = points.get(m)[0];

        // Recursive calls for left and right halves
        int[] t1 = dfs(l, m);
        int[] t2 = dfs(m + 1, r);

        // Choose the pair with the smaller distance
        if (t1[0] > t2[0] || (t1[0] == t2[0] && (t1[1] > t2[1] || (t1[1] == t2[1] && t1[2] > t2[2])))) {
            t1 = t2;
        }

        List<int[]> t = new ArrayList<>();

        // Collect points that are within the current best distance
        for (int i = l; i <= r; ++i) {
            if (Math.abs(points.get(i)[0] - x) <= t1[0]) {
                t.add(points.get(i));
            }
        }

        // Sort the collected points based on the second element (nums2 value)
        t.sort((a, b) -> a[1] - b[1]);

        // Check pairs within the collected points to find the smallest distance
        for (int i = 0; i < t.size(); ++i) {
            for (int j = i + 1; j < t.size(); ++j) {
                if (t.get(j)[1] - t.get(i)[1] > t1[0]) {
                    break;
                }
                int pi = Math.min(t.get(i)[2], t.get(j)[2]);
                int pj = Math.max(t.get(i)[2], t.get(j)[2]);
                int d = dist(t.get(i)[0], t.get(i)[1], t.get(j)[0], t.get(j)[1]);
                if (d < t1[0] || (d == t1[0] && (pi < t1[1] || (pi == t1[1] && pj < t1[2])))) {
                    t1 = new int[] { d, pi, pj };
                }
            }
        }
        return t1;
    }
    public static void main(String[] args) {
        BeautifulPairs beautifulPairs = new BeautifulPairs();
        int[] nums1 = {1, 2, 3, 2, 4};
        int[] nums2 = {2, 3, 1, 2, 3};
        int[] result = beautifulPairs.beautifulPair(nums1, nums2);
        System.out.println(result[0] + " " + result[1]);
    }
}
