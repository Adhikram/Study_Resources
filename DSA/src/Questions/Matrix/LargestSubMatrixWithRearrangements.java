package Questions.Matrix;

import java.util.Arrays;
/*
https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/
 You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

 

Example 1:


Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.
Example 2:


Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.
Example 3:

Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m * n <= 105
matrix[i][j] is either 0 or 1.
Time Complexity: O(m * n * log(n))
Space Complexity: O(1)
 */
public class LargestSubMatrixWithRearrangements {
public int largestSubMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        // Calculate the height of 1s for each element
        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 1) {
                    matrix[i][j] += matrix[i - 1][j];
                }
            }
        }

        int maxArea = 0;

        // For each row, sort the heights and calculate the maximum area
        for (int i = 0; i < m; i++) {
            Arrays.sort(matrix[i]);
            for (int j = n - 1; j >= 0; j--) {
                int height = matrix[i][j];
                if (height == 0) break; // no need to calculate further
                int width = n - j;
                maxArea = Math.max(maxArea, height * width);
            }
        }

        return maxArea;
    }
    public static void main(String[] args) {
        LargestSubMatrixWithRearrangements largestSubMatrixWithRearrangements = new LargestSubMatrixWithRearrangements();
        int[][] matrix = {{0,0,1},{1,1,1},{1,0,1}};
        System.out.println(largestSubMatrixWithRearrangements.largestSubMatrix(matrix));
    }
}
