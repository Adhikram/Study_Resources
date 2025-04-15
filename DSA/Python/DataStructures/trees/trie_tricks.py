"""
Common Trie (Prefix Tree) Tricks and Patterns for Coding Interviews

This file contains popular trie manipulation techniques and patterns
that frequently appear in coding interviews.
"""

def autocomplete_system():
    """
    Implementing an Autocomplete System:
    - Store words in trie
    - Track frequency/weight of words
    - Return top k suggestions
    """
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False
            self.frequency = 0
            self.words = set()  # Store complete words at this node
    
    class AutocompleteSystem:
        def __init__(self, words, times):
            self.root = TrieNode()
            self.keyword = ""
            
            # Insert all words with their frequencies
            for word, count in zip(words, times):
                self._insert(word, count)
        
        def _insert(self, word, frequency):
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.words.add(word)
            node.is_end = True
            node.frequency = frequency
        
        def input(self, c):
            if c == "#":
                # Insert the complete word
                self._insert(self.keyword, 1)
                self.keyword = ""
                return []
            
            self.keyword += c
            node = self.root
            
            # Find node for current prefix
            for char in self.keyword:
                if char not in node.children:
                    return []
                node = node.children[char]
            
            # Get all words with current prefix
            words_with_freq = [(word, self._get_frequency(word)) 
                             for word in node.words]
            
            # Sort by frequency and lexicographically
            words_with_freq.sort(key=lambda x: (-x[1], x[0]))
            return [word for word, _ in words_with_freq[:3]]
        
        def _get_frequency(self, word):
            node = self.root
            for char in word:
                node = node.children[char]
            return node.frequency

def word_search_ii():
    """
    Word Search II (Find words in board):
    - Build trie from dictionary
    - DFS with trie on board
    """
    def find_words(board, words):
        def dfs(node, i, j, path, result):
            if node.is_end:
                result.add(path)
                
            if (i < 0 or i >= len(board) or 
                j < 0 or j >= len(board[0])):
                return
            
            temp = board[i][j]
            if temp not in node.children:
                return
            
            board[i][j] = '#'  # Mark as visited
            
            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                ni, nj = i + di, j + dj
                dfs(node.children[temp], ni, nj, path + temp, result)
            
            board[i][j] = temp  # Restore
        
        # Build trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
        
        # Search in board
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(root, i, j, "", result)
        
        return list(result)

def maximum_xor():
    """
    Maximum XOR of Two Numbers:
    - Build binary trie
    - Find maximum XOR pair
    """
    class BinaryTrieNode:
        def __init__(self):
            self.children = {}  # 0 and 1 only
    
    def find_maximum_xor(nums):
        # Build binary trie
        root = BinaryTrieNode()
        for num in nums:
            node = root
            for i in range(31, -1, -1):  # From MSB to LSB
                bit = (num >> i) & 1
                if bit not in node.children:
                    node.children[bit] = BinaryTrieNode()
                node = node.children[bit]
        
        # Find maximum XOR
        max_xor = 0
        for num in nums:
            node = root
            current_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                # Try to go opposite way
                opposite = 1 - bit
                if opposite in node.children:
                    current_xor |= (1 << i)
                    node = node.children[opposite]
                else:
                    node = node.children[bit]
            max_xor = max(max_xor, current_xor)
        
        return max_xor

def replace_words():
    """
    Replace Words with Roots:
    - Build trie from dictionary of roots
    - Find shortest root for each word
    """
    def replace_with_root(dictionary, sentence):
        # Build trie of roots
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
        
        def find_root(word):
            node = root
            for i, char in enumerate(word):
                if node.is_end:
                    return word[:i]
                if char not in node.children:
                    return word
                node = node.children[char]
            return word if not node.is_end else word
        
        # Process each word in sentence
        words = sentence.split()
        return " ".join(find_root(word) for word in words)

def word_squares():
    """
    Word Squares Problem:
    - Build prefix trie
    - Backtrack with prefix constraints
    """
    def find_word_squares(words):
        # Build prefix trie
        trie = {}
        for word in words:
            for i in range(len(word)):
                prefix = word[:i]
                if prefix not in trie:
                    trie[prefix] = []
                trie[prefix].append(word)
        
        def get_words_with_prefix(prefix):
            return trie.get(prefix, [])
        
        def backtrack(square, n):
            if len(square) == n:
                result.append(square[:])
                return
            
            prefix = ""
            for word in square:
                prefix += word[len(square)]
            
            for word in get_words_with_prefix(prefix):
                square.append(word)
                backtrack(square, n)
                square.pop()
        
        result = []
        for word in words:
            backtrack([word], len(word))
        return result

# Interview Tips:
"""
1. Common Trie Applications:
   - Autocomplete/Type-ahead
   - Spell checker
   - IP routing table
   - Phone directory
   - Word games
   - Dictionary operations

2. Optimization Techniques:
   - Compress nodes with single child
   - Store frequency information
   - Use hash map vs array for children
   - Maintain additional metadata
   - Implement delete operation

3. Problem-Solving Patterns:
   - Word by word insertion
   - Character by character search
   - Prefix matching
   - DFS with trie
   - Backtracking with trie

4. Common Edge Cases:
   - Empty string
   - Single character
   - Duplicate words
   - Case sensitivity
   - Special characters
   - Overlapping prefixes

5. Time/Space Analysis:
   - Insertion: O(m) time, where m is word length
   - Search: O(m) time
   - Space: O(ALPHABET_SIZE * m * n) for n words
   - Prefix operations: O(p) for prefix length p
   - Delete: O(m) time

6. Advanced Techniques:
   - Ternary search tree
   - Compressed trie
   - Suffix trie/tree
   - Radix tree
   - Patricia trie
""" 