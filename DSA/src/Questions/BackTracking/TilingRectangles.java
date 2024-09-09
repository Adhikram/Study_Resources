package Questions.BackTracking;

/*
https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/description/
 Given a rectangle of size n x m, return the minimum number of integer-sided squares that tile the rectangle.

 

Example 1:



Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)
Example 2:



Input: n = 5, m = 8
Output: 5
Example 3:



Input: n = 11, m = 13
Output: 6
 

Constraints:

1 <= n, m <= 13
Time Complexity: O(N^2)
Space Complexity: O(N^2)

Backtracking Approach:

Use a recursive function to explore all possible ways to tile the rectangle with squares.
For each uncovered cell, try placing the largest possible square and recursively tile the remaining uncovered area.
Use backtracking to restore the state after exploring each possibility.

Dynamic Programming Approach:

Use a 2D array dp where dp[i][j] represents the minimum number of squares needed to tile a rectangle of size i x j.
For each rectangle, try all possible splits and find the minimum number of squares needed.
 */
public class TilingRectangles {
    int ret; // store the final result
    int m, n; // m is the height, and n is the width

    // Note: original signature is changed from n,m to m,n
    public int tilingRectangle(int m, int n) {
        this.m = m;
        this.n = n;
        this.ret = m * n; // initialize the result as m*n if cut rectangle to be all 1*1 squares
        int[][] mat = new int[m][n]; // record the status of every location, 0 means not covered, 1 means covered
        backtrack(mat, 0); // start backtracking
        return ret;
    }

    // the size means how many squares cut now
    public void backtrack(int[][] mat, int size) {
        if (size > ret)
            return; // if we already have more squares than the min result, no need to go forward

        // find out the leftmost and topmost position where is not covered yet
        int x = -1, y = -1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    x = i;
                    y = j;
                    break;
                }
            }
            if (x != -1 && y != -1)
                break;
        }
        // if not found, we know that all positions are covered
        if (x == -1 && y == -1) {
            // update the result
            ret = Math.min(size, ret);
        } else {
            int len = findWidth(x, y, mat); // find the maximum width to cut the square
            while (len >= 1) {
                cover(x, y, len, mat, 1); // cover the current square
                backtrack(mat, size + 1);
                cover(x, y, len, mat, 0); // uncover the previous result
                len--; // decrement the square width by 1
            }
        }
    }

    public int findWidth(int x, int y, int[][] mat) {
        int len = 1;
        while (x + len < m && y + len < n) {
            boolean flag = true; // flag means the len is reachable
            for (int i = 0; i <= len; i++) {
                // check the right i-th column and the bottom i-th row away from (x, y)
                if (mat[x + i][y + len] == 1 || mat[x + len][y + i] == 1) {
                    flag = false;
                    break;
                }
            }
            if (!flag)
                break;
            len++;
        }
        return len;
    }

    public void cover(int x, int y, int len, int[][] mat, int val) {
        for (int i = x; i < x + len; i++) {
            for (int j = y; j < y + len; j++) {
                mat[i][j] = val;
            }
        }
    }

    public int tilingRectangleDP(int n, int m) {

        // if((n==11 && m==13) || (n==13 && m==11)){
        // return 6;
        // }

        int[][] dp = new int[n + 1][m + 1];

        // Loop through rows and columns
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (i == j) {
                    // If the rectangle is already a square, one square is needed
                    dp[i][j] = 1;
                } else {
                    // Initialize with maximum value
                    dp[i][j] = Integer.MAX_VALUE;
                    // Try all possible splits and find the minimum
                    for (int k = 1; k <= i / 2; k++) {
                        dp[i][j] = Math.min(dp[i][j], dp[i - k][j] + dp[k][j]);
                    }
                    for (int k = 1; k <= j / 2; k++) {
                        dp[i][j] = Math.min(dp[i][j], dp[i][j - k] + dp[i][k]);
                    }
                }
            }
        }
        return dp[n][m];
    }
    public static void main(String[] args) {
        TilingRectangles obj = new TilingRectangles();
        System.out.println(obj.tilingRectangle(2, 3)); // 3
        System.out.println(obj.tilingRectangle(5, 8)); // 5
        System.out.println(obj.tilingRectangle(11, 13)); // 6
    }
}
