"""
Trie (prefix tree) fundamentals for interviews — a clean, runnable Trie class.

A TRIE is a character-indexed tree. Each node holds a `children` map (char ->
child node) and an `is_end` flag marking whether a word terminates there. Words
that share a prefix share the path of nodes for that prefix — that shared-prefix
structure is the whole point, and it's why prefix queries are O(length of the
prefix) regardless of how many words are stored.

Every operation below carries its time complexity and the gotchas that cause
real interview bugs. Run `python3 fundamentals.py` — if it exits cleanly, every
example behaved as documented.

The five core operations:
    insert(word)                  -> O(m)   m = len(word)
    search(word)                  -> O(m)   full-word match (is_end matters!)
    starts_with(prefix)           -> O(p)   p = len(prefix)
    delete(word)                  -> O(m)   prune only nodes no one else needs
    count_words_with_prefix(pre)  -> O(p)   via a per-node word counter
"""

from typing import Dict, Optional


# ---------------------------------------------------------------------------
# Node: a children map + an end-of-word flag (+ a counter for fast prefix counts)
# ---------------------------------------------------------------------------
class TrieNode:
    """One node of the trie.

    `children` maps a single character to the next TrieNode. `is_end` is the
    SENTINEL that says "a complete word ends here" — without it you cannot tell
    a stored word from a mere prefix of one. `count` caches how many inserted
    words pass through this node, turning count_words_with_prefix into O(p).
    """

    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.is_end: bool = False
        self.count: int = 0       # number of inserted words passing through here


