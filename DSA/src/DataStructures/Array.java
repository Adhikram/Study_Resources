package DataStructures;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Array {
  public static void main(String[] args) {
    int[] array = new int[3];
    List<Integer>[] adj = new List[3];

    ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 5, 1));
    array[0] = 1;
    array[1] = 2;
    array[2] = 3;

    // Access
    int element = array[0]; // O(1)
    System.out.println(element); // 1

    // Search
    int index = -1;
    for (int i = 0; i < array.length; i++) {
      if (array[i] == 2) {
        index = i;
        break;
      }
    }
    System.out.println(index); // 1

    // Insertion (dynamic)
    int[] newArray = new int[array.length + 1];
    for (int i = 0; i < array.length; i++) {
      newArray[i] = array[i];
    }
    newArray[array.length] = 4;
    array = newArray;
    System.out.println(array);

    // Deletion (dynamic)
    int value = 2;
    int[] anotherArray = new int[array.length - 1];
    int j = 0;
    for (int i = 0; i < array.length; i++) {
      if (array[i] != value) {
        anotherArray[j] = array[i];
        j++;
      }
    }
    int[][] intervals = { { 1, 3 }, { 2, 6 }, { 8, 10 }, { 15, 18 } };
    Arrays.sort(intervals, new Comparator<int[]>() {
      public int compare(int[] a, int[] b) {
        return a[0] - b[0];
      }
    });
    System.out.println(Arrays.deepToString(intervals));


    int [][] grid = new int[3][3];
    Arrays.stream(grid).forEach(row -> Arrays.fill(row, 1));
  }
}
