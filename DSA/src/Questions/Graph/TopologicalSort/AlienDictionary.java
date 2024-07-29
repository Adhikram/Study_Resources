package Questions.Graph.TopologicalSort;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
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
    public  String alienOrder(String[] words) {
        if(words.length==0)
            return "";
        Map<Character,Integer>inDegree=new HashMap<>();
        Map<Character,List<Character>>graph=new HashMap<>();
		//a. Initialise adjacency list and in degree map
        for (String word : words) {
            for (char character : word.toCharArray()) {
                inDegree.put(character, 0);
                graph.put(character, new ArrayList<Character>());
            }
        }
        for(int i=0;i<words.length-1;i++){
            String w1 = words[i], w2 = words[i + 1];
            //Checks if str1 starts wtih str2
            if (w1.length() > w2.length() && w1 .startsWith(w2)) {
                return "";
            }
			//b. Build the graph and in degree map
            for (int j = 0; j < Math.min(w1.length(), w2.length()); j++) {
                char parent = w1.charAt(j), child = w2.charAt(j);
                if (parent != child) { // if the two characters are different
                  graph.get(parent).add(child); // put the child into it's parent's list
                  inDegree.put(child, inDegree.get(child) + 1); // increment child's inDegree
                  break; // only the first different character between the two words will help us find the order
                }
            }
        }
            // c. Find all sources i.e., all vertices with 0 in-degrees
            Queue<Character> sources = new LinkedList<>();
            for (Map.Entry<Character, Integer> entry : inDegree.entrySet()) {
              if (entry.getValue() == 0)
                sources.add(entry.getKey());
            }
        // d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
        // if a child's in-degree becomes zero, add it to the sources queue
        StringBuilder sortedOrder = new StringBuilder();
        while (!sources.isEmpty()) {
          Character vertex = sources.poll();
          sortedOrder.append(vertex);
          List<Character> children = graph.get(vertex); // get the node's children to decrement their in-degrees
          for (Character child : children) {
            inDegree.put(child, inDegree.get(child) - 1);
            if (inDegree.get(child) == 0)
              sources.add(child);
          }
        }

        // if sortedOrder doesn't contain all characters, there is a cyclic dependency between characters, therefore, we
        // will not be able to find the correct ordering of the characters
        if (sortedOrder.length() != inDegree.size())
          return "";

        return sortedOrder.toString();
    }

}
