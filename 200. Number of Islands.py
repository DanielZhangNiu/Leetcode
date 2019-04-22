"""
    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
    
    Example 1:
    
    Input:
    11110
    11010
    11000
    00000
    
    Output: 1
    Example 2:
    
    Input:
    11000
    11000
    00100
    00011
    
    Output: 3

"""
def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid: return 0
    res = 0
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid,i,j)
                res += 1
    return res
    
    def dfs(grid,r,c):
        
        grid[r][c] = 'x'
        for dir in directions:
            x, y = r + dir[0], c + dir[1]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                dfs(grid,x,y)
    

    
    
    """
        union Find
    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])
        
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.parent[rooty] = rootx
            self.count -= 1
        
    def dfs(self, i,j,grid):
        n = len(grid[0])
        for d in self.directions:
        nr, nc = i + d[0], j + d[1]
        if nr >=0 and nr < len(grid) and nc >=0 and nc < n and grid[nr][nc] == '1':
            self.union(i*n+j, nr*n+nc)
        
    def numIslands(self, grid):
        
    :type grid: List[List[str]]
    :rtype: int
        
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i*n + j] = i*n + j
                    self.count += 1
        
        self.directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(i,j,grid)
        return self.count
        """
