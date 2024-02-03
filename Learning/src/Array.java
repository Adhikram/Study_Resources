public class Array {
    public static void main(String[] args) {
    int[] array = new int[3];
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
    array = anotherArray;
    System.out.println(array);
  }
}