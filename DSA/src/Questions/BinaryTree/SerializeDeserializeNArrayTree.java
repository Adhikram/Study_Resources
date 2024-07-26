package Questions.BinaryTree;

import java.util.ArrayList;

/*
https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/description/
 Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree


 

as [1 [3[5 6] 2 4]]. Note that this is just an example, you do not necessarily need to follow this format.

Or you can follow LeetCode's level order traversal serialization format, where each group of children is separated by the null value.


 

For example, the above tree may be serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].

You do not necessarily need to follow the above-suggested formats, there are many more different formats that work so please be creative and come up with different approaches yourself.

 

Example 1:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Example 2:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
 */
public class SerializeDeserializeNArrayTree {
    public class Node {
        public int val;
        public ArrayList<Node> children;

        public Node() {
        }

        public Node(int val) {
            this.val = val;
        }

        public Node(int val, ArrayList<Node> children) {
            this.val = val;
            this.children = children;
        }
    }

    private void rserialize(Node root, StringBuilder sb) {
        if (root == null)
            return;
        sb.append((char) (root.val + '0'));
        for (Node child : root.children)
            rserialize(child, sb);
        sb.append('#');
    }

    // Encodes a tree to a single string.
    public String serialize(Node root) {
        StringBuilder sb = new StringBuilder();
        this.rserialize(root, sb);
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public Node deserialize(String data) {
        if (data.isEmpty())
            return null;
        return rdeserialize(data, new int[1]);
    }

    private Node rdeserialize(String data, int[] index) {
        if (index[0] == data.length())
            return null;
        Node node = new Node(data.charAt(index[0]) - '0', new ArrayList<Node>());
        index[0]++;
        while (data.charAt(index[0]) != '#')
            node.children.add(rdeserialize(data, index));
        index[0]++;
        return node;
    }

    public static void main(String[] args) {
        SerializeDeserializeNArrayTree serializeDeserializeNArrayTree = new SerializeDeserializeNArrayTree();
        Node root = serializeDeserializeNArrayTree.new Node(1, new ArrayList<>());
        Node child1 = serializeDeserializeNArrayTree.new Node(3, new ArrayList<>());
        Node child2 = serializeDeserializeNArrayTree.new Node(2, new ArrayList<>());
        Node child3 = serializeDeserializeNArrayTree.new Node(4, new ArrayList<>());
        root.children.add(child1);
        root.children.add(child2);
        root.children.add(child3);
        Node child4 = serializeDeserializeNArrayTree.new Node(5, new ArrayList<>());
        Node child5 = serializeDeserializeNArrayTree.new Node(6, new ArrayList<>());
        child1.children.add(child4);
        child1.children.add(child5);
        String serialized = serializeDeserializeNArrayTree.serialize(root);
        System.out.println(serialized);
        Node deserialized = serializeDeserializeNArrayTree.deserialize(serialized);
        System.out.println(deserialized.val);
    }
}
