package Questions.BinaryTree;

import java.util.ArrayList;
import java.util.List;

/*
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
Explanation:
findDistance Function:

This function serves a dual purpose.
It recursively finds the distance from the current node to the target node while simultaneously calculating the distance
to all nodes that are k steps away.
If the target node is found in the left or right subtree, it checks the other subtree or the parent node for nodes at the required distance.
collectNodesAtDistance Function:

This function is a simple DFS that collects all nodes at a given distance from the current node.
Optimization Points:

Space Efficiency: This approach avoids the need for an explicit parent map and instead leverages the DFS call stack, which reduces space complexity.
Single Pass: The tree is traversed once, and all relevant nodes are identified in one go, making it more efficient than separate DFS and BFS passes.
Time Complexity:
O(N): The tree is traversed once, where N is the number of nodes in the tree.
Space Complexity:
O(H): Space is needed for the recursion stack, where H is the height of the tree. This is better than O(N) space in the previous implementation that required a parent map.









 */
public class AllNodesAtKDistance {
    List<Integer> result = new ArrayList<>();

    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        findDistance(root, target, k);
        return result;
    }

    // Helper method to find the distance from the target node
    private int findDistance(TreeNode node, TreeNode target, int k) {
        if (node == null)
            return -1;

        if (node == target) {
            collectNodesAtDistance(node, k);
            return 0;
        }

        int leftDistance = findDistance(node.left, target, k);
        if (leftDistance != -1) {
            if (leftDistance + 1 == k) {
                result.add(node.val);
            } else {
                // Collect nodes at distance k - leftDistance - 2 from the right subtree
                collectNodesAtDistance(node.right, k - leftDistance - 2);
            }
            // Return the distance to the target node
            return leftDistance + 1;
        }

        int rightDistance = findDistance(node.right, target, k);
        if (rightDistance != -1) {
            if (rightDistance + 1 == k) {
                // Add the current node to the result
                result.add(node.val);
            } else {
                // Collect nodes at distance k - rightDistance - 2 from the left subtree
                collectNodesAtDistance(node.left, k - rightDistance - 2);
            }
            // Return the distance to the target node
            return rightDistance + 1;
        }

        return -1;
    }

    // Collect nodes that are exactly at the given distance
    private void collectNodesAtDistance(TreeNode node, int distance) {
        if (node == null || distance < 0)
            return;
        if (distance == 0) {
            result.add(node.val);
            return;
        }
        collectNodesAtDistance(node.left, distance - 1);
        collectNodesAtDistance(node.right, distance - 1);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(5);
        root.right = new TreeNode(1);
        root.left.left = new TreeNode(6);
        root.left.right = new TreeNode(2);
        root.right.left = new TreeNode(0);
        root.right.right = new TreeNode(8);
        root.left.right.left = new TreeNode(7);
        root.left.right.right = new TreeNode(4);

        AllNodesAtKDistance allNodesAtKDistance = new AllNodesAtKDistance();
        System.out.println(allNodesAtKDistance.distanceK(root, root.left, 2)); // Output: [7, 4, 1]
    }

}
