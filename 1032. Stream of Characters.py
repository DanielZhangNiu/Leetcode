"""
    Implement the StreamChecker class as follows:
    
    StreamChecker(words): Constructor, init the data structure with the given words.
    query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
    
    
    Example:
    
    StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
    streamChecker.query('a');          // return false
    streamChecker.query('b');          // return false
    streamChecker.query('c');          // return false
    streamChecker.query('d');          // return true, because 'cd' is in the wordlist
    streamChecker.query('e');          // return false
    streamChecker.query('f');          // return true, because 'f' is in the wordlist
    streamChecker.query('g');          // return false
    streamChecker.query('h');          // return false
    streamChecker.query('i');          // return false
    streamChecker.query('j');          // return false
    streamChecker.query('k');          // return false
    streamChecker.query('l');          // return true, because 'kl' is in the wordlist
    
    
    Note:
    
    1 <= words.length <= 2000
    1 <= words[i].length <= 2000
    Words will only consist of lowercase English letters.
    Queries will only consist of lowercase English letters.
    The number of queries is at most 40000.

"""

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)

class StreamChecker:
    
    def __init__(self, words: List[str]):
        if not words: return False
        self.root = TrieNode()
        # reversely add the words into trie, we will keep query based on tye sequence
        for word in words:
            self.addNode(word[::-1])
        self.buff = []
        self.maxl = len(max(words, key = lambda x: len(x)))
    
    def query(self, letter: str) -> bool:
        self.buff.append(letter)
        s = ""
        for i in range(len(self.buff) - 1, -1, -1):
            s += self.buff[i]
            if len(s) > self.maxl:
                break
            res = self.find(s)
            if not res:
                return False
            if res.is_word:
                return True
        return False
    
    
    def addNode(self,word):
        p = self.root
        for ch in word:
            if not p.children.get(ch):
                p.children[ch]= TrieNode()
            p = p.children[ch]
        p.is_word = True
    
    def find(self,word):
        p = self.root
        for ch in word:
            if not p.children.get(ch):
                return False
            p = p.children[ch]
        return p




# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
