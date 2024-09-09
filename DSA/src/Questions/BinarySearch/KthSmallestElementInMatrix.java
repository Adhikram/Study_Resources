package Questions.BinarySearch;

/*
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
 Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
 Time Complexity: O(n * log(max - min))
    Space Complexity: O(1)


    low = matrix[0][0]
    high = matrix[n - 1][n - 1]
    while low < high:
        mid = (low + high) // 2
        count = countLessEqual(matrix, mid, n)
        if count < k:
            low = mid + 1
        else:
            high = mid
    return low

    countLessEqual(matrix, target, n):
        count = 0
        row = n - 1
        col = 0
        while row >= 0 and col < n:
            if matrix[row][col] <= target:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count

 */
public class KthSmallestElementInMatrix {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        int low = matrix[0][0];
        int high = matrix[n - 1][n - 1];

        while (low < high) {
            int mid = (high + low) >> 1;
            int count = countLessEqual(matrix, mid, n);

            if (count < k) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }

        return low;
    }

    private int countLessEqual(int[][] matrix, int target, int n) {
        int count = 0;
        int row = n - 1;
        int col = 0;

        while (row >= 0 && col < n) {
            if (matrix[row][col] <= target) {
                count += (row + 1);
                col++;
            } else {
                row--;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        KthSmallestElementInMatrix obj = new KthSmallestElementInMatrix();
        int[][] matrix = {
                { 1, 5, 9 },
                { 10, 11, 13 },
                { 12, 13, 15 }
        };
        int k = 8;
        System.out.println(obj.kthSmallest(matrix, k)); // Output: 13
    }

}
