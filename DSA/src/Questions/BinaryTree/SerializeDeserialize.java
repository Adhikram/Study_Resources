package Questions.BinaryTree;

public class SerializeDeserialize {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

    private int index; // Index to keep track of the position in the array during deserialization

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null)
            return "#";
        return root.val + " " + serialize(root.left) + " " + serialize(root.right);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] arr = data.split(" ");
        index = 0; // Reset the index before deserialization starts
        return helper(arr);
    }

    private TreeNode helper(String[] arr) {
        if (index >= arr.length || arr[index].equals("#")) {
            index++; // Increment the index when encountering "#" or reaching the end of array
            return null;
        }

        TreeNode root = new TreeNode(Integer.valueOf(arr[index]));
        index++; // Move to the next element in the array
        root.left = helper(arr);
        root.right = helper(arr);
        return root;
    }

    public static void main(String[] args) {
        SerializeDeserialize serializeDeserialize = new SerializeDeserialize();
        TreeNode root = serializeDeserialize.new TreeNode(1);
        root.left = serializeDeserialize.new TreeNode(2);
        root.right = serializeDeserialize.new TreeNode(3);
        root.right.left = serializeDeserialize.new TreeNode(4);
        root.right.right = serializeDeserialize.new TreeNode(5);

        String serialized = serializeDeserialize.serialize(root);
        System.out.println(serialized);
        TreeNode deserialized = serializeDeserialize.deserialize(serialized);
        System.out.println(deserialized.val);
        
    }
}
