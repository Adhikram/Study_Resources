package Questions.BinaryTree;

public class SerializeDeserialize {

    // Encodes a tree to a single string.
    public static String serialize(TreeNode root) {
        if (root == null)
            return "#";
        return root.val + " " + serialize(root.left) + " " + serialize(root.right);
    }

    // Decodes your encoded data to tree.
    public static TreeNode deserialize(String data) {
        String[] arr = data.split(" ");
        int[] index = {0}; // Reset the index before deserialization starts
        return helper(arr, index);
    }

    private static TreeNode helper(String[] arr, int[] index) {
        if (index[0] >= arr.length || arr[index[0]].equals("#")) {
            index[0]++; // Increment the index when encountering "#" or reaching the end of array
            return null;
        }

        TreeNode root = new TreeNode(Integer.valueOf(arr[index[0]]));
        index[0]++; // Move to the next element in the array
        root.left = helper(arr,index);
        root.right = helper(arr, index);
        return root;
    }

    public static void print(TreeNode root) {
        if(root == null){
            System.out.println("#");
            return;
        }
        System.out.println(root.val);
        print(root.left);
        print(root.right);
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
        print(deserialized);

    }
}
