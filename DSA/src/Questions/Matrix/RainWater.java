package Questions.Matrix;

import java.util.ArrayList;
import java.util.List;

public class RainWater {
    int delRow[] = { 1, -1, 0, 0 };
    int delCol[] = { 0, 0, 1, -1 };

    public List<List<Integer>> pacificAtlantic(int[][] heights) {

        int n = heights.length;
        int m = heights[0].length;

        int pacific[][] = new int[n][m];
        int atlantic[][] = new int[n][m];

        for (int i = 0; i < n; i++) {
            dfs(i, 0, heights, pacific, Integer.MIN_VALUE);// first col
            dfs(i, m - 1, heights, atlantic, Integer.MIN_VALUE);// last col
        }

        for (int j = 0; j < m; j++) {
            dfs(0, j, heights, pacific, Integer.MIN_VALUE);// first row
            dfs(n - 1, j, heights, atlantic, Integer.MIN_VALUE);// last row
        }

        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (pacific[i][j] == 1 && atlantic[i][j] == 1) {
                    List<Integer> res = new ArrayList<>();
                    res.add(i);
                    res.add(j);
                    ans.add(res);
                }
            }
        }

        return ans;

    }

    public void dfs(int i, int j, int[][] heights, int[][] visit, int height) {
        int n = heights.length;
        int m = heights[0].length;
        if (i < 0 || i >= n || j < 0 || j >= m || visit[i][j] == 1 || heights[i][j] < height)
            return;

        visit[i][j] = 1;

        for (int k = 0; k < 4; k++) {
            int nrow = i + delRow[k];
            int ncol = j + delCol[k];

            dfs(nrow, ncol, heights, visit, heights[i][j]);

        }
    }
    public static void main(String[] args) {
        RainWater rainWater = new RainWater();
        int[][] heights = new int[][]{
                {1, 2, 2, 3, 5},
                {3, 2, 3, 4, 4},
                {2, 4, 5, 3, 1},
                {6, 7, 1, 4, 5},
                {5, 1, 1, 2, 4}
        };
        System.out.println(rainWater.pacificAtlantic(heights));
    }
}
