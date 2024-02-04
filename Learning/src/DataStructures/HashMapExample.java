package DataStructures;
import java.util.HashMap;
import java.util.Map;

public class HashMapExample {
    public static void main(String[] args) {
        // Create a HashMap with key as String and value as Integer
        HashMap<String, Integer> hashMap = new HashMap<>();

        // Insert (put)
        // Average Case: O(1), Worst Case: O(n)
        // Explanation: Worst case occurs when there are hash collisions and the internal structure needs adjustment (resizing the array).
        System.out.println("Inserting values into HashMap:");
        hashMap.put("One", 1);
        hashMap.put("Two", 2);
        hashMap.put("Three", 3);
        System.out.println("HashMap after insertion: " + hashMap);

        System.out.println(hashMap.size()); // O(1)
        // Delete (remove)
        // Average Case: O(1), Worst Case: O(n)
        // Explanation: Worst case occurs when there are hash collisions, and the internal structure needs adjustment after deletion.
        System.out.println("\nDeleting a key from HashMap:");
        String keyToRemove = "Two";
        if (hashMap.containsKey(keyToRemove)) {
            hashMap.remove(keyToRemove);
            System.out.println("Removed key '" + keyToRemove + "'. Updated HashMap: " + hashMap);
        } else {
            System.out.println("Key '" + keyToRemove + "' not found in HashMap.");
        }

        // Lookup (get)
        // Average Case: O(1), Worst Case: O(n)
        // Explanation: Worst case occurs when there are hash collisions, and multiple keys hash to the same location, requiring a linear search.
        System.out.println("\nLooking up values in HashMap:");
        String keyToLookup = "Three";
        int value = hashMap.getOrDefault(keyToLookup, 0);
        System.out.println("Value for key '" + keyToLookup + "': " + value);

        // Iterate through HashMap
        // Time Complexity: O(n)
        // Explanation: Iterating through all elements requires visiting each entry once, leading to a linear time complexity.
        System.out.println("\nIterating through HashMap:");
        for (String key : hashMap.keySet()) {
            int val = hashMap.get(key);
            System.out.println("Key: " + key + ", Value: " + val);
        }

        System.out.println("\nIterating through HashMap using entrySet and for-each loop:");
        // Iterate through HashMap using entrySet and for-each loop
        for (Map.Entry<String, Integer> entry : hashMap.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
        }

        System.out.println("\nIterating through HashMap using forEach method (Java 8 and later):");

        hashMap.forEach((key, val) -> System.out.println("Key: " + key + ", Value: " + val));


    }
}
