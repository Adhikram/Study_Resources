package Questions.Matrix;

/*
https://leetcode.com/problems/search-a-2d-matrix-ii/description/
 Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109
Time Complexity: O(m + n)
Space Complexity: O(1)
 */
public class SearchIn2DMatrixII {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }

        int m = matrix.length; // number of rows
        int n = matrix[0].length; // number of columns
        int row = 0; // start from the first row
        int col = n - 1; // start from the last column

        while (row < m && col >= 0) {
            int current = matrix[row][col];
            if (current == target) {
                return true; // target found
            } else if (current > target) {
                col--; // move left
            } else {
                row++; // move down
            }
        }
        return false; // target not found
    }

    public static void main(String[] args) {
        SearchIn2DMatrixII obj = new SearchIn2DMatrixII();
        int[][] matrix = {
                { 1, 4, 7, 11, 15 },
                { 2, 5, 8, 12, 19 },
                { 3, 6, 9, 16, 22 },
                { 10, 13, 14, 17, 24 },
                { 18, 21, 23, 26, 30 }
        };
        System.out.println(obj.searchMatrix(matrix, 5)); // Output: true

        System.out.println(obj.searchMatrix(matrix, 20)); // Output: false
    }
}
