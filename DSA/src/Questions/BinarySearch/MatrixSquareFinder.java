package Questions.BinarySearch;

public class MatrixSquareFinder {

    // Method to find the first and last occurrences of 1s
    public static int[][] findSquareOccurrences(int[][] matrix) {
        int m = matrix.length; // Number of rows
        int n = matrix[0].length; // Number of columns

        int firstRow = -1, firstCol = -1;
        int lastRow = -1, lastCol = -1;

        // Perform binary search to find the first occurrence of 1
        int low = 0, high = m * n - 1;

        // Find the first occurrence of 1
        while (low <= high) {
            int mid = (low + high) / 2;
            int row = mid / n; // Get row index
            int col = mid % n; // Get column index

            if (matrix[row][col] == 1) {
                firstRow = row;
                firstCol = col;
                high = mid - 1; // Search left for the first occurrence
            } else {
                low = mid + 1; // Search right
            }
        }

        // Reset low and high for last occurrence search
        low = 0;
        high = m * n - 1;

        // Find the last occurrence of 1
        while (low <= high) {
            int mid = (low + high) / 2;
            int row = mid / n; // Get row index
            int col = mid % n; // Get column index

            if (matrix[row][col] == 1) {
                lastRow = row;
                lastCol = col;
                low = mid + 1; // Search right for the last occurrence
            } else {
                high = mid - 1; // Search left
            }
        }

        return new int[][] { { firstRow, firstCol }, { lastRow, lastCol } };
    }

    public static void main(String[] args) {
        int[][] matrix = {
                { 0, 0, 0, 0 },
                { 0, 1, 1, 0 },
                { 0, 1, 1, 0 },
                { 0, 0, 0, 0 }
        };

        int[][] result = findSquareOccurrences(matrix);
        System.out.println("First occurrence of square of 1s: (" + result[0][0] + ", " + result[0][1] + ")");
        System.out.println("Last occurrence of square of 1s: (" + result[1][0] + ", " + result[1][1] + ")");
    }
}