class Trie:
    """A standard prefix tree over arbitrary strings.

    Case sensitivity: this trie is CASE-SENSITIVE ('A' and 'a' are different
    characters). Normalize input (e.g. `word.lower()`) before insert/search if
    your problem wants case-insensitive behavior.
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    # -----------------------------------------------------------------------
    # insert — walk/create one node per character, mark the last as a word end
    # Time O(m), Space O(m) worst case (a brand-new branch). m = len(word).
    # -----------------------------------------------------------------------
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1          # one more word passes through this node
        node.is_end = True
        # NOTE: inserting "" just sets root.is_end = True (the empty string is a
        # legitimate stored word). The loop body never runs, so no counts change.
        if word == "":
            self.root.is_end = True

    # -----------------------------------------------------------------------
    # search — full-word match. The is_end check is the whole gotcha:
    # reaching the end of the path is NOT enough; that node must end a word.
    # Time O(m).
    # -----------------------------------------------------------------------
    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_end

    # -----------------------------------------------------------------------
    # starts_with — prefix existence. Unlike search, is_end does NOT matter:
    # we only care that the path of characters exists. Time O(p).
    # -----------------------------------------------------------------------
    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    # -----------------------------------------------------------------------
    # count_words_with_prefix — how many stored words begin with `prefix`.
    # The cached node.count makes this O(p), no subtree traversal needed.
    # -----------------------------------------------------------------------
    def count_words_with_prefix(self, prefix: str) -> int:
        if prefix == "":
            # Every inserted non-empty word passes through some child of root;
            # sum their counts. (root.count is not maintained, by design.)
            return sum(child.count for child in self.root.children.values())
        node = self._walk(prefix)
        return node.count if node is not None else 0

    # -----------------------------------------------------------------------
    # delete — remove `word` if present, pruning ONLY the nodes that no other
    # word needs. The gotcha: if `word` is a prefix of a longer stored word
    # (e.g. delete "car" while "card" stays), we must NOT remove shared nodes —
    # we only clear the is_end flag. Recursion returns "is my child now safe to
    # remove?" upward. Time O(m).
    # Returns True if the word was present and removed.
    # -----------------------------------------------------------------------
    def delete(self, word: str) -> bool:
        if not self.search(word):
            return False             # deleting a non-existent word is a no-op

        def _prune(node: TrieNode, depth: int) -> bool:
            # Returns True if `node` can be removed from its parent's children.
            if depth == len(word):
                node.is_end = False  # unmark the word
            else:
                ch = word[depth]
                child = node.children[ch]
                child.count -= 1     # one fewer word passes through the child
                if _prune(child, depth + 1):
                    del node.children[ch]
            # A node is removable only if it is not the end of another word
            # AND has no remaining children (no other word needs it).
            return not node.is_end and not node.children

        _prune(self.root, 0)
        # The empty-string word lives on root.is_end; clearing it above suffices.
        return True

    # -----------------------------------------------------------------------
    # internal: walk the trie following `s`; return the final node or None.
    # -----------------------------------------------------------------------
    def _walk(self, s: str) -> Optional[TrieNode]:
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


# ===========================================================================
# TESTS — normal behavior + the gotchas, all via assert. Run from main().
# ===========================================================================
def _test() -> None:
    # --- basic insert / search / prefix ------------------------------------
    t = Trie()
    for w in ["apple", "app", "application", "apt"]:
        t.insert(w)

    assert t.search("app") is True            # "app" was inserted as a word
    assert t.search("apple") is True
    assert t.starts_with("appl") is True      # prefix of "apple"/"application"
    assert t.search("appl") is False          # GOTCHA: a prefix is NOT a word

    # --- missing words / prefixes ------------------------------------------
    assert t.search("banana") is False
    assert t.starts_with("xyz") is False
    assert t.starts_with("appz") is False     # diverges at the 'z'

    # --- prefix-is-not-a-word (the is_end flag is what decides) -------------
    t2 = Trie()
    t2.insert("hello")
    assert t2.starts_with("hell") is True     # path exists...
    assert t2.search("hell") is False         # ...but is_end is False here

    # --- empty string is a legitimate word ---------------------------------
    t3 = Trie()
    assert t3.search("") is False             # not inserted yet
    t3.insert("")
    assert t3.search("") is True              # now stored on root.is_end
    assert t3.starts_with("") is True         # empty prefix matches everything

    # --- duplicate inserts are idempotent for membership -------------------
    t4 = Trie()
    t4.insert("dog")
    t4.insert("dog")
    assert t4.search("dog") is True
    # count counts INSERTS, so a duplicate bumps it (mirrors a multiset/freq use)
    assert t4.count_words_with_prefix("dog") == 2

    # --- count_words_with_prefix -------------------------------------------
    assert t.count_words_with_prefix("app") == 3   # app, apple, application
    assert t.count_words_with_prefix("appl") == 2  # apple, application
    assert t.count_words_with_prefix("ap") == 4    # + apt
    assert t.count_words_with_prefix("z") == 0     # nothing
    assert t.count_words_with_prefix("") == 4      # all four words

    # --- delete: remove a leaf word, shared nodes survive ------------------
    # GOTCHA: deleting "app" must NOT break "apple"/"application" which share
    # the "app" path. We only clear is_end on the "app" node.
    assert t.delete("app") is True
    assert t.search("app") is False           # gone as a word
    assert t.search("apple") is True          # shared prefix preserved
    assert t.starts_with("app") is True       # path still needed by apple/...
    assert t.count_words_with_prefix("app") == 2

    # --- delete a word that is a prefix of another (the classic) -----------
    t5 = Trie()
    t5.insert("car")
    t5.insert("card")
    assert t5.delete("car") is True
    assert t5.search("car") is False
    assert t5.search("card") is True          # untouched
    assert t5.starts_with("car") is True      # nodes kept for "card"

    # --- delete that should actually prune dead nodes ----------------------
    t6 = Trie()
    t6.insert("cat")
    assert t6.delete("cat") is True
    assert t6.search("cat") is False
    assert t6.starts_with("c") is False       # whole dead branch pruned
    assert t6.root.children == {}             # trie is empty again

    # --- delete of a non-existent / mere-prefix word is a no-op ------------
    t7 = Trie()
    t7.insert("test")
    assert t7.delete("tea") is False          # never inserted
    assert t7.delete("tes") is False          # a prefix, not a stored word
    assert t7.search("test") is True          # nothing was harmed

    # --- case sensitivity ---------------------------------------------------
    t8 = Trie()
    t8.insert("Apple")
    assert t8.search("Apple") is True
    assert t8.search("apple") is False        # 'A' != 'a' — case-sensitive
    assert t8.starts_with("app") is False


def main() -> None:
    _test()
    print("fundamentals.py: all examples verified ✔")


if __name__ == "__main__":
    main()
