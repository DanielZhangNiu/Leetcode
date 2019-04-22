"""
    Given a 2D board and a list of words from the dictionary, find all words in the board.
    
    Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
    

    Example:
    
    Input:
    board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    
    Output: ["eat","oath"]
    
    
    Note:
    
    All inputs are consist of lowercase letters a-z.
    The values of words are distinct.

"""
"""
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_word = False

class Trietree:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        p =self.root
        for c in word:
            if not p.children.get(c):
                p.children[c] = Node()
            p = p.children[c]
        p.is_word = True
    
    def search(self,word):
        node = self.find(word)
        return node is not None and node.is_word
    
    def prefix(self,prefix):
        return self.find(prefix) is not None
    
    def find(self,word):
        p = self.root
        for c in word:
            if not p.children.get(c):
                return None
            p = p.children[c]
        return p


class Solution:
    def dfs(self,board,r,c,path,node):
        if node.is_word:
            self.res.append(path)
            node.is_word = False
        
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return
        
        tmp = board[r][c]
        newnode = node.children.get(tmp)
        
        if not newnode:
            return
        
        for dir in self.directions:
            x = r + dir[0]
            y = c + dir[1]
            board[r][c] = "#"
            self.dfs(board,x,y,path+tmp,newnode)
            board[r][c] = tmp

                
    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
        if not board:return []
        self.res = []
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
                
        self.trie = Trietree()
        node = self.trie.root
        for word in words:
            self.trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i,j,"",node)
                                                
        return self.res
"""

class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_word = False

class Solution:
    def __init__(self):
        self.root = Node()
    
    def addword(self, word):
        p =self.root
        for c in word:
            if not p.children.get(c):
                p.children[c] = Node()
            p = p.children[c]
        p.is_word = True

    def dfs(self,board,r,c,path,node):
        if node.is_word:
            self.res.append(path)
            node.is_word = False
        
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return
        
        tmp = board[r][c]
        newnode = node.children.get(tmp)
        
        if not newnode:
            return
        
        for dir in self.directions:
            x = r + dir[0]
            y = c + dir[1]
            board[r][c] = "#"
            self.dfs(board,x,y,path+tmp,newnode)
            board[r][c] = tmp
    

    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
        if not board:return []
        self.res = []
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        node = self.root
        for word in words:
            self.addword(word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i,j,"",node)
        
    return self.res
