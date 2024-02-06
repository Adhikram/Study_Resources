package Questions.StackQueue;

public class StackImplementation {
    static class Stack {
        int top;
        int[] store;
        int capacity = 0;
        Stack(int capacity) {
            // Write your code here.
            this.capacity = capacity;
            store = new int[capacity];
            top = -1;
        }
        public void push(int num) {
            // Write your code here.
            if(this.isFull() == 1){
                return;
            }
            store[++top] = num;
        }
        public int pop() {
            // Write your code here.
            if(this.isEmpty() == 1){
                return -1;
            }
            return store[top--];
        }
        public int top() {
            // Write your code here.
            if(this.isEmpty() == 1){
                return -1;
            }
            return store[top];
        }
        public int isEmpty() {
            // Write your code here.
            return (top == -1) ? 1 : 0;
        }
        public int isFull() {
            // Write your code here.
            return (top == (capacity - 1))? 1 : 0;
        }
    }
    public static void main(String[] args) {
        Stack stack = new Stack(5);
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(5);
        System.out.println("Top element of the stack: " + stack.top);
    }
}
