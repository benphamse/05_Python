class TrieNode:
    """Node in the Trie data structure."""
    
    def __init__(self):
        self.children = {}  # Dictionary mapping characters to TrieNode
        self.isWord = False  # True if this node represents end of a word


class WordDictionary:
    """
    Word Dictionary that supports adding words and searching with wildcards.
    
    The search can include '.' as a wildcard that matches any letter.
    
    Time Complexity:
        - addWord: O(m) where m is the length of the word
        - search: O(m) for exact match, O(26^m) worst case with all wildcards
    
    Space Complexity: O(n * m) where n is number of words and m is average word length
    """

    def __init__(self):
        """Initialize the WordDictionary with an empty root node."""
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Add a word to the data structure.
        
        Args:
            word: The word to add
        """
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Search for a word in the data structure.
        Supports '.' as a wildcard that matches any single letter.
        
        Args:
            word: The word to search for (may contain '.')
            
        Returns:
            True if the word exists in the dictionary, False otherwise
        """
        return self._dfs(0, self.root, word)
    
    def _dfs(self, idx: int, node: TrieNode, word: str) -> bool:
        """
        Helper function to perform depth-first search.
        
        Args:
            idx: Current character index in the word
            node: Current TrieNode being examined
            word: The word being searched for
            
        Returns:
            True if the word is found, False otherwise
        """
        if idx == len(word):
            return node.isWord
        
        char = word[idx]
        
        # Wildcard: try all possible children
        if char == '.':
            for child in node.children.values():
                if self._dfs(idx + 1, child, word):
                    return True
        
        # Regular character: check if exists in children
        if char in node.children:
            return self._dfs(idx + 1, node.children[char], word)
        
        return False


# Example usage and test cases
if __name__ == "__main__":
    # Your WordDictionary object will be instantiated and called as such:
    obj = WordDictionary()
    
    # Test case 1: Basic operations
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    
    print(obj.search("pad"))      # False
    print(obj.search("bad"))      # True
    print(obj.search(".ad"))      # True (matches "bad", "dad", "mad")
    print(obj.search("b.."))      # True (matches "bad")
    print(obj.search("b.d"))      # True (matches "bad")
    print(obj.search("..."))      # True (matches "bad", "dad", "mad")
    print(obj.search(".a."))      # True
    print(obj.search("..d"))      # True
    print(obj.search("b..d"))     # False (4 characters, we only have 3-letter words)
    
    # Test case 2: Multiple lengths
    wordDict = WordDictionary()
    wordDict.addWord("a")
    wordDict.addWord("ab")
    wordDict.addWord("abc")
    wordDict.addWord("abcd")
    
    print(wordDict.search("a"))       # True
    print(wordDict.search("."))       # True (matches "a")
    print(wordDict.search(".."))      # True (matches "ab")
    print(wordDict.search("..."))     # True (matches "abc")
    print(wordDict.search("...."))    # True (matches "abcd")
    print(wordDict.search("....."))   # False
