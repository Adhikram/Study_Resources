import java.util.ArrayList;

public class King extends Piece {
    public King(boolean white) {
        super(white);
    }
    public boolean canMove(Board board, Block startBlock, Block endBlock) {
        ArrayList<Integer> startCoordinates = startBlock.getCoordinates();
        ArrayList<Integer> endCoordinates = endBlock.getCoordinates();
        int xDistance = Math.abs(startCoordinates.get(0) - endCoordinates.get(0));
        int yDistance = Math.abs(startCoordinates.get(1) - endCoordinates.get(1));
        // Add Logic for castle move
        if (xDistance == 2 && yDistance == 0) {
            return true;
        }
        return xDistance + yDistance == 1;
    }
}