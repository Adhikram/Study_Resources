package Questions.BST;

public class BSTFromPreOrder {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }

    }
    public TreeNode helper(int[] preOrder, int start, int end){
        if(start > end) return null;
        TreeNode root = new TreeNode(preOrder[start]);
        int i = start + 1;
        while(i <= end && preOrder[i] < root.val){
            i++;
        }
        root.left = helper(preOrder, start + 1, i - 1);
        root.right= helper(preOrder, i, end);
        return root;
    }
    public TreeNode bstFromPreorder(int[] preOrder) {
        return helper(preOrder, 0, preOrder.length -1);
    }
    public static void main(String[] args) {
        BSTFromPreOrder bstFromPreOrder = new BSTFromPreOrder();
        int[] preOrder = {8,5,1,7,10,12};
        TreeNode result = bstFromPreOrder.bstFromPreorder(preOrder);
        System.out.println("Result: " + result.val);
    }
}