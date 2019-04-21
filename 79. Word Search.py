"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
 ['A','B','C','E'],
 ['S','F','C','S'],
 ['A','D','E','E']
 ]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

"""
def exist(board, word):
    if not board: return False
    firstchr = word[0]
    for i in range(len(board)):
        for j in range(len(board[0)):
            if board[i][j] == firstchr and dfs(board, i,j,word):
               return True
    return False


def dfs(board, x, y, word):
    if len(word) == 0:
        return True
    
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    if x < 0 or x > len(board) -1 or y < 0 or y > len(board) -1 and board[x][y]!= word[0]:
        return False
             
    board[x][y] = '#'
    for dir in directions:
        r, c = x + dir[0], y + dir[1]
        if dfs(board,r,c,word[1:]):
           return True
    
    board[x][y] = word[0]
    return False
