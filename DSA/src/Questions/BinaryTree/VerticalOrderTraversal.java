package Questions.BinaryTree;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

import Questions.BinaryTree.VerticalView.Pair;

/*
https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
 Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

 */
public class VerticalOrderTraversal {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        // A map to store the nodes in each vertical column
        Map<Integer, List<Integer>> columnTable = new HashMap<>();
        // A queue for BFS
        Queue<Pair<TreeNode, Integer>> queue = new LinkedList<>();
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        // Initialize the queue with the root node and its column index (0)
        queue.offer(new Pair<>(root, 0));

        // Perform BFS
        while (!queue.isEmpty()) {
            Pair<TreeNode, Integer> pair = queue.poll();
            TreeNode node = pair.getKey();
            int column = pair.getValue();

            // If the node is not null, process it
            if (node != null) {
                min = Math.min(column, min);
                max = Math.max(column, max);
                // Add the node's value to the corresponding column in the map
                columnTable.putIfAbsent(column, new ArrayList<>());
                columnTable.get(column).add(node.val);

                // Add the left child to the queue with column index - 1
                queue.offer(new Pair<>(node.left, column - 1));
                // Add the right child to the queue with column index + 1
                queue.offer(new Pair<>(node.right, column + 1));
            }
        }

        // Build the result list
        List<List<Integer>> result = new ArrayList<>();
        for (int i = min; i <= max; i++) {
            if (columnTable.containsKey(i)) {
                result.add(columnTable.get(i));
            }

        }

        return result;

    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        TreeNode right = new TreeNode(20);
        TreeNode rightLeft = new TreeNode(15);
        TreeNode rightRight = new TreeNode(7);
        root.right = right;
        right.left = rightLeft;
        right.right = rightRight;
        VerticalOrderTraversal verticalOrderTraversal = new VerticalOrderTraversal();
        System.out.println(verticalOrderTraversal.verticalOrder(root));
    }
}
