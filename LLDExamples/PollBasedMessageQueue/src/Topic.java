import java.util.ArrayList;

public class Topic {
    // private Integer id;
    private Message head = new Message();
    private Message tail = new Message();

    // Constructor without parameters
    public Topic() {
        // this.id = id;
        head.setNext(tail);
        tail.setPrevious(head);
    }

    // Getter for head
    public Message getHead() {
        return this.head;
    }

    // Getter for tail
    public Message getTail() {
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
        Message lastMessage = tail.getPrevious();
        lastMessage.setNext(message);
        message.setPrevious(lastMessage);
        message.setNext(tail);
        tail.setPrevious(message);
    }
}