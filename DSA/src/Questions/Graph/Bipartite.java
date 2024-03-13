package Questions.Graph;

import java.util.ArrayList;

public class Bipartite {
    private boolean dfs(int node, int col, int color[],
            ArrayList<ArrayList<Integer>> adj) {

        color[node] = col;

        // traverse adjacent nodes
        for (int it : adj.get(node)) {
            // if uncoloured
            if (color[it] == -1) {
                if (dfs(it, 1 - col, color, adj) == false)
                    return false;
            }
            // if previously coloured and have the same colour
            else if (color[it] == col) {
                return false;
            }
        }

        return true;
    }

    public boolean isBipartite(int V, ArrayList<ArrayList<Integer>> adj) {
        int color[] = new int[V];
        for (int i = 0; i < V; i++)
            color[i] = -1;

        // for connected components
        for (int i = 0; i < V; i++) {
            if (color[i] == -1) {
                if (dfs(i, 0, color, adj) == false)
                    return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int V = 4;
        ArrayList<ArrayList<Integer>> adj = new ArrayList<ArrayList<Integer>>(V);
        for (int i = 0; i < V; i++)
            adj.add(new ArrayList<Integer>());

        adj.get(0).add(1);
        adj.get(1).add(0);
        adj.get(1).add(2);
        adj.get(2).add(1);
        adj.get(2).add(3);
        adj.get(3).add(2);
        adj.get(3).add(0);
        adj.get(0).add(3);

        Bipartite bipartite = new Bipartite();
        boolean result = bipartite.isBipartite(V, adj);
        System.out.println("Is Bipartite: " + result);
    }
}
