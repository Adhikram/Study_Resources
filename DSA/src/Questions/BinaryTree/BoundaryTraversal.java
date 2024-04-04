package Questions.BinaryTree;

import java.util.ArrayList;

public class BoundaryTraversal {
    // Method to check if a node is a leaf node
    static Boolean isLeaf(TreeNode root) {
        return (root.left == null) && (root.right == null);
    }

    // Method to add the left boundary of the binary tree to the result
    static void addLeftBoundary(TreeNode root, ArrayList<Integer> res) {
        TreeNode cur = root.left;
        while (cur != null) {
            // If the current node is not a leaf node, add its value to the result
            if (isLeaf(cur) == false)
                res.add(cur.val);
            // Move to the left child if it exists, otherwise move to the right child
            if (cur.left != null)
                cur = cur.left;
            else
                cur = cur.right;
        }
    }

    // Method to add the right boundary of the binary tree to the result
    static void addRightBoundary(TreeNode root, ArrayList<Integer> res) {
        TreeNode cur = root.right;
        ArrayList<Integer> tmp = new ArrayList<Integer>();
        while (cur != null) {
            // If the current node is not a leaf node, add its value to a temporary list
            if (isLeaf(cur) == false)
                tmp.add(cur.val);
            // Move to the right child if it exists, otherwise move to the left child
            if (cur.right != null)
                cur = cur.right;
            else
                cur = cur.left;
        }
        // Add the values in the temporary list to the result in reverse order
        for (int i = tmp.size() - 1; i >= 0; --i) {
            res.add(tmp.get(i));
        }
    }

    // Method to add the leaf nodes of the binary tree to the result
    static void addLeaves(TreeNode root, ArrayList<Integer> res) {
        // If the current node is a leaf node, add its value to the result
        if (isLeaf(root)) {
            res.add(root.val);
            return;
        }
        // Recursively add the leaf nodes in the left and right subtrees
        if (root.left != null)
            addLeaves(root.left, res);
        if (root.right != null)
            addLeaves(root.right, res);
    }

    static void addAllInOne(TreeNode root, ArrayList<Integer> leaves, ArrayList<Integer> left, ArrayList<Integer> right) {
        if (root == null)
            return;
        if (isLeaf(root)) {
            leaves.add(root.val);
            return;
        }
        if (root.left != null)
            addAllInOne(root.left, leaves, left, right);
        if (root.right != null)
            addAllInOne(root.right, leaves, left, right);
        if (root != null && !isLeaf(root)) {
            if (root.left != null)
                right.add(root.val);
            else
                left.add(0, root.val);
        }
    }

    // Method to print the boundary of the binary tree
    static ArrayList<Integer> printBoundary(TreeNode node) {
        ArrayList<Integer> ans = new ArrayList<Integer>();
        // If the root node is not a leaf node, add its value to the result
        if (isLeaf(node) == false)
            ans.add(node.val);
        // Add the left boundary, the leaf nodes, and the right boundary to the result
        addLeftBoundary(node, ans);
        addLeaves(node, ans);
        addRightBoundary(node, ans);
        // Return the result
        return ans;
    }


    public static void main(String[] args) {
        // Create a binary tree
        TreeNode root = new TreeNode(1);
        TreeNode right = new TreeNode(2);
        TreeNode rightLeft = new TreeNode(3);
        TreeNode rightRight = new TreeNode(4);
        TreeNode rightRightLeft = new TreeNode(5);
        TreeNode rightRightRight = new TreeNode(6);
        root.right = right;
        right.left = rightLeft;
        right.right = rightRight;
        rightRight.left = rightRightLeft;
        rightRight.right = rightRightRight;
        // Print the boundary of the binary tree
        ArrayList<Integer> result = printBoundary(root);
        System.out.println("Boundary Traversal: " + result);
        ArrayList<Integer> leaves = new ArrayList<>();
        ArrayList<Integer> left = new ArrayList<>();
        ArrayList<Integer> rightList = new ArrayList<>();
        addAllInOne(root, leaves, left, rightList);
        System.out.println("Boundary Traversal: " + left + leaves + rightList);
    }
}