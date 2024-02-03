import java.util.HashSet;
import java.util.Iterator;

// Class Structure
class HashSetExample {
    public static void main(String[] args) {
        // Signature
        HashSet<Integer> hashSet = new HashSet<>();

        // Add
        // Average Case: O(1), Worst Case: O(n)
        // Explanation: Worst case occurs when there are hash collisions and elements need to be rehashed or placed in a different location.
        hashSet.add(1);
        hashSet.add(2);
        hashSet.add(3);
        System.out.println("HashSet after insertion: " + hashSet);

        // Remove
        // Average Case: O(1), Worst Case: O(n)
        // Explanation: Worst case occurs when there are hash collisions and elements need to be rehashed or placed in a different location after removal.
        System.out.println("\nRemoving a value from HashSet:");
        hashSet.remove(2);

        // Contains
        // Average Case: O(1), Worst Case: O(n)
        // Explanation: Worst case occurs when there are hash collisions and the element's hash position needs to be searched.
        boolean contains = hashSet.contains(1);
        System.out.println("HashSet contains 1: " + contains);

        // Size (Length)
        // Time Complexity: O(1)
        int size = hashSet.size();
        System.out.println("Size of HashSet: " + size);

        // Iterate through HashSet without Iterator
        System.out.println("\nIterating through for-each loop:");
        // Using forEach method (Java 8 and later)
        hashSet.forEach(element -> System.out.println("Element: " + element));

        System.out.println("\nIterating using toArray method:");
        // Alternatively, convert to array and use enhanced for loop
        Integer[] elementsArray = hashSet.toArray(new Integer[0]);
        System.out.println("\nIterating using array:");
        for (int element : elementsArray) {
            System.out.println("Element: " + element);
        }

        System.out.println("\nIterating using Iterator:");
        // Iterate through HashSet using Iterator
        Iterator<Integer> iterator = hashSet.iterator();
        while (iterator.hasNext()) {
            int element = iterator.next();
            System.out.println("Element: " + element);
        }
        System.out.println("\nIterating using for-each loop:");
        // Alternatively, use enhanced for loop
        for (int element : hashSet) {
            System.out.println("Element: " + element);
        }
    }
}
