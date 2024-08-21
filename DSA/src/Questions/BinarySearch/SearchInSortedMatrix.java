package Questions.BinarySearch;

public class SearchInSortedMatrix {
    public static boolean searchMatrix(int[][] matrix, int target) {
        int row = 0;
        int rowSize = matrix.length;
        int colSize = matrix[0].length;
        while (row < rowSize) {
            if (target <= matrix[row][colSize - 1] && target >= matrix[row][0]) {
                int start = 0;
                int end = colSize - 1;
                while (start <= end) {
                    int mid = (start + end) / 2;
                    if (matrix[row][mid] == target) {
                        return true;
                    }
                    if (matrix[row][mid] > target) {
                        end = mid - 1;
                    } else {
                        start = mid + 1;
                    }
                }
                return false;
            } else {
                row++;
            }
        }
        return false;
    }

    public static String solve(int[][] matrix, int target) {
        int row = 0;
        int col = matrix[0].length - 1;
        while (row < matrix.length && col > -1) {
            int cur = matrix[row][col];
            if (cur == target) {
                return "" + row + " " + col;
            }
            if (cur < target) {
                row++;
            } else {
                col--;
            }
        }

        return "Element not found";

    }

    public static void main(String[] args) {
        int[][] matrix = new int[][] { { 1, 3, 5, 7 }, { 10, 11, 16, 20 }, { 23, 30, 34, 60 } };
        System.out.println(searchMatrix(matrix, 3));
        System.out.println(solve(matrix, 3));
    }
}
