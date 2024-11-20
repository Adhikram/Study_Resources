"""
# Question: Word Search
# Link: https://leetcode.com/problems/word-search/

# Time Complexity: O(m*n*4^L) where L is word length
# Space Complexity: O(L)

# Algorithm:
# 1. DFS from each cell
# 2. Track visited cells
# 3. Check all possible directions
# 4. Return true if word is found
"""


class WordSearch:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i: int, j: int, k: int) -> bool:
            if k == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False

            # Mark as visited
            temp = board[i][j]
            board[i][j] = "#"

            # Check all directions
            result = (
                dfs(i + 1, j, k + 1)
                or dfs(i - 1, j, k + 1)
                or dfs(i, j + 1, k + 1)
                or dfs(i, j - 1, k + 1)
            )

            # Restore the cell
            board[i][j] = temp
            return result

        # Try starting from each cell
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False


def main():
    solution = WordSearch()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(solution.exist(board, word))  # Expected: True


if __name__ == "__main__":
    main()
