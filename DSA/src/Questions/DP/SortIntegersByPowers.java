package Questions.DP;

import java.util.Arrays;

public class SortIntegersByPowers {
    static int dp[] = new int[1000000];

    public int getKth(int low, int high, int k) {
        int[][] ans = new int[(high - low) + 1][2];
        int i = 0;
        while (low <= high) {
            ans[i][0] = low;
            ans[i][1] = power(low);
            i++;
            low++;
        }
        Arrays.sort(ans, (a, b) -> a[1] - b[1]);
        // System.out.println(Arrays.toString(dp));
        // System.out.println(Arrays.toString(ans));
        return ans[k - 1][0];
    }

    public int power(int x) {
        if (x == 1 || x == 0) {
            return 0;
        }
        if (dp[x] != 0) {
            return dp[x];
        }
        if (x % 2 == 0) {
            dp[x] = 1 + power(x / 2);
        } else {
            dp[x] = 1 + power((x * 3) + 1);
        }
        return dp[x];
    }

    public static void main(String[] args) {
        SortIntegersByPowers s = new SortIntegersByPowers();
        System.out.println(s.getKth(12, 15, 2));
    }
}
