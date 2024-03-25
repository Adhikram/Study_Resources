package Questions.BinaryTree;

public class SerializeDeserialize {
    private static int index; // Index to keep track of the position in the array during deserialization

    // Encodes a tree to a single string.
    public static String serialize(TreeNode root) {
        if (root == null)
            return "#";
        return root.val + " " + serialize(root.left) + " " + serialize(root.right);
    }

    // Decodes your encoded data to tree.
    public static TreeNode deserialize(String data) {
        String[] arr = data.split(" ");
        index = 0; // Reset the index before deserialization starts
        return helper(arr);
    }

    private static TreeNode helper(String[] arr) {
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
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.right.left = new TreeNode(4);
        root.right.right = new TreeNode(5);

        String serialized = serialize(root);
        System.out.println(serialized);
        TreeNode deserialized = deserialize(serialized);
        System.out.println(deserialized.val);

    }
}
