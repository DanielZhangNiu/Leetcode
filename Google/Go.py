def count_capture(board, row, col):
    def visit(board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]): return 0
        if board[i][j] == 'e': return float('-inf')
        if board[i][j] == 'b': return 0

        board[i][j] = 'b'
        count = 1
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            count += visit(board, i + y, j + x)

        return count

    board[row][col] = 'b'

    maxcount = 0
    h, w = len(board), len(board[0])
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'w':
                count = visit(board, i, j)
                maxcount = max(count, maxcount)

    return maxcount


if __name__ == '__main__':
    board = [['e', 'e', 'e', 'b', 'b', 'b', 'b'],
             ['e', 'e', 'b', 'w', 'w', 'w', 'b'],
             ['e', 'e', 'b', 'w', 'b', 'e', 'b'],
             ['e', 'e', 'b', 'b', 'b', 'e', 'e']]
    print(count_capture(board, 2, 5))
