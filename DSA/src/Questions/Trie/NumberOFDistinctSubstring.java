package Questions.Trie;

public class NumberOFDistinctSubstring{
    static class Node {
        Node[] links = new Node[26]; // Trie node links

        boolean containsKey(char ch) {
            return (links[ch - 'a'] != null);
        }

        Node get(char ch) {
            return links[ch - 'a'];
        }

        void put(char ch, Node node) {
            links[ch - 'a'] = node;
        }

        // Function to insert a string into the trie
        void insert(String s) {
            Node node = this;
            // Traverse the trie, inserting characters of the string
            for (int i = 0; i < s.length(); i++) {
                char currentChar = s.charAt(i);
                // If the character is not present, create a new node
                if (!node.containsKey(currentChar)) {
                    node.put(currentChar, new Node());
                }
                // Move to the next node
                node = node.get(currentChar);
            }
        }
    }

    // Function to count the number of distinct substrings
    public static int countDistinctSubstrings(String s) {
        Node root = new Node(); // Create a trie root node
        int n = s.length();
        int count = 0;

        // Iterate through each character in the string
        for (int i = 0; i < n; i++) {
            Node node = root;

            // Iterate through each substring starting from index i
            for (int j = i; j < n; j++) {
                // If the current character is not present in the trie, insert it and increment
                // count
                if (!node.containsKey(s.charAt(j))) {
                    node.put(s.charAt(j), new Node());
                    count++;
                }
                // Move to the next node
                node = node.get(s.charAt(j));
            }
        }
        // Return the count of distinct substrings (add 1 for the empty string)
        return count + 1;
    }

    public static void main(String[] args) {
        String s1 = "ababa";
        System.out.println("Total number of distinct substrings for s1: " +
                countDistinctSubstrings(s1));

        String s2 = "ccfdf";
        System.out.println("Total number of distinct substrings for s2: " +
                countDistinctSubstrings(s2));
    }
}
