import java.util.LinkedList;
import java.util.Queue;

/**
 * @author : Adhikram Maitra
 * @created : 5/14/2023, Sunday
 **/
public class Game {
    private String winner = null;
    private Board board;
    private Dice dice;
    private Queue<Player> players = new LinkedList<>();

    private Game(){
        initializeGame();
    }

    private void initializeGame() {
        this.board = new Board(10, 1, 5, 6, 2);
        this.dice = new Dice(2, 6);
        addPlayers(2);
    }

    private void addPlayers(int count) {
        System.out.println("Setting players");
        int temp = 0;
        while(temp++ < count){
            System.out.println("Getting Details of Player " + temp);
            players.add(new Player("Player " + String.valueOf(temp), 0));
        }

    }

    private void startGame(){
        while(winner == null){
            Player player = players.poll();
            int dice_value = dice.roll();
            int new_position = player.getPosition() + dice_value;
            if( new_position > this.board.getBoardSize() - 1){
                // Player will not move for this turn
                new_position = player.getPosition();
            }
            int final_position = this.board.getFinalePosition(new_position);
            System.out.println("MOVE->>>> " + player.getName() + " rolled a " + dice_value + " and moved from " + player.getPosition() + " to " + final_position);
            player.setPosition(final_position);
            if(final_position == this.board.getBoardSize() - 1){
                winner = player.getName();
            }
            players.add(player);

        }
        System.out.println("Winner is " + winner);
    }

    public static void main(String[] args) {
        Game game = new Game();
        game.startGame();
    }
}
