"""
 Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

 Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

 Example 1:

 11000
 11000
 00011
 00011
 Given the above grid map, return 1.
 Example 2:

 11011
 10000
 00001
 11011
 Given the above grid map, return 3.

 Notice that:
 11
 1
 and
  1
 11
 are considered different island shapes, because we do not consider reflection / rotation.
 Note: The length of each dimension in the given grid does not exceed 50.
"""
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        dummy = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = self.dfs(grid,i,j,0,0,[])
                    dummy.add(tuple(res))
        
        return len(dummy)

    def dfs(self, grid, r, c,mr,mc, path):
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        grid[r][c] = 'X'
        for dir in directions:
            nr, nc = dir[0] + r, dir[1] + c
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                nmr,nmc = dir[0] + mr, dir[1] + mc
                path.append((nmr,nmc))
                self.dfs(grid, nr , nc, nmr,nmc, path)
        return path
