"""
# Question: Place Word in Crossword
# Link: https://leetcode.com/problems/place-word-in-crossword/

# Time Complexity: O(m*n*max(m,n))
# Space Complexity: O(m+n)

# Algorithm:
# 1. Process board row by row and column by column
# 2. Try placing word in both directions
# 3. Check for valid placements
# 4. Handle blocked cells and boundaries

# Key Components:
# - place_word_in_crossword(): Main implementation
# - place(): Helper for word placement
# - Direction handling
"""


class PlaceWordInCrossWord:
    def place_word_in_crossword(self, board: list[list[str]], word: str) -> bool:
        if not word:
            return True
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])

        # Track available rows and columns
        cols = [False] * n
        rows = [False] * m

        # Try placing word in both directions
        rev = word[::-1]

        for r in range(m):
            for c in range(n):
                if board[r][c] != "#":
                    if not cols[c]:
                        # Try vertical placement
                        if self.place(board, word, 0, r, c, 1, 0) or self.place(
                            board, rev, 0, r, c, 1, 0
                        ):
                            return True
                        cols[c] = True

                    if not rows[r]:
                        # Try horizontal placement
                        if self.place(board, word, 0, r, c, 0, 1) or self.place(
                            board, rev, 0, r, c, 0, 1
                        ):
                            return True
                        rows[r] = True
                else:
                    rows[r] = False
                    cols[c] = False

        return False

    def place(
        self,
        board: list[list[str]],
        word: str,
        i: int,
        r: int,
        c: int,
        dr: int,
        dc: int,
    ) -> bool:
        m, n = len(board), len(board[0])
        last = m if dr == 1 else n

        if i == len(word):
            if dr > 0 and (r == last or board[r][c] == "#"):
                return True
            elif dc > 0 and (c == last or board[r][c] == "#"):
                return True
            return False

        allowed = ((dr > 0 and 0 <= r < m) or (dc > 0 and 0 <= c < n)) and (
            board[r][c] == " " or board[r][c] == word[i]
        )

        if not allowed:
            return False

        return self.place(board, word, i + 1, r + dr, c + dc, dr, dc)


def main():
    solution = PlaceWordInCrossWord()
    board = [
        [" ", "#", " ", " ", " "],
        [" ", "#", " ", "#", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", "#", " ", " "],
    ]
    word = "hello"
    print(solution.place_word_in_crossword(board, word))


if __name__ == "__main__":
    main()
