package Questions.LinkedList;
/*
 Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
 

Constraints:

1 <= capacity <= 104
0 <= key <= 105
0 <= value <= 109
At most 2 * 105 calls will be made to get and put.
 

Time Complexity: O(1) for both get and put operations
Space Complexity: O(capacity) where capacity is the maximum number of elements in the cache
 */
class LFUCache {
    // Node class to represent elements in the cache
    public class Node {
        int data;   // Value associated with the key
        int count;  // Frequency of key access
        int key;    // Key of the node
        Node left;  // Pointer to the previous node in the linked list
        Node right; // Pointer to the next node in the linked list

        // Constructor to initialize the node with a key and its associated data
        public Node(int key, int data) {
            this.key = key;
            this.data = data;
            count = 1;  // Initialize the access count to 1
        }
    }

    Node keyMap[];               // Array to store key to node mapping
    Node countMap[] = new Node[10005]; // Array to store frequency to node mapping
    Node head;                   // Dummy node representing the head of the linked list
    Node tail;                   // Dummy node representing the tail of the linked list
    int capacity;                // Maximum capacity of the cache
    int currentSize;             // Current number of elements in the cache

    // Constructor to initialize the LFUCache with a given capacity
    public LFUCache(int capacity) {
        keyMap = new Node[100005];  // Initialize the keyMap with a large enough size
        head = new Node(-1, -1);    // Initialize head as a dummy node
        tail = new Node(0, 1);      // Initialize tail as a dummy node
        this.capacity = capacity;   // Set the cache capacity
        currentSize = 0;            // Initialize the current size to 0
        head.right = tail;          // Connect head to tail
        tail.left = head;           // Connect tail to head
        countMap[1] = tail;         // Initialize countMap for frequency 1 to point to tail
    }

    // Get the value associated with the key from the cache
    public int get(int key) {
        if (keyMap[key] == null)
            return -1;  // Return -1 if the key is not found in the cache

        Node node = keyMap[key];
        shiftNode(node, node.data); // Increment frequency and adjust position in the linked list

        return node.data;  // Return the value associated with the key
    }

    // Put or update the key-value pair in the cache
    public void put(int key, int value) {
        if (keyMap[key] != null) {
            shiftNode(keyMap[key], value); // Update frequency and adjust position
            return;
        }

        if (currentSize == capacity) {
            deleteNode(tail.left.key, tail.left); // Evict least frequently used key
            addNode(key, value); // Add the new key-value pair
            return;
        }

        addNode(key, value);  // Add the new key-value pair if capacity is not reached
        currentSize++;        // Increment the current size of the cache
    }

    // Delete the node corresponding to the given key
    public void deleteNode(int key, Node node) {
        int count = node.count;

        // Update the countMap for the current frequency
        if (countMap[count] == node) {
            countMap[count] = null;
        }

        if (countMap[1] == null)
            countMap[1] = tail;

        // Remove the node from the linked list
        node.left.right = node.right;
        node.right.left = node.left;

        keyMap[key] = null;  // Remove the key from the keyMap
    }

    // Add a new node to the cache
    public void addNode(int key, int value) {
        Node node = new Node(key, value); // Create a new node

        Node refNode = countMap[1]; // Get the reference node for frequency 1
        countMap[1] = node;         // Update the countMap for frequency 1

        // Insert the new node before the reference node in the linked list
        refNode.left.right = node;
        node.left = refNode.left;
        node.right = refNode;
        refNode.left = node;

        keyMap[key] = node;  // Update the keyMap with the new node
    }

    // Adjust the frequency and position of the node in the linked list
    public void shiftNode(Node node, int value) {
        node.count++;        // Increment the access count of the node
        int count = node.count;
        node.data = value;   // Update the data of the node
        Node prevNode = node.right; // Get the next node in the linked list
        Node refNode;

        // Get the reference node for the new frequency
        if (countMap[count] == null)
            refNode = countMap[count - 1];
        else
            refNode = countMap[count];

        // Re-position the node in the linked list if necessary
        if (refNode != node) {
            node.left.right = node.right;
            node.right.left = node.left;
            node.left = refNode.left;
            node.right = refNode;
            refNode.left.right = node;
            refNode.left = node;
        }

        // Update the countMap for the previous frequency if necessary
        if (countMap[count - 1] == node) {
            if (prevNode.count == count - 1) {
                countMap[prevNode.count] = prevNode;
            } else {
                countMap[count - 1] = null;
            }
        }

        countMap[count] = node; // Update the countMap for the current frequency
    }
    public static void main(String[] args) {
        LFUCache cache = new LFUCache(2);
        cache.put(1, 1);
        cache.put(2, 2);
        System.out.println(cache.get(1)); // returns 1
        cache.put(3, 3); // evicts key 2
        System.out.println(cache.get(2)); // returns -1 (not found)
        System.out.println(cache.get(3)); // returns 3
        cache.put(4, 4); // evicts key 1
        System.out.println(cache.get(1)); // returns -1 (not found)
        System.out.println(cache.get(3)); // returns 3
        System.out.println(cache.get(4)); // returns 4
    }
}
