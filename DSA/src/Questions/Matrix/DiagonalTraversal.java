package Questions.Matrix;

/*
https://leetcode.com/problems/diagonal-traverse/description/
 Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
Time Complexity: O(m * n)
Space Complexity: O(1)
 */
public class DiagonalTraversal {
    public int[] findDiagonalOrder(int[][] mat) {
        if (mat == null || mat.length == 0)
            return new int[0];

        int m = mat.length;
        int n = mat[0].length;
        int[] result = new int[m * n];
        int r = 0, c = 0, d = 1;

        for (int i = 0; i < m * n; i++) {
            result[i] = mat[r][c];
            // Move up-right
            if (d == 1) {
                if (c == n - 1) {
                    r++;
                    d = -1;
                } else if (r == 0) {
                    c++;
                    d = -1;
                } else {
                    r--;
                    c++;
                }
            }
            // Move down-left
            else {
                if (r == m - 1) {
                    c++;
                    d = 1;
                } else if (c == 0) {
                    r++;
                    d = 1;
                } else {
                    r++;
                    c--;
                }
            }
        }

        return result;
    }
    public static void main(String[] args) {
        DiagonalTraversal diagonalTraversal = new DiagonalTraversal();
        int[][] mat = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int[] result = diagonalTraversal.findDiagonalOrder(mat);
        for (int i : result) {
            System.out.print(i + " ");
        }
    }
}
