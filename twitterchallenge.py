
grid1 = ['001', '011', '100']
grid2 = ['001', '011', '101']

def countMatches(grid1, grid2):
    # Write your code here
    res = []
    result1 = []
    result2 = []
    count1, count2 = 0, 0
    grid1 = trans(grid1)
    grid2 = trans(grid2)
    for i in range(len(grid1)):
        for j in range(len(grid1[0])):
            if grid1[i][j] == 1:
                result1.append(dfs(grid1, i, j, res))
                res = []
                count1 += 1
            if grid2[i][j] == 1:
                result2.append(dfs(grid2, i, j, res))
                res = []
                count2 += 1
    if count1 > count2:
        acc = [cnn for cnn in result2 if cnn in result1]
    else:
        acc = [cnn for cnn in result1 if cnn in result2]
    return (len(acc))


# transfer the string array into integer array
def trans(grid):
    tmp = []
    pos_grid = []
    for _ in range(len(grid)):
        for sub in grid[_]:
            tmp.append(int(sub))
        pos_grid.append(tmp)
        tmp = []
    return pos_grid


# Recrusively check the contiguous cells of the current "1" cell, modify the vall of visited cell into "x",
# which simply means not "1".
def dfs(grid, i, j, tmp):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
        return
    grid[i][j] = 'x'
    tmp.append((i, j))
    dfs(grid, i - 1, j, tmp)
    dfs(grid, i, j - 1, tmp)
    dfs(grid, i + 1, j, tmp)
    dfs(grid, i, j + 1, tmp)
    return tmp

print(countMatches(grid1,grid2))
