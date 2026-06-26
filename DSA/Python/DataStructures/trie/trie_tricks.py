"""
Core trie patterns for coding interviews — runnable & self-testing.

Every pattern below is REAL, callable, self-contained code (not a nested stub)
with its time/space complexity, the edge cases it handles, and inline `assert`
tests in `_test()`. Each pattern defines every node/class it uses, so there are
no dangling references. Run `python3 trie_tricks.py`; a clean exit means all
patterns passed their tests.

Patterns:
    1. WordDictionary           — add/search with '.' wildcard (Add & Search Words)
    2. Word Search II           — find dictionary words on a grid via trie + DFS
    3. Autocomplete top-k       — prefix suggestions ranked by frequency
    4. Replace words            — swap each word for its shortest dictionary root
    5. Maximum XOR (binary trie) — max xor of any two numbers, 32-bit trie
"""

from typing import Dict, List, Optional, Tuple


# ===========================================================================
# 1. WORD DICTIONARY — add/search where '.' matches any single character
#    (LeetCode 211: Design Add and Search Words Data Structure)
# ===========================================================================
class _WDNode:
    def __init__(self) -> None:
        self.children: Dict[str, "_WDNode"] = {}
        self.is_end: bool = False


class WordDictionary:
    """Trie supporting '.' as a wildcard in search.

    add_word  : O(m)            — plain trie insert.
    search    : O(m) for a literal query; with w wildcards over an alphabet of
                branching factor b the worst case is O(b^w * m) because each '.'
                forks the DFS into every child. Without wildcards it's O(m).
    Edge cases: empty string (stored on root.is_end), a query that matches
    nothing, a '.'-only query (matches any stored word of that exact length).
    """

    def __init__(self) -> None:
        self.root = _WDNode()

    def add_word(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, _WDNode())
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: _WDNode, i: int) -> bool:
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == ".":
                # wildcard: succeed if ANY child leads to a match
                return any(dfs(child, i + 1) for child in node.children.values())
            child = node.children.get(ch)
            return child is not None and dfs(child, i + 1)

        return dfs(self.root, 0)


# ===========================================================================
# 2. WORD SEARCH II — return every dictionary word found on the board
#    (LeetCode 212). Build a trie of the words, then DFS the grid once,
#    walking the trie in lockstep so all words are searched simultaneously.
# ===========================================================================
class _WSNode:
    def __init__(self) -> None:
        self.children: Dict[str, "_WSNode"] = {}
        self.word: Optional[str] = None       # store the full word at its end node


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    """Find all `words` that can be formed by adjacent (4-dir) cells, no cell
    reused within a single word. Returns the found words (unique).

    Time: O(W*L) to build the trie (W words of length L) + O(R*C*4^maxlen) to
    DFS an R x C board in the worst case (each cell branches 4 ways up to the
    longest word). The trie prunes branches that can't extend any word, which
    is the whole speedup over searching each word independently.
    Edge cases: empty board, empty word list, words longer than the board.
    """
    if not board or not board[0] or not words:
        return []

    # build trie
    root = _WSNode()
    for w in words:
        node = root
        for ch in w:
            node = node.children.setdefault(ch, _WSNode())
        node.word = w

    rows, cols = len(board), len(board[0])
    found: List[str] = []

    def dfs(r: int, c: int, node: _WSNode) -> None:
        ch = board[r][c]
        nxt = node.children.get(ch)
        if nxt is None:
            return                       # no word extends this path — prune
        if nxt.word is not None:
            found.append(nxt.word)
            nxt.word = None              # de-dup: don't report the same word twice

        board[r][c] = "#"                # mark visited
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr, nc, nxt)
        board[r][c] = ch                 # restore

    for i in range(rows):
        for j in range(cols):
            dfs(i, j, root)

    return found


# ===========================================================================
# 3. AUTOCOMPLETE top-k by frequency — given a prefix, return the k most
#    frequent stored words that start with it, ties broken lexicographically.
# ===========================================================================
class _ACNode:
    def __init__(self) -> None:
        self.children: Dict[str, "_ACNode"] = {}
        self.is_end: bool = False
        self.freq: int = 0               # frequency of the word ending here


class Autocomplete:
    """Frequency-ranked prefix suggestions.

    insert : O(m).
    suggest: O(p + S log S) where p = len(prefix) and S = number of words under
             the prefix subtree — walk to the prefix node (O(p)), collect its
             subtree (O(S)), then sort by (-freq, word) and take k.
    Edge cases: prefix not present -> []; empty prefix -> rank across all words;
    fewer than k matches -> return what exists.
    """

    def __init__(self) -> None:
        self.root = _ACNode()

    def insert(self, word: str, freq: int = 1) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, _ACNode())
        node.is_end = True
        node.freq += freq                # accumulate; repeated inserts add up

    def suggest(self, prefix: str, k: int) -> List[str]:
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return []                # prefix not in trie

        matches: List[Tuple[int, str]] = []

        def collect(n: "_ACNode", path: str) -> None:
            if n.is_end:
                matches.append((n.freq, path))
            for ch, child in n.children.items():
                collect(child, path + ch)

        collect(node, prefix)
        # highest frequency first; lexicographic tie-break
        matches.sort(key=lambda fw: (-fw[0], fw[1]))
        return [word for _, word in matches[:k]]


# ===========================================================================
# 4. REPLACE WORDS — replace each word in a sentence by the SHORTEST dictionary
#    "root" that is a prefix of it (LeetCode 648). Build a trie of roots; for
#    each word, walk until you hit a root end (return that prefix) or fall off.
# ===========================================================================
class _RWNode:
    def __init__(self) -> None:
        self.children: Dict[str, "_RWNode"] = {}
        self.is_end: bool = False


