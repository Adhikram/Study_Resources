package Questions.BinaryTree;

import java.util.LinkedList;
import java.util.Queue;

public class MaximumWidth {
    // Pair class to store a node and its id
    static class Pair {
        TreeNode node;
        int num;

        Pair(TreeNode _node, int _num) {
            num = _num;
            node = _node;
        }
    }

    // Method to find the maximum width of a binary tree
    public static int widthOfBinaryTree(TreeNode root) {
        // If the root is null, return 0
        if (root == null)
            return 0;
        int ans = 0;
        Queue<Pair> q = new LinkedList<>();
        // Add the root to the queue with id 0
        q.offer(new Pair(root, 0));
        while (!q.isEmpty()) {
            int size = q.size();
            // Get the id of the first node in the queue
            int first_id = q.peek().num;
            int first = 0, last = 0;
            for (int i = 0; i < size; i++) {
                // Get the id of the current node relative to the first node in the queue
                int cur_id = q.peek().num - first_id;
                TreeNode node = q.peek().node;
                q.poll();
                // If this is the first node in the current level, record its id
                if (i == 0)
                    first = cur_id;
                // If this is the last node in the current level, record its id
                if (i == size - 1)
                    last = cur_id;
                // If the left child exists, add it to the queue with id cur_id * 2 + 1
                if (node.left != null)
                    q.offer(new Pair(node.left, cur_id * 2 + 1));
                // If the right child exists, add it to the queue with id cur_id * 2 + 2
                if (node.right != null)
                    q.offer(new Pair(node.right, cur_id * 2 + 2));
            }
            // Update the maximum width
            ans = Math.max(ans, last - first + 1);
        }
        // Return the maximum width
        return ans;
    }

    // Main method
    public static void main(String args[]) {

        // Create a binary tree
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(3);
        root.left.left = new TreeNode(5);
        root.left.left.left = new TreeNode(7);
        root.right = new TreeNode(2);
        root.right.right = new TreeNode(4);
        root.right.right.right = new TreeNode(6);

        // Find the maximum width of the binary tree
        int maxWidth = widthOfBinaryTree(root);
        System.out.println("The maximum width of the Binary Tree is " + maxWidth);

    }
}