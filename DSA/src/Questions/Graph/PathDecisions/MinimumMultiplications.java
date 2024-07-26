package Questions.Graph.PathDecisions;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;


public class MinimumMultiplications {
    static class Pair {
        int first;
        int second;

        public Pair(int first, int second) {
            this.first = first;
            this.second = second;
        }
    }
    public int minimumMultiplications(int[] arr, int start, int end) {
        // Create a queue for storing pairs of numbers (number, steps)
        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(start, 0));

        // Create an array to store the number of multiplications to reach a particular
        // number
        int[] dist = new int[100000];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        int mod = 100000;
        int n = arr.length;

        // Perform Breadth-First Search (BFS)
        while (!queue.isEmpty()) {
            int node = queue.peek().first;
            int steps = queue.peek().second;
            queue.poll();

            // Multiply the current node with each number in the array
            for (int i = 0; i < n; i++) {
                int num = (arr[i] * node) % mod;

                // If the number of multiplications is less than before to reach a number,
                // update the dist array and add the number to the queue for further exploration
                if (steps + 1 < dist[num]) {
                    dist[num] = steps + 1;

                    // If the target number is reached, return the calculated steps
                    if (num == end)
                        return dist[num];

                    queue.offer(new Pair(num, dist[num]));
                }
            }
        }

        // If the target number is unattainable
        return -1;
    }

    // Time complexity: O(n * log(end)), where n is the number of elements in the array
    // Space complexity: O(n)
    public static void main(String[] args) {
        // Example usage
        int[] arr = { 2, 3, 5 }; // Array of numbers
        int start = 2; // Start number
        int end = 100; // End number

        MinimumMultiplications mm = new MinimumMultiplications();
        int minSteps = mm.minimumMultiplications(arr, start, end);

        // Print the minimum number of multiplications to reach the end number
        System.out.println("Minimum number of multiplications: " + minSteps);
    }
}
