"""
    Implement a trie with insert, search, and startsWith methods.
    
    Example:
    
    Trie trie = new Trie();
    
    trie.insert("apple");
    trie.search("apple");   // returns true
    trie.search("app");     // returns false
    trie.startsWith("app"); // returns true
    trie.insert("app");
    trie.search("app");     // returns true
    Note:
    
    You may assume that all inputs are consist of lowercase letters a-z.
    All inputs are guaranteed to be non-empty strings.

"""
class TrieNode():
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)

class Trie():
    def __init__(self):
        """
            Initialize your data structure here.
            self.root = {}
            """
        self.root = TrieNode()
    
    
    def insert(self, word):
        """
            Inserts a word into the trie.
            :type word: str
            :rtype: void
            p = self.root
            for c in word:
            if c not in p:
            p[c] = {}
            p = p[c]
            p['#'] = True
            """
        p = self.root
        for c in word:
            if not p.children.get(c):
                p.children[c] = TrieNode()
            p = p.children[c]
        p.is_word = True
    
    def search(self, word):
        """
            Returns if the word is in the trie.
            :type word: str
            :rtype: bool
            """
        node = self.find(word)
        return node is not None and node.is_word
    
    
    def startsWith(self, prefix):
        """
            Returns if there is any word in the trie that starts with the given prefix.
            :type prefix: str
            :rtype: bool
            """
        return self.find(prefix) is not None
    
    def find(self, prefix):
        """
            p = self.root
            for c in word:
            if c not in p:
            return None
            p = p[c]
            return p
            """
        p =self.root
        for c in prefix:
            if not p.children.get(c):
                return None
            p = p.children[c]
        return p


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
