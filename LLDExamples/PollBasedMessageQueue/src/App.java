import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Starting the application...");

        // Create a new Queue
        Queue queue = new Queue("10");
        // Adding a new topic to the queue
        Topic topic = queue.addTopic();
        // Creating a new subscriber
        Subscriber subscriber = new Subscriber("Alice", queue);
        // Creating a new publisher
        Publisher publisher = new Publisher("Bob", queue);
        // Alice subscribes to the topic
        subscriber.subscribe(topic);
        // Bob publishes a message to the topic
        publisher.publish("Hello, World!", topic);

        // Getting the content of the topic for Alice
        ArrayList<Message> messages = subscriber.getTopicContent(topic);
        for (Message message : messages) {
            System.out.println(message.getData());
        }

    }
}
