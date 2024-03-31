import java.util.ArrayList;
import java.util.HashMap;

public class Queue {

    ArrayList<Topic> topics = new ArrayList<Topic>();
    private HashMap<Subscriber, Message> subscriberDetails = new HashMap<Subscriber, Message>();
    private HashMap<Message, String> ttlDetails = new HashMap<Message, String>();
    private String ttl;

    // Constructor without parameters
    public Queue(String ttl) {
        this.ttl = ttl;
    }

    // Setter for ttlDetails
    public void setTtlDetails(Message message, String time) {
        ttlDetails.put(message, time);
    }

    // Getter for ttlDetails
    public String getTtlDetails(Message message) {
        return ttlDetails.getOrDefault(message, ttl);
    }

    // Getter for ttl
    public String getTtl() {
        return this.ttl;
    }

    // Add a topic to the queue
    public Topic addTopic() {
        Topic topic = new Topic();
        topics.add(topic);
        return topic;
    }

    // Get the topics
    public ArrayList<Topic> getTopics() {
        return this.topics;
    }

    // Get content of the topic
    public ArrayList<Message> getTopicContent(Topic topic, Subscriber subscriber) {
        Message message = subscriberDetails.getOrDefault(subscriber, topic.getHead());
        ArrayList<Message> messages = topic.getNextMessages(message);

        // Updating the subscriber's last message
        if (messages.size() > 0) {
            subscriberDetails.put(subscriber, messages.get(messages.size() - 1));
        }
        return messages;
    }

    // Add a subscriber to the queue
    public void addSubscriber(Subscriber subscriber, Topic topic) {
        subscriberDetails.put(subscriber, topic.getHead());
    }


}
