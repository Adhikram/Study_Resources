/**
 * @author : Adhikram Maitra
 * @created : 5/14/2023, Sunday
 **/
public class Dice {
    private int dice_count = 1;
    private int dice_max = 6;

    public Dice(int dice_count, int dice_max) {
        this.dice_count = dice_count;
        this.dice_max = dice_max - 1;
    }

    public int roll() {
        System.out.println("Rolling dice");
        int result = 0;
        int dice_value = this.dice_count;
        while (dice_value-- > 0) {
            int val = (int) (Math.random() * this.dice_max) + 1;
            result += val;
            System.out.println("Dice value: " + val);
        }
        return result;
    }

    public static void main(String[] args) {
        Dice dice = new Dice(2, 6);
        System.out.println(dice.roll());
    }
}
