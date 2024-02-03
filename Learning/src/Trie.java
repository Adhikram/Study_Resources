import java.util.HashMap;
import java.util.Map;

// Class Structure
public class Trie {
    public static void main(String[] args) {
        // Signature
        TrieNode root = new TrieNode();

        // Insert
        insert(root, "hello");

        // Search
        boolean contains = search(root, "hello");
        System.out.println("Trie contains hello: " + contains);

        // Delete
        delete(root, "hello");
    }

    // TrieNode class
    static class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        boolean isEndOfWord;
    }

    // Helper methods for Trie
    static void insert(TrieNode root, String word) {
        TrieNode current = root;
        for (char ch : word.toCharArray()) {
            current.children.putIfAbsent(ch, new TrieNode());
            current = current.children.get(ch);
        }
        current.isEndOfWord = true;
    }

    static boolean search(TrieNode root, String word) {
        TrieNode current = root;
        for (char ch : word.toCharArray()) {
            current = current.children.get(ch);
            if (current == null) {
                return false;
            }
        }
        return current.isEndOfWord;
    }

    static void delete(TrieNode root, String word) {
        deleteRecursive(root, word, 0);
    }

    static boolean deleteRecursive(TrieNode current, String word, int index) {
        if (index == word.length()) {
            if (!current.isEndOfWord) {
                return false;
            }
            current.isEndOfWord = false;
            return current.children.isEmpty();
        }

        char ch = word.charAt(index);
        TrieNode nextNode = current.children.get(ch);
        if (nextNode == null) {
            return false;
        }

        boolean shouldDeleteCurrentNode = deleteRecursive(nextNode, word, index + 1);

        if (shouldDeleteCurrentNode) {
            current.children.remove(ch);
            return current.children.isEmpty();
        }

        return false;
    }
}
