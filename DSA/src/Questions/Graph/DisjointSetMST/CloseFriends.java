package Questions.Graph.DisjointSetMST;

import java.util.Arrays;

public class CloseFriends {
    public int earliestAcq(int[][] logs, int n) {
        Arrays.sort(logs, (a, b) -> a[0] - b[0]);
        UnionFind uf = new UnionFind(n);
        for (int[] log : logs) {
            uf.union(log[1], log[2]);
            if (uf.numSets() == 1) {
                return log[0];
            }
        }
        return -1;
    }

    class UnionFind {
        private int[] parent;
        private int numSets;

        public UnionFind(int n) {
            numSets = n;
            parent = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
        }

        public int find(int u) {
            int x = u;
            while (x != parent[x]) {
                x = parent[x];
            }
            parent[u] = x;
            return x;
        }

        public int numSets() {
            return numSets;
        }

        public void union(int u, int v) {
            if (u != v) {
                int a = find(u);
                int b = find(v);
                if (a != b) {
                    parent[b] = a;
                    numSets--;
                }
                parent[u] = a;
                parent[v] = a;
            }
        }

    }
    public static void main(String[] args) {
        CloseFriends obj = new CloseFriends();
        int[][] logs = { { 2000, 0, 1 }, { 2000, 2, 3 }, { 100, 0, 3 }, { 2000, 1, 2 } };
        int n = 4;
        System.out.println(obj.earliestAcq(logs, n));
    }
}
