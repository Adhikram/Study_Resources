import java.util.ArrayList;

public class Subscriber {
    private String name;
    private Queue queue;

    // Constructor with parameters
    public Subscriber(String name, Queue queue) {
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

    // Subscribe to a topic
    public void subscribe(Topic topic) {
        queue.addSubscriber(this, topic);
    }

    // Get the content of the topic
    public ArrayList<Message> getTopicContent(Topic topic) {
        return queue.getTopicContent(topic, this);
    }

}
