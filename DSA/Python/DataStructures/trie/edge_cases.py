"""
Trie edge cases — the inputs that break naive solutions, with runnable proof.

Each function demonstrates ONE edge-case category: a naive approach that fails
(or a subtlety that bites) and the robust version that doesn't. Run
`python3 edge_cases.py`; a clean exit means every "robust" version handled its
edge case as documented.

Use this as a pre-submission checklist: walk your trie solution through each case.
"""

from typing import Dict, Optional


# A small, self-contained trie used by the demos below.
class _Node:
    def __init__(self) -> None:
        self.children: Dict[str, "_Node"] = {}
        self.is_end: bool = False


class _Trie:
    def __init__(self) -> None:
        self.root = _Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, _Node())
        node.is_end = True

    def _walk(self, s: str) -> Optional[_Node]:
        node = self.root
        for ch in s:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        n = self._walk(word)
        return n is not None and n.is_end

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None


# ---------------------------------------------------------------------------
# 1. EMPTY STRING insert/search — the empty word lives on root.is_end. A naive
#    "did the loop run?" check forgets it can be a legitimate stored word.
# ---------------------------------------------------------------------------
def empty_string() -> None:
    t = _Trie()
    assert t.search("") is False          # nothing inserted yet
    t.insert("")                          # loop body never runs -> sets root.is_end
    assert t.search("") is True
    assert t.starts_with("") is True      # empty prefix always matches (root exists)

    # And the empty prefix is a prefix of every word:
    t.insert("abc")
    assert t.starts_with("") is True


# ---------------------------------------------------------------------------
# 2. SINGLE CHARACTER — the smallest non-empty word; the end node is a direct
#    child of root. Make sure search vs starts_with still differ correctly.
# ---------------------------------------------------------------------------
def single_character() -> None:
    t = _Trie()
    t.insert("a")
    assert t.search("a") is True
    assert t.starts_with("a") is True
    assert t.search("b") is False
    assert t.starts_with("ab") is False   # 'a' is a leaf-word, no 'b' child


# ---------------------------------------------------------------------------
# 3. DUPLICATE WORD INSERTS — must be idempotent for membership; re-inserting
#    a word must not corrupt the structure or flip is_end off.
# ---------------------------------------------------------------------------
def duplicate_inserts() -> None:
    t = _Trie()
    t.insert("dog")
    t.insert("dog")
    t.insert("dog")
    assert t.search("dog") is True
    # exactly one path 'd'->'o'->'g' regardless of how many inserts
    assert list(t.root.children.keys()) == ["d"]


# ---------------------------------------------------------------------------
# 4. PREFIX THAT IS NOT A FULL WORD — the canonical trie trap. Reaching the end
#    of the path is NOT a match; the node must have is_end set.
# ---------------------------------------------------------------------------
def prefix_not_a_word() -> None:
    def naive_search(t, word):            # WRONG: treats "path exists" as a match
        return t.starts_with(word)

    t = _Trie()
    t.insert("apple")
    assert naive_search(t, "app") is True     # the bug: "app" was never inserted
    assert t.search("app") is False           # robust: is_end is False here
    assert t.starts_with("app") is True       # but it IS a valid prefix


# ---------------------------------------------------------------------------
# 5. MISSING PREFIX — a query that diverges from every stored path must short-
#    circuit to False, not crash on a missing child.
# ---------------------------------------------------------------------------
def missing_prefix() -> None:
    def naive_walk(t, s):                 # crashes: assumes the child exists
        node = t.root
        for ch in s:
            node = node.children[ch]      # KeyError on a missing branch
        return True

    t = _Trie()
    t.insert("hello")
    assert t.starts_with("xyz") is False  # robust: .get() returns None -> False
    assert t.starts_with("help") is False # diverges at 'p'
    try:
        naive_walk(t, "xyz")
        assert False
    except KeyError:
        pass                              # exactly the crash we avoid


# ---------------------------------------------------------------------------
# 6. CASE SENSITIVITY — 'A' and 'a' are different characters. Decide and
#    normalize up front, or matches silently fail.
# ---------------------------------------------------------------------------
def case_sensitivity() -> None:
    t = _Trie()
    t.insert("Hello")
    assert t.search("Hello") is True
    assert t.search("hello") is False     # different first character

    # Robust case-insensitive trie: normalize on the way in AND out.
    ci = _Trie()
    ci.insert("Hello".lower())
    assert ci.search("HELLO".lower()) is True


# ---------------------------------------------------------------------------
# 7. DELETE OF A NON-EXISTENT WORD — must be a safe no-op, never a crash and
#    never partial corruption of existing words.
# ---------------------------------------------------------------------------
def delete_non_existent() -> None:
    def delete(t: _Trie, word: str) -> bool:
        if not t.search(word):
            return False                  # robust: bail before touching anything

        def prune(node: _Node, depth: int) -> bool:
            if depth == len(word):
                node.is_end = False
            else:
                ch = word[depth]
                if prune(node.children[ch], depth + 1):
                    del node.children[ch]
            return not node.is_end and not node.children

        prune(t.root, 0)
        return True

    t = _Trie()
    t.insert("test")
    assert delete(t, "tea") is False      # never inserted -> no-op
    assert delete(t, "tes") is False      # a mere prefix -> no-op
    assert t.search("test") is True       # original word intact
    assert delete(t, "test") is True      # real delete works
    assert t.search("test") is False
    assert t.starts_with("t") is False    # dead branch fully pruned


# ---------------------------------------------------------------------------
# 8. WILDCARD MATCHING NOTHING — a '.' query whose length or path matches no
#    stored word must return False, not accidentally succeed on partial walks.
# ---------------------------------------------------------------------------
def wildcard_matches_nothing() -> None:
    class WD:
        def __init__(self) -> None:
            self.root = _Node()

        def add(self, word: str) -> None:
            node = self.root
            for ch in word:
                node = node.children.setdefault(ch, _Node())
            node.is_end = True

        def search(self, word: str) -> bool:
            def dfs(node: _Node, i: int) -> bool:
                if i == len(word):
                    return node.is_end    # MUST require a word end, not just a node
                ch = word[i]
                if ch == ".":
                    return any(dfs(c, i + 1) for c in node.children.values())
                nxt = node.children.get(ch)
                return nxt is not None and dfs(nxt, i + 1)

            return dfs(self.root, 0)

    wd = WD()
    wd.add("cat")
    assert wd.search("c.t") is True
    assert wd.search("....") is False     # no 4-letter word -> nothing matches
    assert wd.search("c.") is False       # ends mid-word: 'ca' node not is_end
    assert wd.search("d.t") is False      # diverges immediately, no 'd' child
    assert wd.search("...") is True       # matches "cat" exactly


def main() -> None:
    empty_string()
    single_character()
    duplicate_inserts()
    prefix_not_a_word()
    missing_prefix()
    case_sensitivity()
    delete_non_existent()
    wildcard_matches_nothing()
    print("edge_cases.py: all 8 edge-case categories verified ✔")


if __name__ == "__main__":
    main()
