package Questions.Matrix;

import java.util.HashSet;
import java.util.Set;

public class ValidSudoku {

    public int removeStones(int[][] stones) {
        int count = 0;

        HashSet<String> seen = new HashSet<>();
        for(int[] stone : stones){
            System.out.println("Stone: " + stone[0] + " " + stone[1]);
            boolean row = seen.add("A stone in row " + stone[0]);
            boolean column = seen.add("A stone in column " + stone[1]);
            if (row || column){
                count ++;
            }
            seen.forEach(System.out::println);
            System.out.println("Count: " + count);
        }
        return count;
    }
    public boolean isValidSudoku(char[][] board) {
        Set<String> seen = new HashSet<>();
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                char number = board[i][j];
                if (number != '.')
                    if (!seen.add(number + " in row " + i) ||
                            !seen.add(number + " in column " + j) ||
                            !seen.add(number + " in block " + i / 3 + "-" + j / 3))
                        return false;
            }
        }
        return true;
    }
    // Time complexity: O(9^(n*n))
    // Space complexity: O(n*n)
    public static void main(String[] args) {
        char[][] board = {
                {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
                {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
                {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
                {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
                {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
                {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
                {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
                {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
                {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };
        ValidSudoku validSudoku = new ValidSudoku();
        System.out.println(validSudoku.isValidSudoku(board));
    }
}
