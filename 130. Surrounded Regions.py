"""
    Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
    
    A region is captured by flipping all 'O's into 'X's in that surrounded region.
    
    Example:
    
    X X X X
    X O O X
    X X O X
    X O X X
    After running your function, the board should be:
    
    X X X X
    X X X X
    X X X X
    X O X X
    Explanation:
    
    Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
def solve(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    if not board: return []
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    queue = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i == 0 or i == len(board)-1) or (j == 0 or j == len(board)-1) and board[i][j] == 'O':
                queue.append((i,j))

    while queue:
        r, c = queue.pop()
        if 0 <= r <= len(board)-1 and 0 <= c <= len(board[0]) and board[r][c] == 'O':
            board[r][c] = 'D'
            for dir in directions:
                x, y = r + dir[0], c + dir[1]
                queue.append((x,y))

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'D':
                board[i][j] = 'O'



