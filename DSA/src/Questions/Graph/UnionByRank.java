package Questions.Graph;
import java.util.*;

public class UnionByRank {

    List<Integer> rank = new ArrayList<>();
    List<Integer> parent = new ArrayList<>();
    public UnionByRank(int n) {
        for (int i = 0; i <= n; i++) {
            rank.add(0);
            parent.add(i);
        }
    }

    public int findUPar(int node) {
        if (node == parent.get(node)) {
            return node;
        }
        int ulp = findUPar(parent.get(node));
        parent.set(node, ulp);
        return parent.get(node);
    }

    public void unionByRank(int u, int v) {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);
        if (ulp_u == ulp_v) return;
        if (rank.get(ulp_u) < rank.get(ulp_v)) {
            parent.set(ulp_u, ulp_v);
        } else if (rank.get(ulp_v) < rank.get(ulp_u)) {
            parent.set(ulp_v, ulp_u);
        } else {
            parent.set(ulp_v, ulp_u);
            int rankU = rank.get(ulp_u);
            rank.set(ulp_u, rankU + 1);
        }
    }
    // Precomputing the parent of each node time complexity: O(n)
    // Time complexity: O(log(n))
    // Space complexity: O(n)
    // n = number of nodes

    public static void main(String[] args) {
        int n = 5;
        UnionByRank u = new UnionByRank(n);
        u.unionByRank(1, 2);
        u.unionByRank(2, 3);
        u.unionByRank(4, 5);
        u.unionByRank(1, 4);
        System.out.println(u.findUPar(1));
        System.out.println(u.findUPar(2));
        System.out.println(u.findUPar(3));
        System.out.println(u.findUPar(4));
        System.out.println(u.findUPar(5));
    }
}
