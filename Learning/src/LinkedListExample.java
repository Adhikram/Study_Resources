import java.util.LinkedList;
import java.util.ListIterator;

public class LinkedListExample {
    public static void main(String[] args) {
        LinkedList<Integer> linkedList = new LinkedList<>();

        // Insertion
        // Time Complexity: O(1)
        linkedList.add(1);
        linkedList.add(2);
        System.out.println("LinkedList after insertion: " + linkedList);
        linkedList.addFirst(0);
        linkedList.addLast(10);
        System.out.println("LinkedList after insertion: " + linkedList);

        // Access
        // Time Complexity: O(n)
        int element = linkedList.get(0);
        System.out.println("Element at index 0: " + element);

        // Search
        // Time Complexity: O(n)
        int index = linkedList.indexOf(2);
        System.out.println("Index of 2: " + index);

        // Deletion
        // Time Complexity: O(1)
        linkedList.removeFirst();
        System.out.println("LinkedList after deletion: " + linkedList);
        linkedList.removeLast();
        System.out.println("LinkedList after deletion: " + linkedList);

        // Size (Length)
        // Time Complexity: O(1)
        int size = linkedList.size();
        System.out.println("Size of LinkedList: " + size);

        // Iterate through LinkedList using for-each loop
        System.out.println("\nIterating through LinkedList using for-each loop:");
        for (int value : linkedList) {
            System.out.println("Element: " + value);
        }

        // Alternatively, use ListIterator for bidirectional traversal
        System.out.println("\nIterating using ListIterator:");
        ListIterator<Integer> iterator = linkedList.listIterator();
        while (iterator.hasNext()) {
            int value = iterator.next();
            System.out.println("Element: " + value);
        }

        // Alternatively, use forEach method (Java 8 and later)
        System.out.println("\nIterating using forEach method:");
        linkedList.forEach(value -> System.out.println("Element: " + value));
    }
}
