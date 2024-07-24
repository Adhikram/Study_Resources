package Questions.String;

/*
 You are given an m x n matrix board, representing the current state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), ' ' to represent any empty cells, and '#' to represent any blocked cells.

A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if:

It does not occupy a cell containing the character '#'.
The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.
There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.
There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.
Given a string word, return true if word can be placed in board, or false otherwise.

 

Example 1:


Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"
Output: true
Explanation: The word "abc" can be placed as shown above (top to bottom).
Example 2:


Input: board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"
Output: false
Explanation: It is impossible to place the word because there will always be a space/letter above or below it.
Example 3:


Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"
Output: true
Explanation: The word "ca" can be placed as shown above (right to left). 
 

Constraints:

m == board.length
n == board[i].length
1 <= m * n <= 2 * 105
board[i][j] will be ' ', '#', or a lowercase English letter.
1 <= word.length <= max(m, n)
word will contain only lowercase English letters.

 */
public class PlaceWordInCrossWord {
    public static boolean placeWordInCrossword(char[][] board, String word) {
        if (word.length() == 0)
            return true;
        int m = board.length;
        if (m == 0)
            return false;
        int n = board[0].length;

        // reverse the string
        String rev = new StringBuilder(word).reverse().toString();
        // available rows and cols
        boolean[] cols = new boolean[n];
        boolean[] rows = new boolean[m];

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (board[r][c] != '#') {
                    if (!cols[c]) {
                        // current col can be used to place the string

                        // placing original string vertically
                        if (place(board, word, 0, r, c, 1, 0))
                            return true;
                        // placing reverse string vertically
                        if (place(board, rev, 0, r, c, 1, 0))
                            return true;

                        cols[c] = true; // mark col as used
                    }

                    if (!rows[r]) {
                        // current row can be used to place the string

                        // placing original string horizontally
                        if (place(board, word, 0, r, c, 0, 1))
                            return true;
                        // placing reverse string horizontally
                        if (place(board, rev, 0, r, c, 0, 1))
                            return true;

                        rows[r] = true; // mark row as used
                    }
                } else {
                    // this means next cols and rows are available for use
                    // mark in the array
                    rows[r] = false;
                    cols[c] = false;
                }
            }
        }

        return false;
    }

    private static boolean place(char[][] board, String word, int i, int r, int c, int dr, int dc) {
        int m = board.length;
        int n = board[0].length;

        int last = dr == 1 ? m : n;

        if (i == word.length()) {
            if (dr > 0 && (r == last || board[r][c] == '#'))
                return true;
            else if (dc > 0 && (c == last || board[r][c] == '#'))
                return true;
            else
                return false;
        }

        boolean allowed = ((dr > 0 && r >= 0 && r < m) || (dc > 0 && c >= 0 && c < n))
                && (board[r][c] == ' ' || board[r][c] == word.charAt(i));
        if (!allowed)
            return false;

        return place(board, word, i + 1, r + dr, c + dc, dr, dc);
    }

    public static void main(String[] args) {
        char[][] board = {
                { ' ', '#', ' ', ' ', ' ' },
                { ' ', '#', ' ', '#', ' ' },
                { ' ', ' ', ' ', ' ', ' ' },
                { ' ', ' ', '#', ' ', ' ' }
        };
        String word = "hello";

        // Assuming canPlaceWord is a method that checks if the word can be placed
        // This is a placeholder for whatever your actual method is for checking the
        // placement
        boolean canPlace = placeWordInCrossword(board, word);

        if (canPlace) {
            System.out.println("The word can be placed in the crossword.");
        } else {
            System.out.println("The word cannot be placed in the crossword.");
        }
    }

}
// Time Complexity: O(m*n*max(m,n))
// Space Complexity: O(m+n)
