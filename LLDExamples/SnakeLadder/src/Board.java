import java.util.HashMap;

/**
 * @author : Adhikram Maitra
 * @created : 5/14/2023, Sunday
 **/
public class Board {
    private int row_count = 3;
    private Cell[][] cells;

    private HashMap<String, Integer> jump_mapper = new HashMap<>();

    public Board(int row_count, int dice_count, int snake_count, int ladder_count, int player_count) {
        System.out.println("Creating board");
        this.row_count = row_count;
        this.cells = new Cell[row_count][row_count];
        setCells();
        setJumps(snake_count, ladder_count);
    }

    private void setCells() {
        // System.out.println("Setting cells");
        for (int row = 0; row < row_count; row++) {
            for (int col = 0; col < row_count; col++) {
                cells[row][col] = new Cell();
            }
        }
        // System.out.println("Cells Created");
    }

    private void setJumps(int snake_count, int ladder_count) {
        System.out.println("Setting snakes and ladders");
        while (snake_count-- > 0) {
            // System.out.println("Setting snakes" + snake_count);
            int start = (int) (Math.random() * (getBoardSize() - 2)) + 1;
            int end = (int) (Math.random() *(getBoardSize() - 2)) + 1;
            if (start <= end || jump_mapper.containsKey(String.valueOf(start))) {
                snake_count++;
                continue;
            }

            jump_mapper.put(String.valueOf(start), 1);
            cells[start / row_count][start % row_count].setJump(new Jump(end));
        }

        while (ladder_count-- > 0) {
            // System.out.println("Setting ladders" + ladder_count);
            int start = (int) (Math.random() * (getBoardSize() - 2)) + 1;
            int end = (int) (Math.random() * (getBoardSize() - 2)) + 1;
            if (start >= end || jump_mapper.containsKey(String.valueOf(start))) {
                ladder_count++;
                continue;
            }

            jump_mapper.put(String.valueOf(start), 1);
            cells[start / row_count][start % row_count].setJump(new Jump(end));
        }

    }

    public int getFinalePosition(int position) {
        System.out.println("Getting final position");
        Cell cell = cells[position / row_count][position % row_count];
        if (cell.getJump() != null) {
            System.out.println("Jumping from "+ position +" to " + cell.getJump().getEnd());
            return cell.getJump().getEnd();
        }
        return position;
    }

    public int getBoardSize() {
        return row_count * row_count;
    }

}
