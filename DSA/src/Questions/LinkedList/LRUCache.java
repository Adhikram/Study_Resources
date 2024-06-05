package Questions.LinkedList;

import java.util.HashMap;

public class LRUCache {
    Node head = new Node(0, 0), tail = new Node(0, 0);
    HashMap<Integer, Node> map = new HashMap<>();
    int capacity;

    public LRUCache(int _capacity) {
        capacity = _capacity;
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        if (map.containsKey(key)) {
            Node node = map.get(key);
            remove(node);
            insert(node);
            return node.value;
        } else {
            return -1;
        }
    }

    public void put(int key, int value) {
        if (map.containsKey(key)) {
            remove(map.get(key));
        }
        if (map.size() == capacity) {
            remove(tail.prev);
        }
        insert(new Node(key, value));
    }

    private void remove(Node node) {
        map.remove(node.key);
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void insert(Node node) {
        map.put(node.key, node);
        node.next = head.next;
        node.next.prev = node;
        head.next = node;
        node.prev = head;
    }

    static class Node {
        Node prev, next;
        int key, value;

        Node(int _key, int _value) {
            key = _key;
            value = _value;
        }
    }
    // Complexity Analysis
    // Time complexity: O(1) both for put and get since all operations with ordered
    // Space complexity: O(capacity) since the space is used only for a hashmap

    public static void main(String[] args) {
        LRUCache lRUCache = new LRUCache(2);
        lRUCache.put(1, 1); // cache is {1=1}
        lRUCache.put(2, 2); // cache is {1=1, 2=2}
        System.out.println("Value for key 1 after putting: " + lRUCache.get(1)); // Expected output: Value for key 1
                                                                                 // after putting: 1
        // System.out.println(lRUCache.get(1)); // Expected output: 1
        lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        System.out.println("Value for key 2 after putting: " + lRUCache.get(2)); // Expected output: Value for key 2
                                                                                 // after putting: -1
        lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        System.out.println("Value for key 1 after putting: " + lRUCache.get(1)); // Expected output: Value for key 1
                                                                                 // after putting: -1
        System.out.println("Value for key 3: " + lRUCache.get(3)); // Expected output: Value for key 3: 3
        System.out.println("Value for key 4: " + lRUCache.get(4)); // Expected output: Value for key 4: 4
    }

}
