import java.util.ArrayList;

public class Publisher {
    private String name;
    private Queue queue;

    // Constructor with parameters
    public Publisher(String name, Queue queue) {
        this.name = name;
        this.queue = queue;
    }

    // Getter for name
    public String getName() {
        return this.name;
    }

    // Getter for queue
    public Queue getQueue() {
        return this.queue;
    }

    // Publish a message to the topic
    public void publish(String data, Topic topic, String time) {
        Message message = new Message(data, null, null);
        queue.setTtlDetails(message, time);
        topic.addMessage(message);
    }

    public void publish(String data, Topic topic) {
        Message message = new Message(data, null, null);
        queue.setTtlDetails(message, queue.getTtl());
        topic.addMessage(message);
    }

}
