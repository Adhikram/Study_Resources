import java.util.ArrayList;
import java.util.concurrent.locks.ReentrantLock;

public class Topic {
    // private Integer id;
    private Message head = new Message();
    private Message tail = new Message();

    private final ReentrantLock write = new ReentrantLock();
    // Constructor without parameters
    public Topic() {
        // this.id = id;
        head.setNext(tail);
        tail.setPrevious(head);
    }

    // Getter for head
    public synchronized Message getHead() {
        return this.head;
    }

    // Getter for tail
    public synchronized Message getTail() {
        return this.tail;
    }

    // Getter for id
    // public Integer getId() {
    //     return this.id;
    // }

    // Get Next Messages
    public ArrayList<Message> getNextMessages(Message message) {
        ArrayList<Message> messages = new ArrayList<Message>();
        Message current = message.getNext();
        if( current == tail){
            return messages;
        }
        while (current != tail) {
            messages.add(current);
            current = current.getNext();
        }
        return messages;
    }

    // Add message to the end of the topic
    public void addMessage(Message message) {
        write.lock();
        try {
            Message lastMessage = tail.getPrevious();
            lastMessage.setNext(message);
            message.setPrevious(lastMessage);
            message.setNext(tail);
            tail.setPrevious(message);
        } finally {
            write.unlock();
        }
    }
}