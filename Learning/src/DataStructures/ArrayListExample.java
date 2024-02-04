package DataStructures;
import java.util.ArrayList;

// Class Structure
public class ArrayListExample {
  public static void main(String[] args) {
    ArrayList<Integer> arrayList = new ArrayList<>();

    // Insertion (static)
    arrayList.add(1); // O(1)
    arrayList.add(2); // O(1)

    // Access
    int element = arrayList.get(0); // O(1)
    System.out.println(element); // 1

    // Search
    int index = arrayList.indexOf(1); // O(n)]
    System.out.println(index); // 1

    // Insertion (dynamic)
    arrayList.add(4); // O(1) amortized
    System.out.println(arrayList); // [4]

    // Deletion (dynamic)
    arrayList.remove(Integer.valueOf(2)); // O(n)
    System.out.println(arrayList); // [4]
    arrayList.remove(0);
    System.out.println(arrayList); // [4]
  }
}
