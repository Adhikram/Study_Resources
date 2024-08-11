package Questions.BinaryTree;

/*
https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/
 Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.
 

Example 1:


Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.
Example 2:


Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
Explanation:
TreeNode Class: This is a standard implementation of a binary tree node.
Solution Class:
averageOfSubtree(TreeNode root): This method initializes the postorder traversal and returns the count of nodes satisfying the condition.
postOrder(TreeNode node): This recursive helper method does a postorder traversal of the tree. For each node, it computes the sum of the values and the number of nodes in its subtree and checks if the node's value is equal to the average of its subtree.
The method postOrder returns an array with two elements: the first element is the sum of values in the subtree, and the second element is the number of nodes in the subtree.
Complexity:
Time Complexity: O(n), where
n is the number of nodes in the tree. Each node is visited exactly once.
Space Complexity: 
O(h), where h is the height of the tree. This is the space used by the recursion stack.
 */
public class CountOfAverageSubtree {
    public int averageOfSubtree(TreeNode root) {
        int[] count = new int[] { 0 };
        postOrder(root, count);
        return count[0];
    }

    private int[] postOrder(TreeNode node, int[] count) {
        if (node == null)
            return new int[] { 0, 0 }; // {sum, number of nodes}

        // Post-order traversal
        int[] left = postOrder(node.left, count);
        int[] right = postOrder(node.right, count);

        // Calculate current subtree's sum and number of nodes
        int sum = left[0] + right[0] + node.val;
        int numNodes = left[1] + right[1] + 1;

        // Check if the current node's value equals the average of its subtree
        if (node.val == sum / numNodes) {
            count[0]++;
        }

        return new int[] { sum, numNodes };
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(8);
        root.right = new TreeNode(5);
        root.left.left = new TreeNode(0);
        root.left.right = new TreeNode(1);
        root.right.right = new TreeNode(6);

        CountOfAverageSubtree countOfAverageSubtree = new CountOfAverageSubtree();
        System.out.println(countOfAverageSubtree.averageOfSubtree(root)); // 5
    }
}
