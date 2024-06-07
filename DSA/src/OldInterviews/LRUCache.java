package OldInterviews;

import java.util.HashMap;

public class LRUCache {
    static class Node {
        Node prev;
        Node next;
        int key, value;

        Node(int _key, int _value) {
            key = _key;
            value = _value;
        }
    }

    Node head = new Node(-1, -1);
    Node tail = new Node(-1, -1);
    HashMap<Integer, Node> store = new HashMap<>();
    int capacity = 0;

    public LRUCache(int _cap) {
        capacity = _cap;
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        if (store.containsKey(key)) {
            Node currNode = store.get(key);
            remove(currNode);
            insert(key, currNode.value);
            return currNode.value;
        }
        return 0;
    }

    public void put(int key, int value) {
        if (store.containsKey(key)) {
            remove(store.get(key));
        }
//        System.out.println(store.size());
//        store.forEach((k,v) -> System.out.println("Key " + k + "val " + value));
        if (store.size() == capacity) {
            Node leastData = tail.prev;
            remove(leastData);
        }
        insert(key, value);
    }


    private void remove(Node curr) {
        store.remove(curr.key);
        curr.next.prev = curr.prev;
        curr.prev.next = curr.next;
    }

    private void insert(int key, int value) {
        Node curr = new Node(key, value);
        store.put(key, curr);
        curr.next = head.next;
        curr.next.prev = curr;
        head.next = curr;
        curr.prev = head;
    }


//   head -> 3 -> 2 -> 1 -> <- tail

//    get (1)
//        remover -> 1


    public static void main(String[] args) {

        LRUCache lru = new LRUCache(3);
        lru.put(1, 1);
        lru.put(2, 2);
        lru.put(3, 3);
        System.out.println("Getting data " + lru.get(1));
        lru.put(4, 4);
        System.out.println("Getting data " + lru.get(2));

    }

}




