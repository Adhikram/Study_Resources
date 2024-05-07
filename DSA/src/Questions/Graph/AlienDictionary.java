package Questions.Graph;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class AlienDictionary {
    private List<Integer> topologicalSort(int V, List<List<Integer>> adj) {
        // Counting in-degree of each node
        int[] inDegree = new int[V];
        for (List<Integer> edges : adj) {
            for (int it : edges) {
                inDegree[it]++;
            }
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < V; i++) {
            if (inDegree[i] == 0) {
                queue.add(i);
            }
        }

        List<Integer> topologicalOrder = new ArrayList<>();
        while (!queue.isEmpty()) {
            int node = queue.poll();
            topologicalOrder.add(node);

            for (int it : adj.get(node)) {
                if (--inDegree[it] == 0) {
                    queue.add(it);
                }
            }
        }

        return topologicalOrder;
    }

    public String findOrder(String[] dict, int N, int K) {
        // Creating adjacency list
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < K; i++) {
            adj.add(new ArrayList<>());
        }

        // Updating adjacency list
        for (int i = 0; i < N - 1; i++) {
            String s1 = dict[i];
            String s2 = dict[i + 1];
            int len = Math.min(s1.length(), s2.length());
            for (int ptr = 0; ptr < len; ptr++) {
                if (s1.charAt(ptr) != s2.charAt(ptr)) {
                    adj.get(s1.charAt(ptr) - 'a').add(s2.charAt(ptr) - 'a');
                    break;
                }
            }
        }

        List<Integer> topologicalOrder = topologicalSort(K, adj);

        StringBuilder result = new StringBuilder();
        for (int it : topologicalOrder) {
            result.append((char) (it + 'a'));
        }

        return result.toString();
    }

    // Time Complexity: O(N + K)
    // Space Complexity: O(N + K)

    public static void main(String[] args) {
        int N = 5, K = 4;
        String[] dict = { "baa", "abcd", "abca", "cab", "cad" };
        AlienDictionary obj = new AlienDictionary();
        String ans = obj.findOrder(dict, N, K);

        System.out.println(ans);
    }

}
