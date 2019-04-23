"""
    Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
    
    Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
    
    Example 1:
    
    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
    Example 2:
    
    [[0,0,0,0,0,0,0,0]]
    Given the above grid, return 0.
    Note: The length of each dimension in the given grid does not exceed 50.

"""
def maxAreaOfIsland(grid):
    """
        :type grid: List[List[int]]
        :rtype: int
        
        BFS
        """
        m, n = len(grid), len(grid[0])
        result ,tres = 0, 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for x in range(m):
            for y in range(n):
                if grid[x][y]==1:
                    tres = 0
                    queue = [(x,y)]
                    grid[x][y] = 0
                    
                    while queue:
                        curx,cury = queue.pop(0)
                        tres += 1
                        for dir in directions:
                            i, j = curx + dir[0], cury + dir[1]
                            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                                queue.append((i,j))
                                grid[i][j] = 0
            
        result = max(result,tres)
        
        return result
        
        
        """
            
            DFS
            m, n = len(grid), len(grid[0])
            
            def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]==1:
            grid[i][j] = 0
            return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0
            
            result = 0
            for x in range(m):
            for y in range(n):
            if grid[x][y]==1:
            result = max(result, dfs(x, y))
            return result
            """
