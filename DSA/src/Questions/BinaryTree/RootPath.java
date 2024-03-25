package Questions.BinaryTree;

import java.util.ArrayList;

public class RootPath {
    static boolean getPath(TreeNode root, ArrayList<Integer> arr, int x) {
        // if root is NULL
        // there is no path
        if (root == null)
            return false;

        // push the Treenode's value in 'arr'
        arr.add(root.val);

        // if it is the required Treenode
        // return true
        if (root.val == x)
            return true;

        // else check whether the required Treenode lies
        // in the left subtree or right subtree of
        // the current Treenode
        if (getPath(root.left, arr, x) ||
                getPath(root.right, arr, x))
            return true;

        // required Treenode does not lie either in the
        // left or right subtree of the current Treenode
        // Thus, remove current Treenode's value from
        // 'arr'and then return false
        arr.remove(arr.size() - 1);
        return false;
    }

    public static void main(String args[]) {

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.left.right.left = new TreeNode(6);
        root.left.right.right = new TreeNode(7);
        root.right = new TreeNode(3);

        ArrayList<Integer> arr = new ArrayList<>();

        boolean res;
        res = getPath(root, arr, 7);

        System.out.print("The path is ");
        for (int it : arr) {
            System.out.print(it + " ");
        }

    }
}
