package Questions.Graph.PathDecisions;

public class FloydWarshall {
    public void shortestDistance(int[][] matrix) {
        int n = matrix.length;

        // Initialize matrix: replace -1 with a large value and set diagonal to 0
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == -1) {
                    matrix[i][j] = Integer.MAX_VALUE;
                }
                if (i == j) {
                    matrix[i][j] = 0;
                }
            }
        }

        // Floyd-Warshall algorithm for finding shortest distances
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    // Update shortest distance if going through vertex k is shorter
                    if (matrix[i][k] != Integer.MAX_VALUE && matrix[k][j] != Integer.MAX_VALUE) {
                        matrix[i][j] = Math.min(matrix[i][j], matrix[i][k] + matrix[k][j]);
                    }
                }
            }
        }

        // Restore original representation: replace large values with -1
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == Integer.MAX_VALUE) {
                    matrix[i][j] = -1;
                }
            }
        }
    }

    public static void main(String[] args) {
        // Example usage
        int[][] matrix = {
                { 0, 5, -1, 10 },
                { -1, 0, 3, -1 },
                { -1, -1, 0, 1 },
                { -1, -1, -1, 0 }
        };

        FloydWarshall fw = new FloydWarshall();
        fw.shortestDistance(matrix);

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