def replace_words(roots: List[str], sentence: str) -> str:
    """Replace each whitespace-separated word with its shortest root prefix.

    Time: O(sum of root lengths) to build + O(total sentence length) to query,
    since each word's walk stops at the first (shortest) matching root.
    Edge cases: word with no matching root -> kept as-is; a root equal to the
    word; empty sentence -> "".
    """
    root = _RWNode()
    for r in roots:
        node = root
        for ch in r:
            node = node.children.setdefault(ch, _RWNode())
        node.is_end = True

    def shortest_root(word: str) -> str:
        node = root
        for i, ch in enumerate(word):
            node = node.children.get(ch)
            if node is None:
                return word              # no root is a prefix of this word
            if node.is_end:
                return word[: i + 1]     # first (=shortest) root prefix wins
        return word

    return " ".join(shortest_root(w) for w in sentence.split())


# ===========================================================================
# 5. MAXIMUM XOR of two numbers — binary trie over the 32 bits of each number
#    (LeetCode 421). For each number, greedily walk the OPPOSITE bit at every
#    level to maximize the running XOR.
# ===========================================================================
class _BitNode:
    def __init__(self) -> None:
        self.children: Dict[int, "_BitNode"] = {}   # keys are 0 / 1


def find_maximum_xor(nums: List[int]) -> int:
    """Maximum value of nums[i] ^ nums[j] over all pairs. Time O(32 * n), i.e.
    O(n): every insert and every query is exactly 32 fixed steps (MSB->LSB),
    independent of n. Space O(32 * n).
    Edge cases: 0 or 1 element -> 0 (no pair); duplicates -> 0 contribution but
    handled; all equal -> 0.
    """
    if len(nums) < 2:
        return 0

    root = _BitNode()
    BITS = 31                            # 32-bit non-negative integers

    def insert(num: int) -> None:
        node = root
        for i in range(BITS, -1, -1):
            bit = (num >> i) & 1
            node = node.children.setdefault(bit, _BitNode())

    for num in nums:
        insert(num)

    best = 0
    for num in nums:
        node = root
        cur = 0
        for i in range(BITS, -1, -1):
            bit = (num >> i) & 1
            want = 1 - bit               # prefer the opposite bit -> sets this bit in XOR
            if want in node.children:
                cur |= (1 << i)
                node = node.children[want]
            else:
                node = node.children[bit]
            # node always has at least one of {0,1} because every num was inserted
        best = max(best, cur)
    return best


# ===========================================================================
# TESTS — normal + edge cases for every pattern.
# ===========================================================================
def _test() -> None:
    # --- 1. WordDictionary with '.' wildcard -------------------------------
    wd = WordDictionary()
    for w in ["bad", "dad", "mad"]:
        wd.add_word(w)
    assert wd.search("bad") is True
    assert wd.search("pad") is False          # not added
    assert wd.search(".ad") is True           # wildcard first char
    assert wd.search("b..") is True           # two wildcards
    assert wd.search("..d") is True
    assert wd.search("...") is True           # any 3-letter stored word
    assert wd.search("....") is False         # no 4-letter word stored
    assert wd.search("b.") is False           # wrong length
    wd.add_word("")
    assert wd.search("") is True              # empty word

    # --- 2. Word Search II -------------------------------------------------
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    assert sorted(find_words(board, words)) == ["eat", "oath"]
    # edge cases
    assert find_words([], ["a"]) == []
    assert find_words([["a"]], []) == []
    assert sorted(find_words([["a", "b"]], ["ab", "ba", "abc"])) == ["ab", "ba"]

    # --- 3. Autocomplete top-k by frequency --------------------------------
    ac = Autocomplete()
    ac.insert("apple", 5)
    ac.insert("app", 3)
    ac.insert("application", 4)
    ac.insert("apt", 1)
    ac.insert("banana", 10)
    assert ac.suggest("app", 2) == ["apple", "application"]   # by freq 5,4
    assert ac.suggest("app", 5) == ["apple", "application", "app"]
    assert ac.suggest("xyz", 3) == []                         # no match
    # ties broken lexicographically
    ac2 = Autocomplete()
    ac2.insert("car", 2)
    ac2.insert("cat", 2)
    ac2.insert("can", 2)
    assert ac2.suggest("ca", 3) == ["can", "car", "cat"]      # equal freq -> lex
    assert ac2.suggest("", 1) == ["can"]                      # empty prefix ranks all

    # --- 4. Replace words --------------------------------------------------
    assert replace_words(
        ["cat", "bat", "rat"], "the cattle was rattled by the battery"
    ) == "the cat was rat by the bat"
    # shortest root wins when several apply
    assert replace_words(["a", "aa", "aaa"], "aaaa a aaa") == "a a a"
    # word with no root is kept
    assert replace_words(["cat"], "the dog ran") == "the dog ran"
    assert replace_words([], "anything") == "anything"

    # --- 5. Maximum XOR (binary trie) --------------------------------------
    assert find_maximum_xor([3, 10, 5, 25, 2, 8]) == 28       # 5 ^ 25
    assert find_maximum_xor([0]) == 0                         # single -> no pair
    assert find_maximum_xor([]) == 0
    assert find_maximum_xor([7, 7, 7]) == 0                   # all equal
    assert find_maximum_xor([0, 0xFFFFFFFF]) == 0xFFFFFFFF    # full 32-bit spread


def main() -> None:
    _test()
    print("trie_tricks.py: all 5 patterns verified ✔")


if __name__ == "__main__":
    main()
