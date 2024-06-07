package OldInterviews;

public class MaxDistance {
    public int maxDistance(int[] heights, int bricks, int ladders) {
        int n = heights.length;
        // Initialize 3D DP array with dimensions (n) x (bricks+1) x (ladders+1)
        boolean[][][] dp = new boolean[n][bricks + 1][ladders + 1];

        // Base case: starting position is always reachable
        for (int b = 0; b <= bricks; b++) {
            for (int l = 0; l <= ladders; l++) {
                dp[0][b][l] = true;
            }
        }
        int result = 0;

        // Iterate over each index
        for (int i = 1; i < n; i++) {
            for (int b = 0; b <= bricks; b++) {
                for (int l = 0; l <= ladders; l++) {
                    // Check if we can reach index i from index i-1
                    if (dp[i-1][b][l]) {
                        // Case 1: No need for bricks or ladders if moving to a lower or equal height
                        if (heights[i] <= heights[i-1]) {
                            dp[i][b][l] = true;
                        }
                        // Case 2: Use bricks to bridge the gap if we have enough bricks
                        else if (heights[i] > heights[i-1] && b > 0) {
                            int diff = heights[i] - heights[i-1];
                            if (b >= diff) {
                                dp[i][b - diff][l] = true;
                            }
                        }
                        // Case 3: Use a ladder if available
                        if (heights[i] > heights[i-1] && l > 0) {
                            dp[i][b][l - 1] = true;
                        }
                    }

                }
            }
        }

        // Find the maximum reachable index
        for (int i = n - 1; i >= 0; i--) {
            for (int b = 0; b <= bricks; b++) {
                for (int l = 0; l <= ladders; l++) {
                    if (dp[i][b][l]) {
                        return i;
                    }
                }
            }
        }

        return 0;  // In case no index is reachable, return 0
    }

    public static void main(String[] args) {
        MaxDistance solution = new MaxDistance();
        int[] heights = {4, 6, 2, 7, 9, 3, 14, 6, 12};
        int bricks = 10;
        int ladders = 2;
        System.out.println(solution.maxDistance(heights, bricks, ladders));  // Output will be the maximum distance reachable
    }
}

