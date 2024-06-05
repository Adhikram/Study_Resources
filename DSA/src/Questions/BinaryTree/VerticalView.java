package Questions.BinaryTree;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class VerticalView {
    public static class Pair<K, V> {
        private final K key;
        private final V value;

        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }
    }

    public List<List<Integer>> verticalTraversal(TreeNode root) {
        HashMap<Integer, List<Integer>> hash = new HashMap<>();
        Queue<Pair<TreeNode, Integer>> q = new LinkedList<>();
        Pair<TreeNode, Integer> temp = new Pair<TreeNode, Integer>(root, 0);
        q.add(temp);
        int index = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            // Need Level hash to get the Level's data
            HashMap<Integer, List<Integer>> lvlHash = new HashMap<>();
            for (int i = 0; i < size; i++) {
                temp = q.poll();
                TreeNode currNode = temp.getKey();
                Integer currLevel = temp.getValue();
                index = Math.max(index, Math.abs(currLevel));
                // System.out.println( "currNode: " + currNode.val + " currLevel: " +
                // currLevel);
                if (!lvlHash.containsKey(currLevel)) {
                    lvlHash.put(currLevel, new ArrayList<>());
                }
                lvlHash.get(currLevel).add(currNode.val);

                if (currNode.left != null)
                    q.add(new Pair<TreeNode, Integer>(currNode.left, currLevel - 1));
                if (currNode.right != null)
                    q.add(new Pair<TreeNode, Integer>(currNode.right, currLevel + 1));
            }
            // Storing the sorted lvl Hash data in Hash
            lvlHash.forEach((k, v) -> {
                Collections.sort(v);
                if (!hash.containsKey(k)) {
                    hash.put(k, v);
                } else {
                    hash.get(k).addAll(v);
                }
            });
            // System.out.println("hash: " + hash);
            // System.out.println("q: " + q);
        }
        List<List<Integer>> result = new ArrayList<>();
        for (int i = -index; i <= index; i++) {
            if (hash.containsKey(i)) {
                result.add(hash.get(i));
            }

        }

        return result;

    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        TreeNode right = new TreeNode(2);
        TreeNode rightLeft = new TreeNode(3);
        root.right = right;
        right.left = rightLeft;
        VerticalView verticalView = new VerticalView();
        List<List<Integer>> result = verticalView.verticalTraversal(root);
        System.out.println("Vertical View: " + result);
    }
}
