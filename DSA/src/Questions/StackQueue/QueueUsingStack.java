package Questions.StackQueue;

import java.util.Stack;

/*
https://leetcode.com/problems/implement-queue-using-stacks/description/
 Time Complexity:
Push: O(n) where n is the number of elements in the queue. This is because we move elements between the two stacks.
Pop: O(1) for removing the top element from s1.
Peek: O(1) for getting the top element from s1.
Empty: O(1) for checking if s1 is empty.
Space Complexity: O(n) for storing the elements in the two stacks.
 */
public class QueueUsingStack {
    private final Stack<Integer> s1 = new Stack<>();
    private final Stack<Integer> s2 = new Stack<>();

    public QueueUsingStack() {
    }

    public void push(int x) {
        while (!s1.isEmpty()) {
            s2.push(s1.pop());
        }
        s1.push(x);
        while (!s2.isEmpty()) {
            s1.push(s2.pop());
        }
    }

    public int pop() {
        return s1.pop();
    }

    public int peek() {
        return s1.peek();
    }

    public boolean empty() {
        return s1.isEmpty();
    }
    public static void main(String[] args) {
        QueueUsingStack queue = new QueueUsingStack();
        queue.push(1);
        queue.push(2);
        queue.push(3);
        queue.push(4);
        queue.push(5);
        System.out.println("Top element of the queue: " + queue.peek());
    }
}
