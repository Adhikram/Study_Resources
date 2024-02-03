import java.util.PriorityQueue;
import java.util.Comparator;

public class PriorityQueueExample {
    public static void main(String[] args) {
        // Default Case (Natural Ordering)
        PriorityQueue<Integer> defaultPriorityQueue = new PriorityQueue<>();
        addElements(defaultPriorityQueue, "Default");
        printElements(defaultPriorityQueue);

        // Using Comparator.reverseOrder()
        PriorityQueue<Integer> reversePriorityQueue = new PriorityQueue<>(Comparator.reverseOrder());
        addElements(reversePriorityQueue, "Reverse");
        printElements(reversePriorityQueue);

        // Using a Custom Comparator (Custom Ordering)
        PriorityQueue<Integer> customPriorityQueue = new PriorityQueue<>(new CustomComparator());
        addElements(customPriorityQueue, "Custom");
        printElements(customPriorityQueue);

        // Using a lambda expression for custom comparison logic
        PriorityQueue<Integer> lambdaPriorityQueue = new PriorityQueue<>((o1, o2) -> Integer.compare(o2, o1));
        addElements(lambdaPriorityQueue, "Lambda");
        printElements(lambdaPriorityQueue);
    }

    // Helper method to add elements to the PriorityQueue
    private static void addElements(PriorityQueue<Integer> priorityQueue, String scenario) {
        System.out.println("Adding elements for " + scenario + " case:");
        priorityQueue.add(3);
        priorityQueue.add(1);
        priorityQueue.add(5);
        priorityQueue.add(2);
    }

    // Helper method to print elements from the PriorityQueue
    private static void printElements(PriorityQueue<Integer> priorityQueue) {
        System.out.println("Elements in the PriorityQueue:");
        while (!priorityQueue.isEmpty()) {
            System.out.println(priorityQueue.poll());
        }
        System.out.println();
    }

    // Custom comparator class
    static class CustomComparator implements Comparator<Integer> {
        @Override
        public int compare(Integer o1, Integer o2) {
            // Custom comparison logic
            // Return a negative value if o1 is less than o2,
            // a positive value if o1 is greater than o2,
            // and 0 if they are equal.
            return Integer.compare(o2, o1); // Reversed order in this example
        }
    }
}
