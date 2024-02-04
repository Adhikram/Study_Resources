package DataStructures;
import java.util.LinkedList;
import java.util.Queue;

public class QueueExample {
    public static void main(String[] args) {
        // Signature
        Queue<Integer> queue = new LinkedList<>();

        // Enqueue
        System.out.println("Enqueuing element: 1");
        queue.add(1);

        // Dequeue
        if (!queue.isEmpty()) {
            int removedElement = queue.poll();
            System.out.println("Dequeued element: " + removedElement);
        } else {
            System.out.println("Queue is empty. Cannot dequeue.");
        }

        // Peek
        if (!queue.isEmpty()) {
            int frontElement = queue.peek();
            System.out.println("Front element: " + frontElement);
        } else {
            System.out.println("Queue is empty. No front element to peek.");
        }

        // Add more elements
        queue.add(2);
        queue.add(3);


        // Length (Size)
        System.out.println("Size of Queue: " + queue.size());

        // Iterate through Queue using for-each loop
        System.out.println("\nIterating through Queue using for-each loop:");
        for (int element : queue) {
            System.out.println("Element: " + element);
        }

        // Alternatively, use Iterator for more control
        System.out.println("\nIterating using Iterator:");
        java.util.Iterator<Integer> iterator = queue.iterator();
        while (iterator.hasNext()) {
            int element = iterator.next();
            System.out.println("Element: " + element);
        }

        // Alternatively, use forEach method (Java 8 and later)
        System.out.println("\nIterating using forEach method:");
        queue.forEach(element -> System.out.println("Element: " + element));

        // Alternatively, convert to array and use enhanced for loop
        System.out.println("\nIterating using toArray method:");
        Integer[] elementsArray = queue.toArray(new Integer[0]);
        for (int element : elementsArray) {
            System.out.println("Element: " + element);
        }

    }
}
