package Questions.Array;

import java.util.Arrays;

public class GridPath {
    public static int uniquePaths(int n, int m) {
        int[][] grid = new int[n][m];
        Arrays.stream(grid).forEach(row -> Arrays.fill(row, 1));

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1];
            }
        }

        return grid[n - 1][m - 1];
    }

    public static int uniquePathsOptimized(int n, int m) {
        int[] prev = new int[m];
        int[] cur = new int[m];
        Arrays.fill(prev, 1);
        Arrays.fill(cur, 1);

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                cur[j] = prev[j] + cur[j - 1];
            }
            prev = cur;
        }

        return cur[m - 1];

    }

    public static void main(String[] args) {
        System.out.println(uniquePathsOptimized(3, 7));
        System.out.println(uniquePaths(3, 7));
    }
}
