import java.util.Stack;

public class StackExample {
    public static void main(String[] args) {
        // Signature
        Stack<Integer> stack = new Stack<>();

        // Push
        System.out.println("Pushing element onto the stack: 1");
        stack.push(1);

        // Pop
        if (!stack.isEmpty()) {
            int poppedElement = stack.pop();
            System.out.println("Popped element from the stack: " + poppedElement);
        } else {
            System.out.println("Stack is empty. Cannot pop.");
        }

        // Peek
        if (!stack.isEmpty()) {
            int topElement = stack.peek();
            System.out.println("Top element of the stack: " + topElement);
        } else {
            System.out.println("Stack is empty. No top element to peek.");
        }

        // Add more elements
        stack.push(2);
        stack.push(3);
        System.out.println("Stack size: " + stack.size());

        // Iterate through Stack using for-each loop
        System.out.println("\nIterating through Stack using for-each loop:");
        for (int element : stack) {
            System.out.println("Element: " + element);
        }

        // Alternatively, use Iterator for more control
        System.out.println("\nIterating using Iterator:");
        java.util.Iterator<Integer> iterator = stack.iterator();
        while (iterator.hasNext()) {
            int element = iterator.next();
            System.out.println("Element: " + element);
        }
        
        // Alternatively, use forEach method (Java 8 and later)
        System.out.println("\nIterating using forEach method:");
        stack.forEach(element -> System.out.println("Element: " + element));

        // Alternatively, convert to array and use enhanced for loop
        System.out.println("\nIterating using toArray method:");
        Integer[] elementsArray = stack.toArray(new Integer[0]);
        for (int element : elementsArray) {
            System.out.println("Element: " + element);
        }
    }
}
