public class Message {
    private String data;
    private Message next = null;
    private Message previous = null;
    // private DataTime time = new DataTime();

    // Constructor without parameters
    public Message() {}

    // Constructor with parameters
    public Message(String data, Message next, Message previous) {
        this.data = data;
        this.next = next;
        this.previous = previous;
    }

    // Getter and Setter for data
    public String getData() {
        return this.data;
    }

    public void setData(String data) {
        this.data = data;
    }

    // Getter and Setter for next
    public Message getNext() {
        return this.next;
    }

    public void setNext(Message next) {
        this.next = next;
    }

    // Getter and Setter for previous
    public Message getPrevious() {
        return this.previous;
    }

    public void setPrevious(Message previous) {
        this.previous = previous;
    }
}