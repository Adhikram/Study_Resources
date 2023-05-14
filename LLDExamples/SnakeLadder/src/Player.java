/**
 * @author : Adhikram Maitra
 * @created : 5/14/2023, Sunday
 **/
public class Player {
    private String name;
    private int position;

    public Player(String name, int position) {
        System.out.println("Creating ->>" + name + " at position " + position);
        this.name = name;
        this.position = position;
    }

    public String getName() {
        return name;
    }

    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }
}
