package Questions.Matrix;

public class WordSearch {
    private char[][] board;
    private int rows;
    private int cols;
    private int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {-1, -1}, {1, -1}, {-1, 1}};

    public WordSearch(char[][] board) {
        this.board = board;
        this.rows = board.length;
        this.cols = board[0].length;
    }

    private boolean isValid(int row, int col) {
        return row >= 0 && row < rows && col >= 0 && col < cols;
    }

    private boolean searchWord(String word, int row, int col, int index, boolean[][] visited) {
        if (index == word.length()) {
            return true;
        }

        if (!isValid(row, col) || visited[row][col] || board[row][col] != word.charAt(index)) {
            return false;
        }

        visited[row][col] = true;

        for (int[] dir : directions) {
            int newRow = row + dir[0];
            int newCol = col + dir[1];
            if (searchWord(word, newRow, newCol, index + 1, visited)) {
                return true;
            }
        }

        visited[row][col] = false;
        return false;
    }

    public boolean wordExists(String word) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == word.charAt(0)) {
                    boolean[][] visited = new boolean[rows][cols];
                    if (searchWord(word, i, j, 0, visited)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    // Time Complexity: O(N * M * 8^L) where N is the number of cells in the board and L is the length of the word
    // Space Complexity: O(L) where L is the length of the word
    // N.B. The time complexity is O(N * 3^L) because for each cell we have 3 choices to go to the next cell
    // and we have L cells in the word. So, the total number of possibilities is 3^L.

    public static void main(String[] args) {
        char[][] board = {
            {'A', 'B', 'C', 'E'},
            {'S', 'F', 'C', 'S'},
            {'A', 'D', 'E', 'E'}
        };

        WordSearch wordSearch = new WordSearch(board);
        System.out.println(wordSearch.wordExists("ABCCED"));  // Output: true
        System.out.println(wordSearch.wordExists("SEE"));     // Output: true
        System.out.println(wordSearch.wordExists("ABCB"));    // Output: false
    }
}

