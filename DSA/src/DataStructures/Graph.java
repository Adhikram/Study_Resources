package DataStructures;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// Class Structure
public class Graph {
    public static void main(String[] args) {
        // Signature
        Map<Integer, List<Integer>> graph = new HashMap<>();

        // Add Vertex
        graph.put(1, new ArrayList<>());

        // Add Edge
        graph.get(1).add(2);

        // Remove Vertex
        graph.remove(1);

        // Remove Edge
        graph.get(1).remove(Integer.valueOf(2));
    }
}
