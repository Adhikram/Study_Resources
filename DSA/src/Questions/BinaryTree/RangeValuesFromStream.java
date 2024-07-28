package Questions.BinaryTree;

import java.util.ArrayList;
import java.util.List;

/*
 Q: There is stream of float values (-inf, inf) which is coming as input and an integer D.

We need to find a set of 3 values which satisfy condition - |a - b| <= D, |b - c| <= D, |a - c| <= D, assuming a,b,c are 3 float values. Print these 3 values and remove them and continue ....

Constraints -
All values in stream will be unique.
D -> [0, inf)

Eg:
Input stream - [1,10,7,-2,8,....], d = 5
Output - (when 8 comes, then print "7 8 10" and remove them and continue)
Time complexity should be less than O(n^2)
Space complexity should be less than O(n)
 */

public class RangeValuesFromStream {
    private class TreeNode {
        float key;
        TreeNode left, right;

        TreeNode(float item) {
            key = item;
            left = right = null;
        }
    }

    private int D;
    private TreeNode root;
    private List<Float> answer;

    // Initialize the class with the given D
    public RangeValuesFromStream(int d) {
        this.D = d;
        this.root = null;
    }

    // Process each incoming item from the stream
    void func(float item) {
        this.answer = new ArrayList<>();
        this.answer.add(item);

        explore(this.root, item);
        if (this.answer.size() == 3) {
            for (float a : this.answer) {
                System.out.println(a);
                this.root = deleteNode(this.root, a);
            }
        } else {
            this.root = insert(this.root, item);
        }
    }

    // Explore the BST to find values within the range
    private void explore(TreeNode node, float item) {
        if (node == null || this.answer.size() == 3) return;

        if (Math.abs(item - node.key) <= this.D) {
            this.answer.add(node.key);
        }

        if (item < node.key) {
            explore(node.left, item);
        } else {
            explore(node.right, item);
        }
    }

    // Insert a new key into the BST
    private TreeNode insert(TreeNode root, float key) {
        if (root == null) {
            root = new TreeNode(key);
            return root;
        }
        if (key < root.key) {
            root.left = insert(root.left, key);
        } else if (key > root.key) {
            root.right = insert(root.right, key);
        }
        return root;
    }

    // Delete a key from the BST
    private TreeNode deleteNode(TreeNode root, float key) {
        if (root == null) return root;

        if (key < root.key) {
            root.left = deleteNode(root.left, key);
        } else if (key > root.key) {
            root.right = deleteNode(root.right, key);
        } else {
            if (root.left == null)
                return root.right;
            else if (root.right == null)
                return root.left;

            root.key = minValue(root.right);
            root.right = deleteNode(root.right, root.key);
        }

        return root;
    }

    private float minValue(TreeNode root) {
        float minv = root.key;
        while (root.left != null) {
            minv = root.left.key;
            root = root.left;
        }
        return minv;
    }
    public void inorder(TreeNode root) {
        if (root != null) {
            inorder(root.left);
            System.out.print(root.key + " ");
            inorder(root.right);
        }
    }

    public static void main(String[] args) {
        RangeValuesFromStream solution = new RangeValuesFromStream(5);

        // Take a bigger stream and check the output
        float[] stream2 = {1, 10, 7, -2, 8, 9, 6, 5, 4, 3, 2, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 29};

        for (float item : stream2) {
            solution.func(item);
            System.out.println("Item: " + item);
            System.out.println("Inorder: ");
            solution.inorder(solution.root);
            System.out.println();
        }
        // solution.inorder(solution.root);

    }
}
